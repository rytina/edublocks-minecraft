# EduBlocks Minecraft

A Minecraft integration for EduBlocks that provides block-based programming capabilities for interacting with Minecraft Pi Edition or compatible servers using the MCPI protocol.

## Features

- Place blocks in the Minecraft world
- Move the player to specific coordinates
- Build structures (like walls)
- Send messages to Minecraft chat

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

The extension uses the standard MCPI API through the `mcpi.minecraft.Minecraft` class with the following core methods:
- `postToChat(message)` - Send a message to Minecraft chat
- `setBlock(x, y, z, block_id, block_data=0)` - Place a block
- `getBlock(x, y, z)` - Get block ID at position
- `player.setPos(x, y, z)` - Move player to position
- `player.getPos()` - Get player's current position
- `setBlocks(x1, y1, z1, x2, y2, z2, block_id, block_data=0)` - Place multiple blocks

## Project Structure

- `mcpi_structures.py` - Structure building functions
- `definitions.ts` - Block definitions for EduBlocks
- `generators.ts` - Code generation for blocks
- `toolbox.xml` - Toolbox configuration
- `config.json` - Project configuration

## Terms of Use

See [EduBlocks terms](https://www.anaconda.com/legal/terms/edublocks)
