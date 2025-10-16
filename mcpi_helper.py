"""Helper functions for interfacing with Minecraft from EduBlocks."""
from __future__ import annotations

from typing import List, Tuple

from mcpi.minecraft import Minecraft
from mcpi import block

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 4711
DEFAULT_MATERIAL = block.STONE.id


def place_block(
    host: str = DEFAULT_HOST, port: int = DEFAULT_PORT, material: int = DEFAULT_MATERIAL
) -> Tuple[int, int, int]:
    """Place a block (default material) at a fixed location and return its coordinates."""
    mc = Minecraft.create(host, port)
    x, y, z = 0, 64, 0
    mc.setBlock(x, y, z, material)
    mc.postToChat(f"edublocks: placed block at {x},{y},{z} using material {material}")
    return x, y, z


def move_player(
    x: int = 0,
    y: int = 64,
    z: int = 0,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
) -> None:
    """Move the player to the supplied coordinates."""
    mc = Minecraft.create(host, port)
    mc.player.setPos(x, y, z)
    mc.postToChat(f"edublocks: moved player to {x},{y},{z}")


def build_walls(
    x: int = 0,
    y: int = 64,
    z: int = 0,
    width: int = 5,
    height: int = 3,
    material: int = DEFAULT_MATERIAL,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
) -> List[Tuple[int, int, int]]:
    """Build a hollow rectangular set of walls using the given material and return placed blocks."""
    mc = Minecraft.create(host, port)
    mc.postToChat(f"edublocks: building house walls at {x},{y},{z} using material {material}")

    placed_blocks: List[Tuple[int, int, int]] = []

    # Front and back walls
    for wall_z in [z, z + width - 1]:
        for dx in range(width):
            for dy in range(height):
                block_x = x + dx
                block_y = y + dy
                block_z = wall_z
                mc.setBlock(block_x, block_y, block_z, material)
                placed_blocks.append((block_x, block_y, block_z))

    # Left and right walls (excluding corners already placed)
    for wall_x in [x, x + width - 1]:
        for dz in range(1, width - 1):
            for dy in range(height):
                block_x = wall_x
                block_y = y + dy
                block_z = z + dz
                mc.setBlock(block_x, block_y, block_z, material)
                placed_blocks.append((block_x, block_y, block_z))

    return placed_blocks
