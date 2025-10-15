# MCPI example wrapper (replaces the original ML text example).
from mcpi.minecraft import Minecraft as MCPIClient
import logging

logger = logging.getLogger(__name__)

def place_block(host: str = "127.0.0.1", port: int = 4711):
    """Place a block and report its position."""
    mc = MCPIClient.create(host=host, port=port)
    # Place a stone block at a fixed position (0, 64, 0)
    x, y, z = 0, 64, 0
    mc.setBlock(x, y, z, 1)  # 1 is the block ID for stone
    mc.post_to_chat(f"edublocks: placed block at {x},{y},{z}")
    return x, y, z

def move_player(x: int = 0, y: int = 64, z: int = 0, host: str = "127.0.0.1", port: int = 4711):
    """Move the player to specified coordinates."""
    mc = MCPIClient.create(host=host, port=port)
    mc.player.setPos(x, y, z)
    mc.post_to_chat(f"edublocks: moved player to {x},{y},{z}")
    return x, y, z

def build_walls(host: str = "127.0.0.1", port: int = 4711, x: int = 0, y: int = 64, z: int = 0, width: int = 5, height: int = 3):
    """Build four walls of stone to form a house outline starting at x,y,z with given width/height."""
    mc = MCPIClient.create(host=host, port=port)
    mc.postToChat(f"edublocks: building house walls at {x},{y},{z}")
    positions = []
    
    # Build front and back walls
    for wall_z in [z, z + width - 1]:
        for dx in range(width):
            for dy in range(height):
                mx = x + dx
                my = y + dy
                mz = wall_z
                mc.setBlock(mx, my, mz, 1)
                positions.append((mx, my, mz))
    
    # Build left and right walls (excluding corners to avoid duplicates)
    for wall_x in [x, x + width - 1]:
        for dz in range(1, width - 1):
            for dy in range(height):
                mx = wall_x
                my = y + dy
                mz = z + dz
                mc.setBlock(mx, my, mz, 1)
                positions.append((mx, my, mz))
    
    return positions
