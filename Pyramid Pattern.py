rows=int(input("enter size: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
