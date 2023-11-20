def upc(number):
    n = str(number)
    odd = sum([int (n[i]) for i in range(11) if i % 2 == 0 ])
    x = odd * 3
    print(odd)
    even = sum([int(n[i]) for i in range(11) if i % 2 !=0 ])
    print(even)
    y = x + even
    m = y % 10
    if m == 0:
        print(0)
    else:
        e = 10 - m    
        print(e)