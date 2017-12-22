#!/usr/bin/env python

# return the % difference of two given images
# only works with images of the same file type

from PIL import Image, ImageChops, ImageStat
from os import remove
import argparse
import sys

diff_img_file = 'diff_img.jpg'

def diff(im1_file, 
         im2_file, 
         delete_diff_file=False, 
         diff_img_file=diff_img_file):
    im1 = Image.open(im1_file)
    im2 = Image.open(im2_file)
    diff_img = ImageChops.difference(im1,im2)
    diff_img.convert('RGB').save(diff_img_file)
    stat = ImageStat.Stat(diff_img)
    # can be [r,g,b] or [r,g,b,a]
    sum_channel_values = sum(stat.mean)
    max_all_channels = len(stat.mean) * 100
    diff_ratio = sum_channel_values/max_all_channels
    if delete_diff_file:
        remove(diff_img_file)
    return diff_ratio

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
            default=diff_img_file,
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
