n = input()
n = n.split()

if n[1] == "*":
    print(int(n[0]) * int(n[2]))
elif n[1] == "+":
    print(int(n[0]) + int(n[2]))
elif n[1] == "-":
    print(int(n[0]) - int(n[2]))
elif n[1] == "/":
    print(int(n[0]) // int(n[2]))