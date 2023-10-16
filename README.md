# Python Dictionaries Assignment

In this assignment, you will further practice using dictionaries in Python.

## Instructions

- Clone this repository to your local machine.
- Navigate to the `solutions` directory and open the `dicts.py` file.
- Complete the functions provided as per the specifications.
- Push your code to GitHub to see the results of the tests.

## Requirements

- Python 3.8+
- `pytest` for running tests locally

To install the dependencies:

```bash
pip install -r requirements.txt
```

To run the tests locally:

```bash
pytest
```

## Grading

Your assignment will be graded automatically every time you push. Check the GitHub Actions tab to see the results.

## Exercises

1. **Get Length and Type**
   - `get_length(my_dict)`: returns the length of the dictionary.
   - `get_type(my_dict)`: returns the type of the dictionary.
  
2. **Access Items**
   - `access_by_key(my_dict, key)`: returns the value for `key` using bracket notation.
   - `access_by_get(my_dict, key)`: returns the value for `key` using the `.get()` method.

3. **Change Items**
   - `update_value_directly(my_dict, key, value)`: updates the value for `key` using bracket notation.
   - `update_value_with_update(my_dict, key, value)`: updates the value for `key` using the `.update()` method.
   
4. **Add Items**
   - `add_item_directly(my_dict, key, value)`: adds a new key-value pair using bracket notation.
   - `add_item_with_update(my_dict, key, value)`: adds a new key-value pair using the `.update()` method.

5. **Remove Items**
   - `remove_item_by_pop(my_dict, key)`: removes the key-value pair with key `key` using the `.pop()` method.
   - `remove_item_by_del(my_dict, key)`: removes the key-value pair with key `key` using `del`.

6. **Looping through Dictionaries**
   - `get_keys(my_dict)`: returns all keys in the dictionary.
   - `get_values(my_dict)`: returns all values in the dictionary.
   - `get_items(my_dict)`: returns all key-value pairs in the dictionary.

7. **Copying Dictionaries**
   - `copy_with_copy_method(my_dict)`: returns a copy of the dictionary using the `.copy()` method.
   - `copy_with_dict_constructor(my_dict)`: returns a copy of the dictionary using the `dict()` constructor.

8. **Find Values**
   - `find_values(input_dict, keys)`: returns a list of values corresponding to the provided keys.

Your task is to implement these functions in `solutions/dicts.py` and ensure they pass all tests in `tests/test_dicts.py`.

Good luck and happy coding!
