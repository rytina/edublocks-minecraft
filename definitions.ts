const mcpiColor = "#5C9C3D"; // Minecraft grass block green


Blockly.Blocks["import_mcpi_structures"] = {
    init: function() {
        this.appendDummyInput()
            .appendField("from mcpi_structures import *");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(mcpiColor);
        this.setTooltip("Import MCPI structure building functions");
    }
};

Blockly.Blocks["import_mcpi_blocks"] = {
    init: function() {
        this.appendDummyInput()
            .appendField("from mcpi_blocks import *");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(mcpiColor);
        this.setTooltip("Import MCPI block placement functions");
    }
};

Blockly.Blocks["mcpi_place_block"] = {
    init: function() {
        this.appendDummyInput()
            .appendField("result")
        this.appendValueInput("host")
            .setCheck("String")
            .appendField(" = example_place_and_report(host=");
        this.appendValueInput("port")
            .setCheck("Number")
            .appendField(", port=");
        this.appendDummyInput()
            .appendField(")");
        this.setOutput(true, null);
        this.setColour(mcpiColor);
        this.setTooltip("Place a block and get its position/type");
    }
};

Blockly.Blocks["mcpi_move_player"] = {
    init: function() {
        this.appendDummyInput()
            .appendField("pos = example_move_player(");
        this.appendValueInput("x")
            .setCheck("Number")
            .appendField("x=");
        this.appendValueInput("y")
            .setCheck("Number")
            .appendField(", y=");
        this.appendValueInput("z")
            .setCheck("Number")
            .appendField(", z=");
        this.appendDummyInput()
            .appendField(")");
        this.setOutput(true, null);
        this.setColour(mcpiColor);
        this.setTooltip("Move player to coordinates");
    }
};

Blockly.Blocks["mcpi_build_wall"] = {
    init: function() {
        this.appendDummyInput()
            .appendField("blocks = example_build_wall(");
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
        this.appendDummyInput()
            .appendField(")");
        this.setOutput(true, null);
        this.setColour(mcpiColor);
        this.setTooltip("Build a wall structure");
    }
};
  