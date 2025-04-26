import random
rand_number = random.randint(1, 10)
print("Вгадай число")
while True:
    a = int(input("- "))
    if a == rand_number:
        print("Ти переміг!!!")
        break
    elif a >= rand_number:
        print("Менше")
    elif a <= rand_number:
        print("Більше")

