#!/usr/bin/env python

# return the % difference of two given images
# only works with images of the same file type

from PIL import Image, ImageChops, ImageStat

DIFF_IMG_FILE = 'diff_img.jpg'

def diff(im1_file, 
         im2_file, 
         delete_diff_file=False, 
         diff_img_file=DIFF_IMG_FILE):
    '''Calculate the difference between two images of the same size
    by comparing channel values at the pixel level. 

    `delete_diff_file`: removes the diff image after ratio found
    `diff_img_file`: filename to store diff image
    '''

    # Generate diff image in memory.
    im1 = Image.open(im1_file)
    im2 = Image.open(im2_file)
    diff_img = ImageChops.difference(im1,im2)

    if not delete_diff_file:
        diff_img.convert('RGB').save(diff_img_file)

    # Calculate difference as a ratio.
    stat = ImageStat.Stat(diff_img)
    # Can be [r,g,b] or [r,g,b,a].
    sum_channel_values = sum(stat.mean)
    max_all_channels = len(stat.mean) * 100
    diff_ratio = sum_channel_values/max_all_channels

    return diff_ratio
