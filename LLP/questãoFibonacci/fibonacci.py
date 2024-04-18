n = int(input("Digite Quantos números de fibonacci quer descobrir: "))
a, b = 0, 1
for i in range(1, n + 1):
    print(b, end=" ")
    a,b = b, a+b