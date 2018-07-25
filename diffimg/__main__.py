from __future__ import print_function
import argparse
import sys
from __init__ import diff, DIFF_IMG_FILE


def get_args():
    parser = argparse.ArgumentParser(
            description='Generate a diff image from two images \
            and/or find difference percentage')
    parser.add_argument('image1',
            type=str,
            help='first image')
    parser.add_argument('image2',
            type=str,
            help='second image')
    parser.add_argument('--ratio', '-r',
            dest='use_ratio',
            action='store_true',
            help='return a ratio instead of percentage')
    parser.add_argument('--delete', '-d',
            dest='delete_diff_file',
            action='store_true',
            help='delete diff image file')
    parser.add_argument('--filename', '-f',
            dest='diff_img_file',
            type=str,
            default=DIFF_IMG_FILE,
            help='filename with valid extension to store diff image \
                (defaults to diff_img.jpg)')
    return parser.parse_args()

def main():
    args = get_args()
    diff_ratio = diff(args.image1,
                      args.image2,
                      args.delete_diff_file,
                      args.diff_img_file)
    if args.use_ratio:
        print(diff_ratio)
    else:
        print('Images differ by {}%'.format(diff_ratio*100))
    return 0

if __name__ == "__main__":
    sys.exit(main())
