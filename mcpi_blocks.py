# MCPI example wrapper (replaces the original ML example).
from mcpi_adapter import MCPIClient
import logging

logger = logging.getLogger(__name__)

def example_place_and_report(host: str = "127.0.0.1", port: int = 4711):
    """Connect to a MCPI server, post a chat message, place a block and report its id."""
    mc = MCPIClient(host=host, port=port)
    mc.post_to_chat("edublocks: placing a block at 0,64,0")
    mc.set_block(0, 64, 0, 1)
    block_id = mc.get_block(0, 64, 0)
    return {"x": 0, "y": 64, "z": 0, "block_id": int(block_id)}

def example_move_player(host: str = "127.0.0.1", port: int = 4711, x: float = 0.0, y: float = 65.0, z: float = 0.0):
    """Move the player to the specified coordinates and report the new position."""
    mc = MCPIClient(host=host, port=port)
    mc.player_set_pos(x, y, z)
    return mc.player_get_pos()
