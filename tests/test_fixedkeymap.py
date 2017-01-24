from maps import FixedKeyMap
import unittest

class FixedKeyMapTest(unittest.TestCase):
    def test_create(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        self.assertIsInstance(rgb, FixedKeyMap)
        self.assertIn('red', rgb)
        self.assertIn('green', rgb)
        self.assertIn('blue', rgb)

    def test_getitem(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        self.assertEqual(rgb['red'], 'rouge')

    def test_getitem_KeyError(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        with self.assertRaises(KeyError) as context:
            rgb['grey']
        self.assertEqual(str(context.exception), "'grey'")

    def test_setitem(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        rgb['blue'] = 'topaz'
        self.assertEqual(rgb['blue'], 'topaz')

    def test_setitem_TypeError(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        with self.assertRaises(TypeError) as context:
            rgb['grey'] = 'pewter'
        self.assertEqual(
            str(context.exception),
            "'FixedKeyMap' object does not support new item assignment")

    def test_len(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        self.assertEqual(len(rgb), 3)

    def test_iter(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        self.assertEqual(frozenset(iter(rgb)), frozenset(['red', 'green', 'blue']))

    def test_del_TypeError(self):
        rgb = FixedKeyMap(red='rouge', green='forest', blue='azul')
        with self.assertRaises(TypeError) as context:
            del rgb['red']
        self.assertEqual(
            str(context.exception),
            "'FixedKeyMap' object does not support item deletion")

if __name__ == '__main__':
    unittest.main()
