def improve(root, target):
    return 	((target / (root ** 2)) + (2 * root)) / 3
def abs(num):
    if num >= 0:
        return num
    else:
        return -num
def good_enough(value, target):
    if abs(value ** 3 - target) < 0.0001:
        return True
    else:
        return False
def square(n):
    root = 1
    while not good_enough(root, n):
        root = improve(root, n)
    return root

