a = int(input("Введите сторону a: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
p = a + b + c
p2 = p // 2
s = (p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5
print(s)
