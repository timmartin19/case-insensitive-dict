import pytest

from insensitive_dict import CaseInsensitiveDict


def assert_dicts_equal(expected, actual):
    assert len(expected) == len(actual)
    for key, value in expected.items():
        assert key in actual
        assert actual[key] == value


class TestInit:
    def test_init_empty__initializes_empty(self):
        resp = CaseInsensitiveDict()
        assert 0 == len(resp)
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
        assert 1 == d['x']

    def test_set_get_different_case(self):
        d = CaseInsensitiveDict()
        d['x'] = 1
        assert d['X'] == 1

    def test_set_get_original_case_preserved(self):
        d = CaseInsensitiveDict()
        d['X'] = 1
        d2 = {key: value for key, value in d.items()}
        assert 'X' in d2
        assert 'x' not in d2

    def test_del_same_case(self):
        d = CaseInsensitiveDict(x=1)
        del d['x']
        assert 'x' not in d

    def test_del_different_case(self):
        d = CaseInsensitiveDict(x=1)
        del d['X']
        assert 'x' not in d
        assert 'X' not in d

    def test_keys_same_case(self):
        d = CaseInsensitiveDict(x=1, Y=2)
        keys = list(d)
        assert 'x' in keys
        assert 'Y' in keys
        assert 'y' not in keys
        assert 'X' not in keys

    def test_len(self):
        d = CaseInsensitiveDict(x=1, y=2)
        assert 2 == len(d)

    def test_lower_items(self):
        d = CaseInsensitiveDict(x=1, Y=2)
        d2 = {key: value for key, value in d.lower_items()}
        assert {'x': 1, 'y': 2} == d2

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
        assert isinstance(repr(actual), str)

    def test_eq_non_dict(self):
        d = CaseInsensitiveDict()
        with pytest.raises(ValueError):
            d == 1
