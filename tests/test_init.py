import maps
import unittest

class TestInit(unittest.TestCase):
    def test_namedmap(self):
        RGB = maps.namedmap('RGB', ['red', 'green', 'blue'])
        self.assertEqual(type(RGB), maps.NamedFrozenMapMeta)
        CMYK = maps.namedmap('CMYK', ['cyan', 'magenta', 'yellow', 'black'], fixed_keys=True)
        self.assertEqual(type(CMYK), maps.NamedFixedKeyMapMeta)

if __name__ == '__main__':
    unittest.main()

