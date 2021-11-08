import unittest
from service.biggest import biggest

class AddTest(unittest.TestCase):
    def testbig1(self):
        self.assertEqual(biggest(0, 0, 0), 0)

    def testbig2(self):
        self.assertEqual(biggest(-1, 1,4), 4)

    def testbig3(self):
        self.assertEqual(biggest(-1, -3, -7), -1)

    def testbig4(self):
        self.assertEqual(biggest(2, 3, "8"), None)
