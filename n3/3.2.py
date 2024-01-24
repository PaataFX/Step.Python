n = int(input("Choose the number you want for multiply to: "))
n += 1
for i in range(1, n):
    for j in range(1, n):
        result = i * j
        print(result, end="\t")
    print()
