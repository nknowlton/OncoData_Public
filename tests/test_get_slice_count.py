from os.path import dirname, realpath, join
import sys
sys.path.append(dirname(dirname(realpath(__file__))))
import unittest

from oncodata.dicom_to_png.get_slice_count import get_slice_count

test_dir = dirname(realpath(__file__))

class SliceCountTests(unittest.TestCase):
    def test_slice_count(self):
        correct_slice_count = 1
        slice_count = get_slice_count(join(test_dir, 'test_data', 'test.dcm'))

        self.assertEqual(correct_slice_count, slice_count)

if __name__ == '__main__':
    unittest.main()
