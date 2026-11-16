class Streamer:
    def __init__(self, nick, subscribers):
        self.nick = nick
        self.donates = []
        self.subscribers = subscribers

    def add_donate(self, amount):
        self.donates.append(amount)

    def total_donates(self):
        total = 0
        for d in self.donates:
            total += d
        return total

    def average_donate(self):
        if len(self.donates) == 0:
            return 0
        return self.total_donates() / len(self.donates)

def print_stats(streamer):
    print(f"Стример: {streamer.nick}")
    print(f"Донатов: {len(streamer.donates)}, сумма: {streamer.total_donates()}, средний: {round(streamer.average_donate(), 1)}")
    print(f"Подписчиков: {streamer.subscribers}")

def is_popular(streamer):
    return streamer.subscribers > 1000

print("--- ВАРИАНТ 1 ---")
s = Streamer("ShadowStorm", 1500)
s.add_donate(100)
s.add_donate(250)
s.add_donate(50)
print_stats(s)
print("Популярен:", is_popular(s))