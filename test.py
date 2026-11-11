import random
memes = ["Это фиаско, братан", "Кринж", "База", "Изи катка", "Гг вп", "Скилл ишью"]
print("Твой мем на сегодня:")
print(random.choice(memes))

name = "Тина"
age = 16
hobby = "программирование"
group = "13/9"
print("Меня зовут", name)
print("Мне", age, "лет")
print("Я учусь в группе", group)
print("Моё хобби —", hobby)

price = 2000
discount = 50
final = price - price * discount / 100
print("Игра стоила", price, "рублей")
print("Скидка", discount, "%")
print("Итоговая цена:", final, "рублей")