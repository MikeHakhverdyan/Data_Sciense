import random

l1 = [0 for i in range(121)]

with open("numbers.txt", 'w') as file:
    for i in range(1, 1000000001):
        file.write(str(random.randint(0, 120)) + " ")
        if i % 100000 == 0:
            file.write("\n")
        i += 1

line = 1
with open("numbers.txt", "r") as file:
    while line:
        line = file.readline()
        l2 = line.split()
        for num in l2:
            l1[int(num)] += 1

a = 0

with open("sorted_numbers.txt", 'w') as file:
    for i in range(len(l1)):
        if l1[i] != 0:
            while l1[i] > 0:
                file.write(str(i) + " ")
                a += 1
                l1[i] -= 1
                if a % 100000 == 0:
                    file.write("\n")
