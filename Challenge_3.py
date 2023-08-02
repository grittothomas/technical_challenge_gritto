def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    current_obj = obj
    for k in keys:
        if k in current_obj:
            current_obj = current_obj[k]
        else:
            return None
    return current_obj

object1 = {"a": {"b": {"c": "d"}}}
key1 = "a/b/c"
print(get_value_from_nested_object(object1, key1))  # Output: d

object2 = {"x": {"y": {"z": "a"}}}
key2 = "x/y/z"
print(get_value_from_nested_object(object2, key2))  # Output: a

key3 = "x/y/w"
print(get_value_from_nested_object(object2, key3))  # Output: None
