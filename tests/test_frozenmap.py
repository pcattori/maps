from maps import FrozenMap
import unittest

class NamedFrozenMapTest(unittest.TestCase):
    def test_create(self):
        rgb = FrozenMap(red='rouge', green='forest', blue='azul')
        self.assertIsInstance(rgb, FrozenMap)
        self.assertIn('red', rgb)
        self.assertTrue('green', rgb)
        self.assertTrue('blue', rgb)

    def test_getitem(self):
        rgb = FrozenMap(red='rouge', green='forest', blue='azul')
        self.assertEqual(rgb['red'], 'rouge')

    def test_getitem_KeyError(self):
        rgb = FrozenMap(red='rouge', green='forest', blue='azul')
        with self.assertRaises(KeyError) as context:
            rgb['grey']
        self.assertEqual(str(context.exception), "'grey'")

    def test_setitem_TypeError(self):
        rgb = FrozenMap(red='rouge', green='forest', blue='azul')
        with self.assertRaises(TypeError) as context:
            rgb['blue'] = 'topaz'
        self.assertEqual(
            str(context.exception),
            "'FrozenMap' object does not support item assignment")
        with self.assertRaises(TypeError) as context:
            rgb['grey'] = 'pewter'
        self.assertEqual(
            str(context.exception),
            "'FrozenMap' object does not support item assignment")

    def test_len(self):
        rgb = FrozenMap(red='rouge', green='forest', blue='azul')
        self.assertEqual(len(rgb), 3)

    def test_hash(self):
        rgb = FrozenMap(red='rouge', green='forest', blue='azul')
        self.assertIsInstance(hash(rgb), int)

    def test_iter(self):
        rgb = FrozenMap(red='rouge', green='forest', blue='azul')
        self.assertEqual(frozenset(iter(rgb)), frozenset(['red', 'green', 'blue']))

    def test_recurse(self):
        obj = {
            "a": 1,
            "b": [
                2,
                {
                    "c": 3
                }
            ]
        }
        fm = FrozenMap.recurse(obj)
        self.assertEqual(fm, FrozenMap(a=1, b=(2, FrozenMap(c=3))))

if __name__ == '__main__':
    unittest.main()
