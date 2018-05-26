import unittest
from diffimg import diff

class TestDiffImg(unittest.TestCase):

    def test_mario_images(self):
        img1 = 'mario-circle-cs.png'
        img2 = 'mario-circle-node.png'
        diff_img_file = 'test-diff.jpg'
        ratio = diff(
                img1, img2,
                delete_diff_file=True,
                diff_img_file=diff_img_file)
        self.assertEqual(ratio, 0.01866502624671916)

if __name__ == '__main__':
    unittest.main()
