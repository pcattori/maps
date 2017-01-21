import maps
import unittest

class TestInit(unittest.TestCase):
    def test_namedfrozen(self):
        RGB = maps.namedfrozen('RGB', ['red', 'green', 'blue'])
        self.assertEqual(type(RGB), maps.NamedFrozenMapMeta)

    def test_namedfixedkey(self):
        CMYK = maps.namedfixedkey('CMYK', ['cyan', 'magenta', 'yellow', 'black'])
        self.assertEqual(type(CMYK), maps.NamedFixedKeyMapMeta)

if __name__ == '__main__':
    unittest.main()

