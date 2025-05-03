class Human:
    def __init__(self, name, job, home, money):
        self.name = name
        self.job = job
        self.home = home
        self.money = money
        self.hp = 100
        self.famine = 100
        self.gladness = 100
        self.a = 0
        self.work_up = 2000


    def eat(self):
        if self.home.food <= 0 :
            self.famine -= 20
            print("Немає їжі дома")
            self.shopping()
        else:
            self.famine += 20
            self.home.food -= 10
            print("Наївся")

    def famine(self):
        if self.famine <= 30:
            self.hp -= 10
        elif self.famine >= 100:
            self.hp += 20
            self.famine -= 20

    def shopping(self):
        if self.money < 30:
            print("Недостатньо Грошей")
            self.work()

        else:
            self.money -= 30
            self.home.food += 20
            print("Купив їжу")
            self.eat()

    def work(self):
        self.money += self.job.salary
        self.gladness += self.job.gladness_less
        self.famine -= 10
        if self.money >= self.work_up and self.a <= 3:
            self.money -= 2000
            self.job.salary += 100
            self.a += 1
            self.work_up += 1000
            print("Вас повисили на роботі.")
        print("Устав...")

    def chill(self):
        if self.gladness >= 100:
            self.work()
        elif self.famine >= 80 and self.gladness <= 80:
            self.gladness += 20
            self.famine -= 10
            print("Добре відпочив")
        else:
            self.gladness += 10
            print("Відпочив")


    def is_alive(self):
        if self.hp <= 0:
            print(f"{self.name} помер. Ви програли")
            return False
        elif self.famine <= 0:
            print(f"{self.name} помер від голоду. Ви програли")
            return False
        elif self.gladness <= 0:
            print(f"{self.name} впав в депресію. Ви програли")
            return False
        elif self.money <= -100:
            print(f"{self.name} набрав багато кредитів. Ви програли")
            return False
        elif self.money >= 100000:
            print(f"{self.name} заробив Міліон")
            return False
        else:
            return True



    def hospital(self):
        if self.hp <= 30:
            self.hp += 20
            self.money -= 30
            print("Ви пішли в лікарню")
        elif self.gladness <= 20:
            self.gladness += 30
            self.money -= 30
            print("Ви пішли в психолога")




    def live(self,day):
        if self.hp <= 30:
            self.hospital()
        elif self.famine <= 70:
            self.eat()
        elif self.money <= 100:
            self.work()
        elif self.gladness <= 40:
            self.chill()
        else:
            self.chill()

        self.day_str(day)

    def day_str(self, day):
        print(f"День: {day} життя {self.name}")
        print(f"Hp: {self.hp} ")
        print(f"Голод: {self.famine}")
        print(f"Їжа дома: {self.home.food}")
        print(f"Гроші: {self.money} ")
        print(f"Gladness: {self.gladness} ")


class Job:
    def __init__(self, name, salary, gladness_less):
        self.name = name
        self.salary = salary
        self.gladness_less = gladness_less

class House:
    def __init__(self, address, food):
        self.address = address
        self.food = food


job1 = Job(name="Macdonals", salary=20, gladness_less= -10)
house1 = House(address="Homeless", food=20)
human1 = Human(name="Mark", job=job1, home=house1, money=30)

job2 = Job(name="Стройка", salary=60, gladness_less= -20)
house2 = House(address="D7", food=30)
human2 = Human(name="Stanislav", job=job2, home=house2, money=50)

for day in range(1, 10000):
    human1.live(day)
    human2.live(day)
    if human1.is_alive() and human2.is_alive() == False:
        break