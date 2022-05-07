def p0w(a, b):
    counter = 1
    answer = a
    if b == 0:
        return 1
    elif b < 0:
        while counter < -b:
            answer *= a
            counter += 1
        return answer
    else:
        while counter < b:
            answer *= a
            counter += 1
        return answer
