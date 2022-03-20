import sys
inFile = sys.argv[1]
#outFile = sys.argv[2]
a1 = ["տըպա"]
b1 = ["print"]

a2 = ["ուրուշ"]
b2 = ["else"]

a3 = ["վերագրա", "հավսար_ա"]
b3 = ["=",        "=="]

a4 = ["եթե", "ուրուշ_եթե"]
b4 = ["if",  "elif"]

a5 = ["ճիշտ_ա", "ճշտի_հակառակն_ա"]
b5 = ["True",    "False"]

signs1 = ["+", "-", "*", "/", "%", "<", ">", "<=", ">="]
variables = {}
with open(inFile) as file:

    for line in file:
        if "==" not in line:
            line = line.replace("=", " = ")
        line = line.replace("==", " == ")
        for sign in signs1:
            line = line.replace(sign, " " + sign + " ")
        l1 = line.split()


        def boolish():
            for bo in a5:
                if bo in l1:
                    bo = b5[a5.index(bo)]
                    return bo
        def removing():
            if l1[-1] == ";":
                l1.pop()
            elif ";" in l1[-1]:
                l1[-1] = l1[-1].rstrip(";")
                l1[-1] = l1[-1].strip()



        '''for sign in signs1:
          for index in range(len(l1)):
                if index < len(l1) - 1:
                    if sign in l1[index]:
                        if l1[index - 1] in a1:
                            l1[index] = l1[index] + l1[index + 1]
                            l1.pop(index + 1)
                        elif l1[index + 1] in a1:
                            l1[index] = l1[index - 1] + l1[index]
                            l1.pop(index)
                        else:
                            l1[index] = l1[index - 1] + l1[index]
                            l1.pop(index - 1)'''
        for token in l1:
            for equals in a3:
                if equals in l1:
                    l1[l1.index(equals)] = b3[a3.index(equals)]
            if token in a3 + b3:
                b00 = False
                for Bool in a5:
                    for equal in a3 + b3:
                        if b00:
                            break
                        if Bool in l1:
                            Bool = b5[a5.index(Bool)]
                            if len(l1) == 3:
                                variables[f"{l1[0]}"] = Bool
                                exec(f"{l1[0]} {b3[a3.index(token)]} {variables[f'{l1[0]}']}")
                                if f"'տըպա' + ' ' + {str(Bool)}" in line:
                                    print(Bool)
                                b00 = True
                                break
                        if equal in l1:
                            for ind in range(len(l1) - 3):
                                l1[l1.index(equal) + 1] = l1[l1.index(equal) + 1] + " " + l1[l1.index(equal) + 2]
                                l1.pop(l1.index(equal) + 2)
                            variables[f"{l1[0]}"] = l1[-1]
                            exec(f"{l1[0]} {token} {variables[f'{l1[0]}']}")
            elif token in a1:
                if len(l1) == 3:
                    l1[1] = l1[1] + " " + l1[2]
                    if len(l1) == 3:
                        l1.pop()
                elif len(l1) > 3:
                    i = 2
                    while i <= len(l1) - 1:
                        # if not l1[i] in signs1:
                        #     i += 1
                        #     continue
                        if l1[i] in signs1:
                            l1[i] = l1[i - 1] + l1[i] + l1[i + 1]
                            l1.pop(i - 1)
                            l1.pop(i)
                        else:
                            l1[i] = l1[i - 1] + " " + l1[i]
                            l1.pop(i - 1)
                removing()
                for booli in a5:
                    if booli in l1:
                        l1[l1.index(booli)] = boolish()

                eval(f"{b1[a1.index(token)]}")(eval(f"{l1[l1.index(token) + 1]}"))

            elif token in a4:
                for equals in a3:
                    if equals in l1:
                        l1[l1.index(equals)] = b3[a3.index(equals)]
                if len(line) > 2:
                    i = 2
                    while i <= len(l1) - 1:
                        if l1[i] in signs1 or l1[i] == "==":
                            l1[i] = l1[i - 1] + l1[i] + l1[i + 1]
                            l1.pop(i - 1)
                            l1.pop(i)
                        else:
                            l1[i] = l1[i - 1] + " " + l1[i]
                            l1.pop(i - 1)
                for bo in a5:
                    if bo in l1:
                        l1[-1] = boolish()
                b00l = eval(f"{l1[l1.index(token) + 1]}")
                if not b00l:
                    while line.strip()[-1] != ";":
                        line = file.readline()