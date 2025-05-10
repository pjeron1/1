result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    try:
        return a/b
    except ZeroDivisionError as e:
        print("Zero Division Error", e)

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
    for key in data:
        res = divider(key, data[key])
        result.append(res)
except (NameError, TypeError) as e:
    print("Error", e)

print(result)