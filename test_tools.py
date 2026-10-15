import math
import tempfile
import unittest
from pathlib import Path

from bed_overlap import overlaps, read_bed


class BedTests(unittest.TestCase):
    def test_half_open_and_pairwise(self):
        left = [('chr1',0,10,1),('chr2',0,10,2)]
        right = [('chr1',10,20,1),('chr1',5,15,2),('chr1',0,10,3)]
        self.assertEqual(list(overlaps(left,right)),[
            ('chr1',1,3,0,10,10),('chr1',1,2,5,10,5)])

    def test_invalid_interval(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'bad.bed'
            path.write_text('chr1\t3\t3\n',encoding='utf-8')
            with self.assertRaises(ValueError):
                read_bed(path)


if __name__ == '__main__':
    unittest.main()
