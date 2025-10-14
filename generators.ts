
Blockly.Python["import_mcpi_structures"] = function() {
    const code = `from mcpi_structures import *\n`;
    return code;
};

Blockly.Python["import_mcpi_blocks"] = function() {
    const code = `from mcpi_blocks import *\n`;
    return code;
};

Blockly.Python["mcpi_place_block"] = function(block) {
    const host = Blockly.Python.valueToCode(block, "host", Blockly.Python.ORDER_NONE) || "\"127.0.0.1\"";
    const port = Blockly.Python.valueToCode(block, "port", Blockly.Python.ORDER_NONE) || "4711";
    const code = `example_place_and_report(host=${host}, port=${port})\n`;
    return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python["mcpi_move_player"] = function(block) {
    const x = Blockly.Python.valueToCode(block, "x", Blockly.Python.ORDER_NONE) || "0";
    const y = Blockly.Python.valueToCode(block, "y", Blockly.Python.ORDER_NONE) || "64";
    const z = Blockly.Python.valueToCode(block, "z", Blockly.Python.ORDER_NONE) || "0";
    const code = `example_move_player(x=${x}, y=${y}, z=${z})\n`;
    return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python["mcpi_build_wall"] = function(block) {
    const x = Blockly.Python.valueToCode(block, "x", Blockly.Python.ORDER_NONE) || "0";
    const y = Blockly.Python.valueToCode(block, "y", Blockly.Python.ORDER_NONE) || "64";
    const z = Blockly.Python.valueToCode(block, "z", Blockly.Python.ORDER_NONE) || "0";
    const width = Blockly.Python.valueToCode(block, "width", Blockly.Python.ORDER_NONE) || "5";
    const height = Blockly.Python.valueToCode(block, "height", Blockly.Python.ORDER_NONE) || "3";
    const code = `example_build_wall(x=${x}, y=${y}, z=${z}, width=${width}, height=${height})\n`;
    return [code, Blockly.Python.ORDER_NONE];
};
  