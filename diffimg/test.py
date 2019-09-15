#!/usr/bin/env python

import os
import unittest

import PIL

from diff import diff

IMAGES_DIR = "images"


def mk_img_path(f):
    return os.path.join(IMAGES_DIR, f)


IMG1 = mk_img_path("mario-circle-cs.png")
IMG2 = mk_img_path("mario-circle-node.png")
IMG3 = mk_img_path("yandex1.png")  # RGBA
IMG4 = mk_img_path("yandex2.png")  # RGB
TEST_JPG_OUT = mk_img_path("test-diff.jpg")
TEST_PNG_OUT = mk_img_path("test-diff.png")
TEST_NO_EXT_OUT = mk_img_path("test-diff")
WHITE_IMG = mk_img_path("white.png")
BLACK_IMG = mk_img_path("black.png")


class TestAll(unittest.TestCase):
    def test_mario_ratio(self):
        ratio = diff(IMG1, IMG2, delete_diff_file=True)
        self.assertEqual(ratio, 0.007319618135968298)

    def test_bw_image_ratio(self):
        ratio = diff(BLACK_IMG, WHITE_IMG, delete_diff_file=True)
        self.assertEqual(ratio, 1.0)

    def test_delete_diff_img(self):
        if os.path.exists(TEST_JPG_OUT):
            os.remove(TEST_JPG_OUT)
        diff(IMG1, IMG2, delete_diff_file=True, diff_img_file=TEST_JPG_OUT)
        self.assertFalse(os.path.exists(TEST_JPG_OUT))

    def test_make_jpg_diff_img(self):
        diff(IMG1, IMG2, diff_img_file=TEST_JPG_OUT)
        self.assertTrue(os.path.exists(TEST_JPG_OUT))
        os.remove(TEST_JPG_OUT)

    def test_different_modes(self):
        with self.assertRaises(ValueError):
            diff(IMG3, IMG4)

    def test_make_png_diff_img(self):
        # these images are the same, but it shouldn't matter for this test
        diff(IMG4, IMG4, diff_img_file=TEST_PNG_OUT)
        self.assertTrue(os.path.exists(TEST_PNG_OUT))
        os.remove(TEST_PNG_OUT)

    def test_diff_filename_without_extension_saves_as_png(self):
        diff(IMG4, IMG4, diff_img_file=TEST_NO_EXT_OUT)
        im = PIL.Image.open(TEST_NO_EXT_OUT)
        self.assertEqual(im.format, "PNG")
        os.remove(TEST_NO_EXT_OUT)

    def test_ignore_alpha_mario(self):
        ratio = diff(IMG1, IMG2, delete_diff_file=True, ignore_alpha=True)
        self.assertEqual(ratio, 0.008675405566134298)

    def test_ignore_alpha_bw(self):
        ratio = diff(BLACK_IMG, WHITE_IMG, delete_diff_file=True, ignore_alpha=True)
        self.assertEqual(ratio, 1.0)

    def test_ignore_alpha_mario_file(self):
        diff(IMG1, IMG2, diff_img_file=TEST_PNG_OUT, ignore_alpha=True)
        im = PIL.Image.open(TEST_PNG_OUT)
        self.assertEqual(im.getextrema()[3], (255, 255))


if __name__ == "__main__":
    unittest.main()
