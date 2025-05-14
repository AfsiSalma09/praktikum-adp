# Menginput banyak data
while True :
    n = int(input('Input banyak data n : '))
    data = []
    for i in range (1, n+1) :
        x = int(input(f'input x ke-{i} : '))
        def f(x) :
            if x>=0 :
                return 4*x**3 + 7*x - 5
            else :
                return 3*x**2 - 5*x + 1
        fx = f(x)
        gx = f(x)**2 - f(x)
        hx = f(x)**2 - f(x)
        data.append([i,x,fx,gx,hx])
    # output tabel
    header = []
    a = 'No'
    b = 'x'
    c = 'f(x)'
    d = 'g(x)'
    e = 'h(x)'
    header.append([a,b,c,d,e])
    for row in header :
        print('+' + ('-'*7)+'+'+('-'*8)+'+'+('-'*17)+'+'+('-'*17)+'+'+('-'*16)+'+')
        print('|{:<6} | {:<6} | {:<15} | {:<15} | {:<15}|'.format(*row))
        print('+' + ('-'*7)+'+'+('-'*8)+'+'+('-'*17)+'+'+('-'*17)+'+'+('-'*16)+'+')
        for row in data :
           print('|{:<6} | {:<6} | {:<15} | {:<15} | {:<15}|'.format(*row))
           print('+' + ('-'*7)+'+'+('-'*8)+'+'+('-'*17)+'+'+('-'*17)+'+'+('-'*16)+'+')
    ulang = input('input nilai x lagi Y/N? ').strip().upper()
    if ulang != 'Y' :
        break
    
