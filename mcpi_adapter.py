"""MCPI adapter for RaspberryJuice / mcpi-compatible servers.

Provides a small, safe wrapper around the mcpi library with
reconnect behavior and a fallback dummy implementation so importing
the module doesn't crash when mcpi isn't installed (useful for
editing or static analysis in environments without the package).

Usage:
    from mcpi_adapter import MCPIClient
    mc = MCPIClient()
    mc.post_to_chat("hello")
    mc.set_block(0,64,0,1)
"""
from __future__ import annotations

import logging
import time
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


class _DummyMC:
    """Fallback implementation used when mcpi package is not available.

    It logs calls instead of making network connections, which keeps the
    rest of the extension usable for development and test.
    """

    class player:
        @staticmethod
        def setPos(x, y, z):
            logger.info("Dummy player.setPos(%s, %s, %s)", x, y, z)

        @staticmethod
        def getPos():
            logger.info("Dummy player.getPos()")
            return (0, 64, 0)

    @staticmethod
    def postToChat(msg):
        logger.info("Dummy postToChat: %s", msg)

    @staticmethod
    def setBlock(x, y, z, block_id, block_data=0):
        logger.info("Dummy setBlock %s,%s,%s -> %s.%s", x, y, z, block_id, block_data)

    @staticmethod
    def setBlocks(x1, y1, z1, x2, y2, z2, block_id, block_data=0):
        logger.info("Dummy setBlocks %s,%s,%s -> %s,%s,%s = %s.%s", x1, y1, z1, x2, y2, z2, block_id, block_data)

    @staticmethod
    def getBlock(x, y, z):
        logger.info("Dummy getBlock %s,%s,%s", x, y, z)
        return 0


try:
    # mcpi is the common Python package that implements the MCPI protocol
    # used by RaspberryJuice. Import lazily so the module import doesn't
    # fail if the package isn't installed.
    from mcpi.minecraft import Minecraft  # type: ignore
    from mcpi import block as mcpi_block  # type: ignore

    _HAS_MCPI = True
except Exception:  # pragma: no cover - environment dependent
    Minecraft = None  # type: ignore
    mcpi_block = None  # type: ignore
    _HAS_MCPI = False


class MCPIClient:
    """A thin wrapper around MCPI's Minecraft client.

    Features:
    - safe imports: works even if mcpi isn't installed (uses dummy)
    - reconnect loop with configurable retry delay
    - helper methods commonly used by educational examples
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 4711, reconnect: bool = True, retry_delay: float = 2.0):
        self.host = host
        self.port = int(port)
        self.reconnect = bool(reconnect)
        self.retry_delay = float(retry_delay)
        self.mc = None
        self._connect()

    def _connect(self) -> None:
        if not _HAS_MCPI:
            logger.warning("mcpi package not available; using dummy client")
            self.mc = _DummyMC()
            return

        # Try to connect, optionally retrying forever if reconnect=True
        while True:
            try:
                self.mc = Minecraft.create(address=self.host, port=self.port)
                logger.info("Connected to MCPI server %s:%s", self.host, self.port)
                return
            except Exception as exc:  # pragma: no cover - network behavior
                logger.warning("Failed to connect to MCPI server %s:%s - %s", self.host, self.port, exc)
                if not self.reconnect:
                    raise
                time.sleep(self.retry_delay)

    def _ensure(self) -> None:
        if self.mc is None:
            self._connect()

    def post_to_chat(self, message: str) -> None:
        """Post a message to the Minecraft chat."""
        try:
            self._ensure()
            self.mc.postToChat(str(message))
        except Exception as exc:  # pragma: no cover - runtime
            logger.warning("post_to_chat error: %s", exc)
            if self.reconnect:
                self._connect()

    def set_block(self, x: int, y: int, z: int, block_id: int, block_data: Optional[int] = 0) -> None:
        try:
            self._ensure()
            # Some mcpi implementations accept (id, data) or block.Block
            if block_data is None:
                self.mc.setBlock(int(x), int(y), int(z), int(block_id))
            else:
                self.mc.setBlock(int(x), int(y), int(z), int(block_id), int(block_data))
        except Exception as exc:  # pragma: no cover - runtime
            logger.warning("set_block error: %s", exc)
            if self.reconnect:
                self._connect()

    def set_blocks(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, block_id: int, block_data: Optional[int] = 0) -> None:
        try:
            self._ensure()
            if block_data is None:
                self.mc.setBlocks(int(x1), int(y1), int(z1), int(x2), int(y2), int(z2), int(block_id))
            else:
                self.mc.setBlocks(int(x1), int(y1), int(z1), int(x2), int(y2), int(z2), int(block_id), int(block_data))
        except Exception as exc:  # pragma: no cover - runtime
            logger.warning("set_blocks error: %s", exc)
            if self.reconnect:
                self._connect()

    def get_block(self, x: int, y: int, z: int) -> int:
        self._ensure()
        return int(self.mc.getBlock(int(x), int(y), int(z)))

    def player_set_pos(self, x: float, y: float, z: float) -> None:
        self._ensure()
        try:
            # mcpi exposes player.setPos
            self.mc.player.setPos(float(x), float(y), float(z))
        except Exception:
            # some mcpi variants require a different call, so try direct call
            try:
                self.mc.setPlayerPos(float(x), float(y), float(z))
            except Exception as exc:  # pragma: no cover - runtime
                logger.warning("player_set_pos error: %s", exc)

    def player_get_pos(self) -> Tuple[float, float, float]:
        self._ensure()
        pos = self.mc.player.getPos()
        # mcpi returns an object with x,y,z or a tuple
        try:
            return (float(pos.x), float(pos.y), float(pos.z))
        except Exception:
            try:
                return (float(pos[0]), float(pos[1]), float(pos[2]))
            except Exception:
                return (0.0, 0.0, 0.0)
