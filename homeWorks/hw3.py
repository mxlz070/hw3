class Bank:
    def __init__(self,name , balance):
        self._name = name
        self._balance = balance
    def moneyX(self):
        try:
            money = int(input('Введите сумму для пополнения: '))
            return self._balance + money
        except ValueError:
            return 'Вводите только числа!'
    def _kill(self):
        kill_balanse = self._balance = 0
        return f'Ваш баланс: {kill_balanse}'
    def __jackpot(self):
        return f'Вы выиграли ДЖЕКПОООТ! {self._balance * 10}'
    def _stolenone(self, other):
        return f'Ваш баланс: {self._balance + other._balance}'
Beka = Bank('Bek', 1234)
Alim = Bank("Beka", 12345)
#print(Alim._kill())
# print(Alim.moneyX())
print(Alim._Bank__jackpot())
print(Alim._stolenone(Beka))


