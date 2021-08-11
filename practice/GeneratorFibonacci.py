def gen(n):
    first = 0
    second = 1
    for i in range(n-1):
        third = first + second
        first,second = second,third
        yield third
        
g = gen(10)
for i in g:
    print(i)