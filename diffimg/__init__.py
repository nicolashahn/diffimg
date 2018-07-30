#!/usr/bin/env python

"""
Return the % difference of two given images.
Only works with images of the same file type and color channels.
"""

from __future__ import print_function
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

    im1 = Image.open(im1_file)
    im2 = Image.open(im2_file)

    # Ensure we have the same color channels (RGBA vs RGB)
    if im1.mode != im2.mode:
        raise ValueError(("Differing color modes:\n  {}: {}\n  {}: {}\n"
                          "Ensure image color modes are the same."
                          ).format(im1_file, im1.mode, im2_file, im2.mode))

    # Generate diff image in memory.
    diff_img = ImageChops.difference(im1, im2)

    if not delete_diff_file:
        extension = diff_img_file.split('.')[-1]
        if extension in ('jpg', 'jpeg'):
            # For some reason, save() thinks "jpg" is invalid
            # This doesn't affect the image's saved filename
            extension = 'jpeg'
            diff_img = diff_img.convert('RGB')
        diff_img.save(diff_img_file, extension)

    # Calculate difference as a ratio.
    stat = ImageStat.Stat(diff_img)
    # Can be [r,g,b] or [r,g,b,a].
    sum_channel_values = sum(stat.mean)
    max_all_channels = len(stat.mean) * 100
    diff_ratio = sum_channel_values/max_all_channels

    return diff_ratio
