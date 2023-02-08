"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.generate = void 0;
const bindings_1 = __importDefault(require("bindings"));
const native = (0, bindings_1.default)({
    bindings: 'emoji'
});
const aligns = ['left', 'center', 'right'];
const formats = ['png', 'webp'];
const colorCodeToNum = (code) => {
    const str = code[0] === '#' ? code.slice(1) : code;
    const hex = parseInt(str, 16);
    if (str.length !== 8) {
        throw new Error('color code must be 8 digits, including alpha (eg. #000000FF)');
    }
    const red = (hex >> 24) & 0xff;
    const green = (hex >> 16) & 0xff;
    const blue = (hex >> 8) & 0xff;
    const alpha = hex & 0xff;
    return (alpha << 24) | (red << 16) | (green << 8) | blue;
};
const generate = (text, { width = 128, height = 128, color = '#000000FF', backgroundColor = '#00000000', textAlign = 'center', textSizeFixed = false, disableStretch = false, typefaceFile = '', typefaceName = '', format = 'png', quality = 100 } = {}) => {
    if (typeof text !== 'string' || !text) {
        throw new Error('text must be a string');
    }
    if (typeof width !== 'number' || width <= 0) {
        throw new Error('width must be a positive number');
    }
    if (typeof height !== 'number' || height <= 0) {
        throw new Error('height must be a positive number');
    }
    const colorNum = colorCodeToNum(color);
    const backgroundColorNum = colorCodeToNum(backgroundColor);
    if (typeof textAlign !== 'string' || !aligns.includes(textAlign)) {
        throw new Error(`align must be one of the following: ${aligns.join(', ')}`);
    }
    if (typeof textSizeFixed !== 'boolean') {
        throw new Error('textSizeFixed must be a boolean');
    }
    if (typeof disableStretch !== 'boolean') {
        throw new Error('disableStretch must be a boolean');
    }
    if (typeof typefaceFile !== 'string') {
        throw new Error('typefaceFile must be a string');
    }
    if (typeof typefaceName !== 'string') {
        throw new Error('typefaceName must be a string');
    }
    if (typeof format !== 'string' || !formats.includes(format)) {
        throw new Error(`format must be one of the following: ${formats.join(', ')}`);
    }
    if (typeof quality !== 'number' || quality < 0 || quality > 100) {
        throw new Error('quality must be a number between 0 and 100');
    }
    return native.generate(text, {
        width,
        height,
        color: colorNum,
        backgroundColor: backgroundColorNum,
        textAlign,
        textSizeFixed,
        disableStretch,
        typefaceFile,
        typefaceName,
        format,
        quality
    });
};
exports.generate = generate;
