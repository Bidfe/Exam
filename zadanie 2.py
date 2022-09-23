def polindrom(a):
    if a == a[::-1]:
        print(f'Слово {a} является полиндромом')
    else:
        print(f'Слово {a} не является полиндромом')


polindrom('aboba')
polindrom('Hello')
