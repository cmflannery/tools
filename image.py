from __future__ import division, absolute_import, print_function
from PIL import Image
import argparse
import subprocess
import os


def parsey():
    parser = argparse.ArgumentParser(description='Scale and crop images')
    parser.add_argument('-file', dest='file', metavar='N', type=str, nargs=1,
                        help='Name of file to resize or crop')
    parser.add_argument('-batch', dest='batch', action='store_true',
                        help='-batch will be used to perform the same command on multiple images. Functionality tbd.')
    parser.add_argument('-scale', dest='scale', metavar='N', type=float, nargs=1,
                        help='Specifies operation to perform on image: -scale should be followed by scale value. 1 == unity')
    parser.add_argument('-crop', dest='crop', metavar='N', type=float, nargs=4,
                        help='Crop from [values] to [values], assumes centered e.g. -crop 1920 1080 1080 1080')
    args = parser.parse_args()
    return args


def openImage(filePath):
    img = Image.open(filePath)
    return img


def scale(img, scale):
    width, height = img.size
    size = width*scale, height*scale
    img.thumbnail(size, Image.ANTIALIAS)
    return img


def saveImage(img, fileName, dir=None):
    imageName = 'edited_' + fileName
    if dir:
        imagePath = os.path.join(dir,imageName)
    else:
        imagePath = imageName
    img.save(imagePath)


def splitfilePath(filePath):
    temp = filePath.split('/')
    fileName = temp[len(temp)-1]
    dirTemp = temp[:len(temp)-1]
    fileDir = ''.join(str(s)+'/' for s in dirTemp)
    return (fileName, fileDir)


def main():
    args = parsey()

    if not(args.batch):
        filePath = args.file[0]
        fileName, fileDir = splitfilePath(filePath)
        img = openImage(filePath)
        imgScaled = scale(img, args.scale[0])
        saveImage(imgScaled, fileName, dir=fileDir)
    print('Modified images saved in %s' % fileDir)
    print('Done!')


if __name__ == '__main__':
    try:
        subprocess.call('clear')
    except OSError:
        subprocess.call('cls', shell=True)

    try:
        main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt: Exiting...')
