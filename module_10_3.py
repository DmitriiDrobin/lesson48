import time
import threading
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def  deposit(self):
            for i in range(100):
                a = randint(50, 500)
                self.balance += a
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                print(f"Пополнение: {a}. Баланс: {self.balance}")
                time.sleep(0.001)

    def  take(self):
        for i in range(100):
            b = randint(50, 500)
            print(f"Запрос на {b}")
            if b <= self.balance:
                self.balance -= b
                print(f"Снятие: {b}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')