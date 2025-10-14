# MCPI example wrapper (replaces the original ML text example).
from mcpi_adapter import MCPIClient
import logging

logger = logging.getLogger(__name__)

def example_build_wall(host: str = "127.0.0.1", port: int = 4711, x: int = 0, y: int = 64, z: int = 0, width: int = 5, height: int = 3):
    """Build a simple wall of stone starting at x,y,z with given width/height."""
    mc = MCPIClient(host=host, port=port)
    mc.post_to_chat(f"edublocks: building wall at {x},{y},{z}")
    positions = []
    for dx in range(width):
        for dy in range(height):
            mx = x + dx
            my = y + dy
            mz = z
            mc.set_block(mx, my, mz, 1)
            positions.append((mx, my, mz))
    return positions
