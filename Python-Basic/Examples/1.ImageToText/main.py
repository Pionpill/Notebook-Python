# -*- coding: utf-8 -*-
from PIL import Image   # 第三方图形库：pillow
import argparse


class ImageToText:

    ASCII_CHAR = list(
        "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    def __init__(self, file, size=(100, 40), output='output.txt') -> None:
        '''接受图像信息
        :param file: str 图像位置，必须是 jpg,png 等图像格式
        :param size: tuple 输出文本大小
        :param output: str 输出文件文字, 必须是 txt 文件
        '''
        self.file = file
        self.size = size
        self.output = output

    def imageProcess(self) -> Image:
        '''图像处理为文本
        :return Image: 重置大小后的图像
        '''
        image = Image.open(self.file)
        image = image.resize(self.size, Image.NEAREST)
        return image

    def get_char(self, rgb, alpha=256) -> str:
        '''灰度映射函数：将像素块映射到函数上
        :param rgb: tuple 三原色通道
        :param alpha: int 不透明度
        :return char: 像素块对应字符
        '''
        if alpha == 0:
            return ' '
        length = len(self.ASCII_CHAR)
        gray = int(0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2])

        return self.ASCII_CHAR[(int)(gray/256*length)]

    def toText(self) -> list:
        '''转换为文本
        :return text: 转换后的文本
        '''
        image = self.imageProcess()
        text = ""
        WIDTH = self.size[0]
        HEIGHT = self.size[1]
        for x in range(HEIGHT):
            for y in range(WIDTH):
                text += self.get_char(image.getpixel((y, x)))
            text += '\n'
        return text


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')  # 输入文件
    parser.add_argument('-o', '--output')  # 输出文件
    parser.add_argument('--width', type=int, default=100)  # 输出字符画宽
    parser.add_argument('--height', type=int, default=40)  # 输出字符画高
    args = parser.parse_args()

    example = ImageToText(args.file, (args.width, args.height), args.output)
    txt = example.toText()

    del example
    print(txt)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
