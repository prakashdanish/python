from handshake import handshake, code

import os
import unittest

class HandshakeTest(unittest.TestCase):
    def test_shake_int(self):
        self.assertEqual(['wink','jump'], handshake(9))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_shake_bin1(self):
        self.assertEqual(['close your eyes','double blink'], handshake('10110'))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_shake_bin2(self):
        self.assertEqual(['wink','close your eyes'], handshake('101'))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_shake_negative_int(self):
        self.assertEqual([], handshake(-9))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_shake_bin_invalid(self):
        self.assertEqual([], handshake('121'))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_unknown_action(self):
        self.assertEqual('0', code(['wink','sneeze']))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_code1(self):
        self.assertEqual('1100', code(['close your eyes','jump']))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_code2(self):
        self.assertEqual('11', code(['wink','double blink']))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_code3(self):
        self.assertEqual('11010', code(['jump','double blink']))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_composition1(self):
        self.assertEqual('11011', code(handshake(27)))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_composition2(self):
        self.assertEqual('1', code(handshake(1)))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_composition3(self):
        self.assertEqual('111', code(handshake('111')))

    @unittest.skipUnless('NO_SKIP' in os.environ, "Not implemented yet")
    def test_composition4(self):
        inp = ['wink','double blink','jump']
        self.assertEqual(inp, handshake(code(inp)))


if __name__ == '__main__':
    unittest.main()
