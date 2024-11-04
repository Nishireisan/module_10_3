import threading
import random
import time



class Bank:
    counter = 0
    balance = 0
    lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            a = random.randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        for i in range(100):
            a = random.randint(50, 500)
            print(f'Запрос на {a}')
            if self.balance >= a:
                self.balance -= a
                print(f'Снятие: {a}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
