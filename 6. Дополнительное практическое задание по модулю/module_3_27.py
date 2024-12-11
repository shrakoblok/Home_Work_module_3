def calculate_structure_sum(values):
    q = 0
    if isinstance(values, int) or isinstance(values, float):
        return values
    elif isinstance(values, str):
        return len(values)
    elif isinstance(values, list):
        for element in values:
            q += calculate_structure_sum(element)
        return q
    elif isinstance(values, tuple):
        for element in values:
            q += calculate_structure_sum(element)
        return q
    elif isinstance(values, set):
        for element in values:
            q += calculate_structure_sum(element)
        return q
    elif isinstance(values, dict):
        for key in values.items():
            q += calculate_structure_sum(key)
        return q
    else:
        return 0

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)