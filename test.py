import unittest
from diffimg import diff
import os

class TestDiffImg(unittest.TestCase):

    def test_mario_images(self):

        images_dir = 'images'
        img_path = lambda f: os.path.join(images_dir, f)

        img1 = img_path('mario-circle-cs.png')
        img2 = img_path('mario-circle-node.png')
        diff_img_file = img_path('test-diff.jpg')

        ratio = diff(
                img1, img2,
                delete_diff_file=True,
                diff_img_file=diff_img_file)

        self.assertEqual(ratio, 0.01866502624671916)

if __name__ == '__main__':
    unittest.main()
