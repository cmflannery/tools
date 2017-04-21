from PIL import Image
import argparse
import subprocess
# from future import print_function


def parsey():
    parser = argparse.ArgumentParser(description='Scale and crop images')
    parser.add_argument('-file', dest='file', metavar='N', type=str, nargs=1,
                        help='Name of file to resize or crop')
    parser.add_argument('-batch', dest='batch', action='store_true',
                        help='-batch will be used to perform the same command on multiple images. Functionality tbd.')
    parser.add_argument('-scale', dest='scale', metavar='N', type=float, nargs=1,
                        help='Specifies operation to perform on image: -scale should be followed by scale value. 1 == unity')
    args = parser.parse_args()
    return args


def openImage(fileName):
    img = Image.open(fileName)
    return img


def scale(img, scale):
    width, height = img.size
    size = width*scale, height*scale
    img.thumbnail(size, Image.ANTIALIAS)
    return img


def saveImage(img, fileName):
    newName = 'CROPPED_' + fileName
    img.save(newName)


def main():
    args = parsey()

    if not(args.batch):
        fileName = args.file[0]
        print(fileName)
        img = openImage(fileName)
        imgScaled = scale(img, args.scale[0])
        saveImage(imgScaled, fileName)

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
