/// <reference types="node" />
export declare type EmojiOptions = {
    width?: number;
    height?: number;
    color?: string;
    backgroundColor?: string;
    textAlign?: typeof aligns[number];
    textSizeFixed?: boolean;
    disableStretch?: boolean;
    typefaceFile?: string;
    typefaceName?: string;
    format?: typeof formats[number];
    quality?: number;
};
declare type Returns = {
    buffer: Buffer;
};
declare const aligns: readonly ["left", "center", "right"];
declare const formats: readonly ["png", "webp"];
export declare const generate: (text: string, { width, height, color, backgroundColor, textAlign, textSizeFixed, disableStretch, typefaceFile, typefaceName, format, quality }?: EmojiOptions) => Returns;
export {};
