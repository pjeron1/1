import sqlite3
import requests

class USDCurrencyConverter:
    def __init__(self, rate_usd):
        self.rate_usd = rate_usd

    def convert_to_usd(self, amount_uah):
        return round(amount_uah / self.rate_usd, 2)

class EURCurrencyConverter:
    def __init__(self, rate_eur):
        self.rate_eur = rate_eur

    def convert_to_eur(self, amount_uah):
        return round(amount_uah / self.rate_eur, 2)

def get_usd_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]['rate']

def get_eur_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]['rate']


rate_usd = get_usd_exchange_rate()
rate_eur = get_eur_exchange_rate()

def mainUSD():
    try:
        print(f"Офіційний курс гривні до долара США: {rate_usd} грн за 1 USD")
        amount_uah = float(input("Введіть суму в гривнях: "))
        converter = USDCurrencyConverter(rate_usd)
        amount_usd = converter.convert_to_usd(amount_uah)
        print(f"Еквівалент у доларах США: {amount_usd} USD")
    except Exception as e:
        print(f"Сталася помилка: {e}")


def mainEUR():
    try:
        print(f"Офіційний курс гривні до Євро: {rate_eur} грн за 1 EUR")
        amount_uah = float(input("Введіть суму в гривнях: "))
        converter = EURCurrencyConverter(rate_eur)
        amount_eur = converter.convert_to_eur(amount_uah)
        print(f"Еквівалент у доларах США: {amount_eur} USD")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    choice = input("Оберіть валюту (USD або EUR): ").strip().upper()
    if choice == "USD":
        mainUSD()
    elif choice == "EUR":
        mainEUR()
    else:
        print("Невірний вибір.")

connection = sqlite3.connect("final_project.db")
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS exchange_rate (
        name TEXT NOT NULL,
        rate REAL NOT NULL
    )
''')
connection.commit()


currency_data = [
    ("Euro", rate_eur),
    ("USD", rate_usd)
]
cursor.execute("DELETE FROM exchange_rate")
cursor.executemany("INSERT INTO exchange_rate (name, rate) VALUES (?, ?)", currency_data)
connection.commit()


cursor.execute("SELECT * FROM exchange_rate")
rows = cursor.fetchall()
for r in rows:
    print(r)

cursor.close()
connection.close()