from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import unittest2

from insensitive_dict import CaseInsensitiveDict


def assert_dicts_equal(expected, actual):
    assert len(expected) == len(actual)
    for key, value in expected.items():
        assert key in actual
        assert actual[key] == value


class TestInit(unittest2.TestCase):
    def test_init_empty__initializes_empty(self):
        resp = CaseInsensitiveDict()
        self.assertEqual(0, len(resp))
        assert_dicts_equal({}, resp)

    def test_init_from_dict(self):
        original = dict(x=1, y=2)
        resp = CaseInsensitiveDict(original)
        assert_dicts_equal(original, resp)

    def test_init_from_kwargs(self):
        original = dict(x=1, y=2)
        resp = CaseInsensitiveDict(**original)
        assert_dicts_equal(original, resp)

    def test_set_get_same_case(self):
        d = CaseInsensitiveDict()
        d['x'] = 1
        self.assertEqual(1, d['x'])

    def test_set_get_different_case(self):
        d = CaseInsensitiveDict()
        d['x'] = 1
        self.assertEqual(1, d['X'])

    def test_set_get_original_case_preserved(self):
        d = CaseInsensitiveDict()
        d['X'] = 1
        d2 = {key: value for key, value in d.items()}
        self.assertIn('X', d2)
        self.assertNotIn('x', d2)

    def test_del_same_case(self):
        d = CaseInsensitiveDict(x=1)
        del d['x']
        self.assertNotIn('x', d)

    def test_del_different_case(self):
        d = CaseInsensitiveDict(x=1)
        del d['X']
        self.assertNotIn('x', d)
        self.assertNotIn('X', d)

    def test_keys_same_case(self):
        d = CaseInsensitiveDict(x=1, Y=2)
        keys = list(d)
        self.assertIn('x', keys)
        self.assertIn('Y', keys)
        self.assertNotIn('y', keys)
        self.assertNotIn('X', keys)

    def test_len(self):
        d = CaseInsensitiveDict(x=1, y=2)
        self.assertEqual(2, len(d))

    def test_lower_items(self):
        d = CaseInsensitiveDict(x=1, Y=2)
        d2 = {key: value for key, value in d.lower_items()}
        self.assertDictEqual({'x': 1, 'y': 2}, d2)

    def test_equal(self):
        d1 = CaseInsensitiveDict(x=1)
        d2 = CaseInsensitiveDict(x=1)
        assert d1 == d2
        d2['x'] = 2
        assert d1 != d2

    def test_copy(self):
        d1 = CaseInsensitiveDict(x=1)
        d2 = d1.copy()
        assert d1 is not d2
        assert d1 == d2

    def test_repr(self):
        original = dict(x=1, y=2)
        actual = CaseInsensitiveDict(data=original)
        self.assertIsInstance(repr(actual), str)

    def test_eq_non_dict(self):
        d = CaseInsensitiveDict()
        self.assertRaises(ValueError, d.__eq__, 1)
