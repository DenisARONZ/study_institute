import random

x = random.randint(1,10)
k = -777

while (k!=x):
    print("Подберите ключ от одного до десяти")
    k = int(input())
    if (x == k):
        print("Вы угадали ключ") 
