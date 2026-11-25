import requests
 
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
print("Статус-код:", response.status_code)

data = response.json()
print("Всего пользователей:", len(data))
 
for user in data:
    print(user["name"], "-", user["email"])
print(data[0]["address"]["city"])

import pandas as pd
 
df = pd.DataFrame(data)
print(df.head())


df = df[["id", "name", "username", "email", "phone", "website"]]
print(df.head())


import json
import os
 
os.makedirs("data", exist_ok=True)
 
df.to_csv("data/users.csv", index=False)
 
with open("data/users.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
 
print("Файлы сохранены:", os.listdir("data"))


dirty = [dict(u) for u in data]        # копии словарей
 
dirty[0]["email"] = None               # пропуск
dirty.append(dirty[1])                 # дубликат
 
df_dirty = pd.DataFrame(dirty)
df_dirty = df_dirty[["id", "name", "email"]]
print("Пропуски по колонкам:")
print(df_dirty.isnull().sum())
print("Найдено дубликатов:", df_dirty.duplicated().sum())


from datetime import datetime
 
def fetch_and_backup(url, folder="data"):
    """Делает GET-запрос и сохраняет ответ с датой в имени файла."""
    response = requests.get(url)
    if response.status_code != 200:
        print("Запрос не удался, код:", response.status_code)
        return None
 
    data = response.json()
    stamp = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"users_{stamp}.json")
 
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
 
    print("Бэкап сохранён:", path)
    return pd.DataFrame(data)
 
df = fetch_and_backup(url)
