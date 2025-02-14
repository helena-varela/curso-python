flag = True
while flag:
    n1 = int(input('Diga um número: '))
    n2 = int(input('Diga outro número: '))
    flag = n1 + n2 <= 10
    print(flag)
