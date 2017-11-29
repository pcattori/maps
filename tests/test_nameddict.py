from maps import NamedDict
import unittest

class NamedDictTest(unittest.TestCase):

    def test_create(self):
        nd = NamedDict({'a': 1, 'b': 2})
        self.assertIsInstance(nd, NamedDict)
        self.assertTrue(hasattr(nd, 'a'))
        self.assertTrue(hasattr(nd, 'b'))

        nd = NamedDict(a=1, b=2)
        self.assertIsInstance(nd, NamedDict)
        self.assertTrue(hasattr(nd, 'a'))
        self.assertTrue(hasattr(nd, 'b'))

        nd = NamedDict([('a', 1), ('b', 2)])
        self.assertIsInstance(nd, NamedDict)
        self.assertTrue(hasattr(nd, 'a'))
        self.assertTrue(hasattr(nd, 'b'))

    def test_getattr(self):
        nd = NamedDict(a=1, b=2, c=3)
        self.assertEqual(nd['a'], 1)
        self.assertEqual(nd['b'], 2)
        self.assertEqual(nd['c'], 3)
        self.assertEqual(nd.a, 1)
        self.assertEqual(nd.b, 2)
        self.assertEqual(nd.c, 3)

    def test_setattr(self):
        nd = NamedDict(a=1, b=2, c=3)
        nd.a = 'a'
        self.assertEqual(nd.a, 'a')
        self.assertEqual(nd['a'], 'a')
        nd.d = 4
        self.assertEqual(nd.d, 4)
        self.assertEqual(nd['d'], 4)

    def test_recurse(self):
        obj = {
            "a": 1,
            "b": [
                2,
                {"c": 3}
            ]
        }
        nd = NamedDict.recurse(obj)
        self.assertEqual(nd, NamedDict(a=1, b=[2, NamedDict(c=3)]))

    def test_subclass_repr_no_infinite_recursion(self):
        class Subclass(NamedDict):
            pass

        sub = Subclass()
        self.assertEqual(repr(sub), 'Subclass({})')

if __name__ == '__main__':
    unittest.main()
