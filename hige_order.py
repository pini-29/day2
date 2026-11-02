#1
def apply_to_all(numbers, action):
    result = []
    for i in numbers:
        result.append(action(i))
    return result
def double(number):
    return number*2
print(apply_to_all([10,15,20],double))
print(apply_to_all([2,3,5],lambda n: n*n))
print(apply_to_all([12,1.5,13.5],round))
