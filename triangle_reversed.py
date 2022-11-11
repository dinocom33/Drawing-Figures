n = int(input("Please enter the number of rows: "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
