from maps import NamedFrozenMapMeta
import unittest

class NamedFrozenMapTest(unittest.TestCase):
    def test_create(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        self.assertIsInstance(rgb, RGB)
        self.assertTrue(hasattr(rgb, 'red'))
        self.assertTrue(hasattr(rgb, 'green'))
        self.assertTrue(hasattr(rgb, 'blue'))

    def test_special_names(self):
        for special_name in ['type', 'self', 'collections', 'super']:
            TestClass = NamedFrozenMapMeta(special_name.title(), [special_name])
            test_obj = TestClass(1)
            self.assertEqual(test_obj[special_name], 1)

    def test_non_alphanumeric_names(self):
        with self.assertRaises(ValueError) as context:
            RGB = NamedFrozenMapMeta('RGB', ['r_e_d', 'gr33n', '&lue'])
        self.assertEqual(
            str(context.exception), (
                'Type names and field names can only contain alphanumeric'
                " characters and underscores: '&lue'"))

    def test_non_keyword_names(self):
        with self.assertRaises(ValueError) as context:
            RGB = NamedFrozenMapMeta('RGB', ['and', 'except', 'import'])
        self.assertEqual(
            str(context.exception),
            "Type names and field names cannot be a keyword: 'and'")

    def test_cannot_start_with_number(self):
        with self.assertRaises(ValueError) as context:
            RGB = NamedFrozenMapMeta('RGB', ['4ed', '6reen', '3lue'])
        self.assertEqual(
            str(context.exception),
            "Type names and field names cannot start with a number: '4ed'")

    def test_no_leading_underscore_fields(self):
        with self.assertRaises(ValueError) as context:
            RGB = NamedFrozenMapMeta('RGB', ['_red', '__green', '___blue'])
        self.assertEqual(
            str(context.exception),
            "Field names cannot start with an underscore: '_red'")

    def test_no_duplicate_fields(self):
        with self.assertRaises(ValueError) as context:
            RGB = NamedFrozenMapMeta('RGB', ['duck', 'duck', 'goose'])
        self.assertEqual(
            str(context.exception),
            "Encountered duplicate field name: 'duck'")

    def test_getitem(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        self.assertEqual(rgb['red'], 'rouge')

    def test_getattr(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        self.assertEqual(rgb.red, 'rouge')

    def test_getitem_KeyError(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        with self.assertRaises(KeyError) as context:
            rgb['grey']
        self.assertEqual(str(context.exception), "'grey'")

    def test_getattr_AttributeError(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        with self.assertRaises(AttributeError) as context:
            rgb.gray
        self.assertEqual(
            str(context.exception),
            "'RGB' object has no attribute 'gray'")

    def test_setitem_TypeError(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        with self.assertRaises(TypeError) as context:
            rgb['blue'] = 'topaz'
        self.assertEqual(
            str(context.exception),
            "'RGB' object does not support item assignment")
        with self.assertRaises(TypeError) as context:
            rgb['grey'] = 'pewter'
        self.assertEqual(
            str(context.exception),
            "'RGB' object does not support item assignment")

    def test_setattr_TypeError(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        with self.assertRaises(TypeError) as context:
            rgb.blue = 'topaz'
        self.assertEqual(
            str(context.exception),
            "'RGB' object does not support attribute assignment")
        with self.assertRaises(TypeError) as context:
            rgb.gray = 'pewter'
        self.assertEqual(
            str(context.exception),
            "'RGB' object does not support attribute assignment")

    def test_len(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        self.assertEqual(len(rgb), 3)

    def test_hash(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        self.assertIsInstance(hash(rgb), int)

    def test_iter(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        rgb = RGB(red='rouge', green='forest', blue='azul')
        self.assertEqual(frozenset(iter(rgb)), frozenset(['red', 'green', 'blue']))

    def test_class_fields(self):
        RGB = NamedFrozenMapMeta('RGB', ['red', 'green', 'blue'])
        self.assertEqual(RGB._fields, ('red', 'green', 'blue'))

    def test_defaults(self):
        RGB = NamedFrozenMapMeta(
            'RGB', ['red', 'green', 'blue'], defaults=dict(green=1, blue=2))
        rgb = RGB(red=100, green=7)
        self.assertEqual(rgb._data, dict(red=100, green=7, blue=2))

    def test_defaults_ordering(self):
        with self.assertRaises(ValueError) as context:
            RGB = NamedFrozenMapMeta(
                'RGB', ['red', 'green', 'blue'], defaults=dict(green=1))
        self.assertEqual(
            str(context.exception),
            "non-default argument 'blue' follows default argument 'green'")

    def test_defaults_correspond_to_fields(self):
        with self.assertRaises(ValueError) as context:
            RGB = NamedFrozenMapMeta(
                'RGB', ['red', 'green', 'blue'], defaults=dict(brown=1))
        self.assertEqual(
            str(context.exception),
            "Default argument does not correspond to any field: 'brown'")


if __name__ == '__main__':
    unittest.main()
