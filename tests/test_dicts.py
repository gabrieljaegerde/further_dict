import pytest
from solutions.dicts import *

# Tests for get_length and get_type
def test_get_length():
    assert get_length({'a': 1, 'b': 2}) == 2

def test_get_type():
    assert get_type({'a': 1, 'b': 2}) == dict

# Tests for access_by_key and access_by_get
def test_access_by_key():
    assert access_by_key({'a': 1, 'b': 2}, 'a') == 1
    
def test_access_by_get():
    assert access_by_get({'a': 1, 'b': 2}, 'b') == 2
    
# Tests for update_value_directly and update_value_with_update
def test_update_value_directly():
    assert update_value_directly({'a': 1, 'b': 2}, 'a', 3) == {'a': 3, 'b': 2}
    
def test_update_value_with_update():
    assert update_value_with_update({'a': 1, 'b': 2}, 'b', 3) == {'a': 1, 'b': 3}
    
# Tests for add_item_directly and add_item_with_update
def test_add_item_directly():
    assert add_item_directly({'a': 1}, 'b', 2) == {'a': 1, 'b': 2}

def test_add_item_with_update():
    assert add_item_with_update({'a': 1}, 'b', 2) == {'a': 1, 'b': 2}

# Tests for remove_item_by_pop and remove_item_by_del
def test_remove_item_by_pop():
    assert remove_item_by_pop({'a': 1, 'b': 2}, 'a') == {'b': 2}
    
def test_remove_item_by_del():
    assert remove_item_by_del({'a': 1, 'b': 2}, 'b') == {'a': 1}

# Tests for get_keys, get_values, and get_items
def test_get_keys():
    assert set(get_keys({'a': 1, 'b': 2, 'c': 3})) == {'a', 'b', 'c'}

def test_get_values():
    assert set(get_values({'a': 1, 'b': 2, 'c': 3})) == {1, 2, 3}

def test_get_items():
    assert set(get_items({'a': 1, 'b': 2})) == {('a', 1), ('b', 2)}

# Tests for copy_with_copy_method and copy_with_dict_constructor
def test_copy_with_copy_method():
    assert copy_with_copy_method({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

def test_copy_with_dict_constructor():
    assert copy_with_dict_constructor({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

# Tests for find_values
def test_find_values():
    assert find_values({'a': 1, 'b': 2, 'c': 3}, ['a', 'b', 'x']) == [1, 2, None]
    assert find_values({'name': 'Alice', 'age': 30}, ['name', 'height']) == ['Alice', None]
    assert find_values({}, ['a', 'b', 'c']) == [None, None, None]
    assert find_values({'x': 10, 'y': 20, 'z': 30}, ['x', 'y', 'z']) == [10, 20, 30]


