import random
import os

if not os.path.exists("Ֆայլիկs"):
    os.makedirs("Ֆայլիկs")

if not os.path.exists("Sorted Ֆայլիկs"):
    os.makedirs("Sorted Ֆայլիկs")

max_fileik_size = 20000000  #Bytes
counter = 0
current_size = 0
a = 1
num_quantity = 10000000

with open("long_numbers.txt", 'w') as file:
    for i in range(1, num_quantity + 1):
        num = random.randint(0, 100000)
        file.write(str(num) + " ")

        with open(f"/Users/mikehakhverdyan/PycharmProjects/pythonProject/Ֆայլիկs/ֆայլիկ_{counter + 1}.txt", "a") as fileik:
            fileik.write(str(num) + " ")

            if i % 1000000 == 0:
                file.write("\n")

        if os.path.exists(f"/Users/mikehakhverdyan/PycharmProjects/pythonProject/Ֆայլիկs/ֆայլիկ_{counter + 1}.txt"):

            if os.path.getsize(f"/Users/mikehakhverdyan/PycharmProjects/pythonProject/Ֆայլիկs/ֆայլիկ_{counter + 1}.txt") > max_fileik_size or i == num_quantity:

                with open(f"/Users/mikehakhverdyan/PycharmProjects/pythonProject/Ֆայլիկs/ֆայլիկ_{counter + 1}.txt",
                          "r") as fileik:
                    s1 = ""
                    for el in fileik.readlines():
                        s1 += " " + el
                        s1 = s1.strip()
                    l1 = [int(x) for x in s1.split()]
                    l1.sort()

                    with open(f"/Users/mikehakhverdyan/PycharmProjects/pythonProject/Sorted Ֆայլիկs/Sorted_ֆայլիկ_{counter + 1}.txt", "a") as sorted_fileik:
                        for srtd_num in l1:
                            sorted_fileik.write(str(srtd_num) + "\n")

                    del(l1)
                counter += 1
main_lst = []
for i in range(1, counter + 1):
    exec(f"f{i} = open('/Users/mikehakhverdyan/PycharmProjects/pythonProject/Sorted Ֆայլիկs/Sorted_ֆայլիկ_{i}.txt', 'r')")
    main_lst.append(eval(f"int(f{i}.readline())"))

sorted_file = open("sorted.txt", 'a')
for i in range(num_quantity):

    if len(main_lst) == 0:
        sorted_file.write(next_num)
        break
    minnum = min(main_lst)
    minindx = main_lst.index(minnum)
    sorted_file.write(str(minnum) + '\n')
    next_num = eval(f"f{minindx + 1}.readline()")
    if next_num == '':
        main_lst.remove(minnum)
        continue
    main_lst[minindx] = int(next_num)
