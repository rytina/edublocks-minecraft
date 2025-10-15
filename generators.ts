import * as Blockly from "blockly";
import "blockly/python";

Blockly.Python["import_mcpi_structures"] = function () {
    return "from mcpi_structures import *\n";
};

Blockly.Python["mcpi_place_block"] = function (block: Blockly.Block) {
    const host =
        Blockly.Python.valueToCode(block, "host", Blockly.Python.ORDER_NONE) || '"127.0.0.1"';
    const port =
        Blockly.Python.valueToCode(block, "port", Blockly.Python.ORDER_NONE) || "4711";
    const code = `place_block(host=${host}, port=${port})`;
    return [code, Blockly.Python.ORDER_FUNCTION_CALL];
};

Blockly.Python["mcpi_move_player"] = function (block: Blockly.Block) {
    const x = Blockly.Python.valueToCode(block, "x", Blockly.Python.ORDER_NONE) || "0";
    const y = Blockly.Python.valueToCode(block, "y", Blockly.Python.ORDER_NONE) || "64";
    const z = Blockly.Python.valueToCode(block, "z", Blockly.Python.ORDER_NONE) || "0";
    const host =
        Blockly.Python.valueToCode(block, "host", Blockly.Python.ORDER_NONE) || '"127.0.0.1"';
    const port =
        Blockly.Python.valueToCode(block, "port", Blockly.Python.ORDER_NONE) || "4711";
    const code = `move_player(x=${x}, y=${y}, z=${z}, host=${host}, port=${port})`;
    return [code, Blockly.Python.ORDER_FUNCTION_CALL];
};

Blockly.Python["mcpi_build_wall"] = function (block: Blockly.Block) {
    const x = Blockly.Python.valueToCode(block, "x", Blockly.Python.ORDER_NONE) || "0";
    const y = Blockly.Python.valueToCode(block, "y", Blockly.Python.ORDER_NONE) || "64";
    const z = Blockly.Python.valueToCode(block, "z", Blockly.Python.ORDER_NONE) || "0";
    const width =
        Blockly.Python.valueToCode(block, "width", Blockly.Python.ORDER_NONE) || "5";
    const height =
        Blockly.Python.valueToCode(block, "height", Blockly.Python.ORDER_NONE) || "3";
    const host =
        Blockly.Python.valueToCode(block, "host", Blockly.Python.ORDER_NONE) || '"127.0.0.1"';
    const port =
        Blockly.Python.valueToCode(block, "port", Blockly.Python.ORDER_NONE) || "4711";
    const code = `build_walls(x=${x}, y=${y}, z=${z}, width=${width}, height=${height}, host=${host}, port=${port})`;
    return [code, Blockly.Python.ORDER_FUNCTION_CALL];
};
