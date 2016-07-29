#!/usr/bin/env python

# diff_images.py
# Nicolas Hahn
# return the % difference of two given images
# only works with images of the same type

from PIL import Image, ImageChops, ImageStat
import sys

diff_img_file = 'diff_img.jpg'

def diff(im1_file, im2_file):
    im1 = Image.open(im1_file)
    im2 = Image.open(im2_file)
    diff_img = ImageChops.difference(im1,im2)
    print 'Saving diff image as',diff_img_file
    diff_img.convert('RGB').save(diff_img_file)
    stat = ImageStat.Stat(diff_img)
    # can be [r,g,b] or [r,g,b,a]
    sum_channel_values = sum(stat.mean)
    max_all_channels = len(stat.mean) * 100
    diff_ratio = sum_channel_values/max_all_channels
    return diff_ratio

def main():
    try:
        diff_ratio = diff(sys.argv[1], sys.argv[2])
        print 'Images differ by '+str(diff_ratio*100)+'%'
    except Exception as e:
        return e
    return 0

if __name__ == "__main__":
    sys.exit(main())
