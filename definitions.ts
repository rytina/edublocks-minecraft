import * as Blockly from "blockly";

const MCPI_COLOR = "#5C9C3D"; // Minecraft grass block green

Blockly.Blocks["import_mcpi_helper"] = {
    init: function () {
        this.appendDummyInput().appendField("from mcpi_helper import *");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(MCPI_COLOR);
        this.setTooltip("Import MCPI helper functions");
    },
};

Blockly.Blocks["mcpi_place_block"] = {
    init: function () {
        this.appendDummyInput().appendField("place_block(");
        this.appendValueInput("host")
            .setCheck("String")
            .appendField("host=");
        this.appendValueInput("port")
            .setCheck("Number")
            .appendField(", port=");
        this.appendDummyInput().appendField(")");
        this.setOutput(true, null);
        this.setInputsInline(true);
        this.setColour(MCPI_COLOR);
        this.setTooltip("Place a block and return its position");
    },
};

Blockly.Blocks["mcpi_move_player"] = {
    init: function () {
        this.appendDummyInput().appendField("move_player(");
        this.appendValueInput("x")
            .setCheck("Number")
            .appendField("x=");
        this.appendValueInput("y")
            .setCheck("Number")
            .appendField(", y=");
        this.appendValueInput("z")
            .setCheck("Number")
            .appendField(", z=");
        this.appendValueInput("host")
            .setCheck("String")
            .appendField(", host=");
        this.appendValueInput("port")
            .setCheck("Number")
            .appendField(", port=");
        this.appendDummyInput().appendField(")");
        this.setOutput(true, null);
        this.setInputsInline(true);
        this.setColour(MCPI_COLOR);
        this.setTooltip("Move the player to coordinates");
    },
};

Blockly.Blocks["mcpi_build_walls"] = {
    init: function () {
        this.appendDummyInput().appendField("build_walls(");
        this.appendValueInput("x")
            .setCheck("Number")
            .appendField("x=");
        this.appendValueInput("y")
            .setCheck("Number")
            .appendField(", y=");
        this.appendValueInput("z")
            .setCheck("Number")
            .appendField(", z=");
        this.appendValueInput("width")
            .setCheck("Number")
            .appendField(", width=");
        this.appendValueInput("height")
            .setCheck("Number")
            .appendField(", height=");
        this.appendValueInput("material")
            .setCheck(null)
            .appendField(", material=");
        this.appendValueInput("host")
            .setCheck("String")
            .appendField(", host=");
        this.appendValueInput("port")
            .setCheck("Number")
            .appendField(", port=");
        this.appendDummyInput().appendField(")");
        this.setOutput(true, null);
        this.setInputsInline(true);
        this.setColour(MCPI_COLOR);
        this.setTooltip("Build a wall structure");
    },
};
