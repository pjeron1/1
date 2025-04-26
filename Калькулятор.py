a = int(input("Перше число : "))
b = int(input("Друге число : "))
c = input("Математична дія : ")

if c == "+":
    print(a+b)
elif c =="-":
    print(a-b)
elif c =="*":
    print(a*b)
elif c =="/" and b == 0:
    print("Ділення на нуль")
elif c =="/":
    print(a/b)
else:
    print("error")