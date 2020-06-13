n = int(input("Enter an even number:"))
for i in range(1, n):
    for j in range(1, n):
        if (i == 1 or j == 1 or i == n//2 or
            (j == n-1 and i < n//2) or
                (i-j == 2 and i > n//2)):
            print("*", end="")
        else:
            print(" ", end="")
    print()
