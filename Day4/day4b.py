file = open("./input", "r")
mininput, maxinput = [int(i) for i in file.read().split('-')]
file.close()

count = 0
for i in range(int(mininput), int(maxinput)):
    stri = str(i)
    a = stri[0]
    b = stri[1]
    c = stri[2]
    d = stri[3]
    e = stri[4]
    f = stri[5]

    if(a <= b and b <= c and c <= d  and d <= e and e <= f):
        if((a == b and b != c) or (a != b and b == c and d != c) or (b != c and c == d and d != e) or (c != d and d == e and e != f) or (d != e and e == f)):
            count += 1
            print(i)

print(count)