#!/usr/bin/env python

# return the % difference of two given images
# only works with images of the same file type

from PIL import Image, ImageChops, ImageStat
from os import remove

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
