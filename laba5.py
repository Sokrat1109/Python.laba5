def task1():

    f = open("input.txt")
    s = f.readline()

    start = 0
    finish = 0
    buf = 1

    counter = 0

    while finish <= len(s) and counter <= 10:
        if finish == len(s):
            buf *= int(s[start:finish])
            counter += 1
            break
        if s[finish] == ' ':
            buf *= int(s[start:finish])
            start = finish + 1
            counter += 1
        finish += 1

    f1 = open("output.txt", "w")
    f1.write(str(buf))
    f1.close()
    f.close()

def task2():
    f = open("input2.txt")

    s = f.readlines()
    for i in range(len(s)):
        s[i] = int(s[i])

    s.sort()

    f1 = open("output2.txt", "w")
    for i in range(len(s)):
        f1.write(str(s[i]) + '\n')
    f1.close()
    f.close()

def task3():
    f = open("detsad.txt", errors="ignore", encoding='cp1251')
    s = f.readlines()

    min_ = 100
    max_ = 0

    for ss in s:
        start = ss.rfind(' ') + 1
        age = int(ss[start:])
        min_ = min(min_, age)
        max_ = max(max_, age)

    f1 = open("detout1.txt", "w", errors="ignore", encoding='cp1251')
    f2 = open("detout2.txt", "w", errors="ignore", encoding='cp1251')

    for ss in s:
        start = ss.rfind(' ') + 1
        age = int(ss[start:])
        if age == min_:
            f1.write(ss)
        elif age == max_:
            f2.write(ss)

task3()