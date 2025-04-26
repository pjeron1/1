number = int(input("Введіть число : "))
n = 1


if (number % 2) == 0:
    print(number)
while n!=number:
    number -= 1
    if (number % 2) == 0:
        print(number)
