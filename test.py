import os
import unittest
from diffimg import diff


IMAGES_DIR = 'images'
IMG_PATH = lambda f: os.path.join(IMAGES_DIR, f)

IMG1 = IMG_PATH('mario-circle-cs.png')
IMG2 = IMG_PATH('mario-circle-node.png')
TEST_FILE = IMG_PATH('test-diff.jpg')


class TestAll(unittest.TestCase):

    def test_ratio(self):
        ratio = diff(IMG1,
                     IMG2,
                     delete_diff_file=True)
        self.assertEqual(ratio, 0.01866502624671916)

    def test_delete_diff_img(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        diff(IMG1,
             IMG2,
             delete_diff_file=True,
             diff_img_file=TEST_FILE)
        self.assertFalse(os.path.exists(TEST_FILE))

    def test_make_diff_img(self):
        diff(IMG1,
             IMG2,
             diff_img_file=TEST_FILE)
        self.assertTrue(os.path.exists(TEST_FILE))
        os.remove(TEST_FILE)


if __name__ == '__main__':
    unittest.main()
