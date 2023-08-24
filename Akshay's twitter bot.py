n = int(input("Input N: "))

for i in range(1, n+1):
    for j in range(i, i+i):
        print(j%2, end="")
    print()