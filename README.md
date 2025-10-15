# EduBlocks Minecraft

A Minecraft integration for EduBlocks that provides block-based programming capabilities for interacting with Minecraft Pi Edition or compatible servers using the MCPI protocol.

## Features

- Place blocks in the Minecraft world
- Move the player to specific coordinates
- Build structures (like walls)
- Send messages to Minecraft chat
- Automatic reconnection handling
- Fallback dummy implementation for development without Minecraft

## Requirements

- Python 3.x
- MCPI library (`pip install mcpi`)
- Minecraft Pi Edition or a compatible server (like RaspberryJuice)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Include the blocks in your EduBlocks project using the provided definition files:
- `definitions.ts` - Block definitions
- `generators.ts` - Code generators
- `toolbox.xml` - Toolbox configuration

## Available Blocks

The extension provides several Minecraft control blocks:

1. **Import Blocks**
   - Import MCPI blocks
   - Import MCPI structures

2. **Basic Operations**
   - Place a block and get its position/type
   - Move player to coordinates
   - Build wall structure

## Example Usage

Once the blocks are imported, you can:
- Place blocks at specific coordinates
- Move the player around the world
- Build walls of specified width and height
- Get block information from the world

Default server connection is to `localhost:4711`.

## API Reference

### MCPIClient

The `MCPIClient` class provides a robust interface to Minecraft with:
- Safe imports (works even if MCPI isn't installed)
- Automatic reconnection handling
- Helper methods for common operations

Core methods:
- `post_to_chat(message)` - Send a message to Minecraft chat
- `set_block(x, y, z, block_id, block_data=0)` - Place a block
- `get_block(x, y, z)` - Get block ID at position
- `player_set_pos(x, y, z)` - Move player to position
- `player_get_pos()` - Get player's current position
- `set_blocks(x1, y1, z1, x2, y2, z2, block_id, block_data=0)` - Place multiple blocks

## Project Structure

- `mcpi_structures.py` - Structure building functions
- `definitions.ts` - Block definitions for EduBlocks
- `generators.ts` - Code generation for blocks
- `toolbox.xml` - Toolbox configuration
- `config.json` - Project configuration

## Development

The project includes a dummy implementation for development without an active Minecraft server. This allows for testing and development of blocks without requiring a running Minecraft instance.

## Terms of Use

See [EduBlocks terms](https://www.anaconda.com/legal/terms/edublocks)
