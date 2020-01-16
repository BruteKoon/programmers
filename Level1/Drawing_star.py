a, b = map(int, raw_input().strip().split(' '))
ss =""
for i in range(b):
    for j in range(a):
        ss = ss + "*"
    print ss
    ss = ""
