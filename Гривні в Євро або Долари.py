import sqlite3
import requests
#Створіть Converter.db
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

class CNYCurrencyConverter:
    def __init__(self, rate_cny):
        self.rate_cny = rate_cny

    def convert_to_cny(self, amount_uah):
        return round(amount_uah / self.rate_cny, 2)

class GELCurrencyConverter:
    def __init__(self, rate_gel):
        self.rate_gel = rate_gel

    def convert_to_gel(self, amount_uah):
        return round(amount_uah / self.rate_gel, 2)

class ILSCurrencyConverter:
    def __init__(self, rate_ils):
        self.rate_ils = rate_ils

    def convert_to_ils(self, amount_uah):
        return round(amount_uah / self.rate_ils, 2)

class KZTCurrencyConverter:
    def __init__(self, rate_kzt):
        self.rate_kzt = rate_kzt

    def convert_to_kzt(self, amount_uah):
        return round(amount_uah / self.rate_kzt, 2)

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

def get_cny_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=CNY&json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]['rate']

def get_gel_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=GEL&json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]['rate']

def get_ils_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=ILS&json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]['rate']

def get_kzt_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=KZT&json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]['rate']


rate_usd = get_usd_exchange_rate()
rate_eur = get_eur_exchange_rate()
rate_cny = get_cny_exchange_rate()
rate_gel = get_gel_exchange_rate()
rate_ils = get_ils_exchange_rate()
rate_kzt = get_kzt_exchange_rate()



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
        print(f"Еквівалент у Євро: {amount_eur} EUR")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def mainCNY():
    try:
        print(f"Офіційний курс гривні до Юаня Женьміньбі: {rate_cny} грн за 1 CNY")
        amount_uah = float(input("Введіть суму в гривнях: "))
        converter = CNYCurrencyConverter(rate_cny)
        amount_cny = converter.convert_to_cny(amount_uah)
        print(f"Еквівалент у Юаня Женьміньбі: {amount_cny} CNY")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def mainGEL():
    try:
        print(f"Офіційний курс гривні до Ларі: {rate_gel} грн за 1 GEL")
        amount_uah = float(input("Введіть суму в гривнях: "))
        converter = GELCurrencyConverter(rate_gel)
        amount_gel = converter.convert_to_gel(amount_uah)
        print(f"Еквівалент у Ларі: {amount_gel} GEL")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def mainILS():
    try:
        print(f"Офіційний курс гривні до Нового ізраїльського шекеля: {rate_ils} грн за 1 ILS")
        amount_uah = float(input("Введіть суму в гривнях: "))
        converter = ILSCurrencyConverter(rate_ils)
        amount_ils = converter.convert_to_ils(amount_uah)
        print(f"Еквівалент у Новий ізраїльський шекель: {amount_ils} ILS")
    except Exception as e:
        print(f"Сталася помилка: {e}")

def mainKZT():
    try:
        print(f"Офіційний курс гривні до Теньге: {rate_kzt} грн за 1 KZT")
        amount_uah = float(input("Введіть суму в гривнях: "))
        converter = KZTCurrencyConverter(rate_kzt)
        amount_kzt = converter.convert_to_kzt(amount_uah)
        print(f"Еквівалент у Теньге: {amount_kzt} KZT")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    choice = input("Оберіть валюту (USD, EUR, CNY, GEL, ILS, KZT): ").strip().upper()
    if choice == "USD":
        mainUSD()
    elif choice == "EUR":
        mainEUR()
    elif choice == "CNY":
        mainCNY()
    elif choice == "GEL":
        mainGEL()
    elif choice == "ILS":
        mainILS()
    elif choice == "KZT":
        mainILS()
    else:
        print("Невірний вибір.")


#Створіть Converter.db
connection = sqlite3.connect("Converter.db")
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS exchange_rate (
        name TEXT NOT NULL,
        rate REAL NOT NULL,
        country TEXT NOT NULL
    )
''')
connection.commit()


currency_data = [
    ("Euro", rate_eur, "Europapa"),
    ("USD", rate_usd, "Amerima"),
    ("CNY", rate_cny, "Chinese party"),
    ("GEL", rate_gel, "ქართული ვალუტა"),
    ("ILS", rate_ils, "ובכן, אין מה לעשות עם זה"),
    ("KZT", rate_kzt, "Країна Бората")
]
cursor.execute("DELETE FROM exchange_rate")
cursor.executemany("INSERT INTO exchange_rate (name, rate, country) VALUES (?, ?, ?)", currency_data)
connection.commit()


cursor.execute("SELECT * FROM exchange_rate")
rows = cursor.fetchall()
for r in rows:
    print(r)

cursor.close()
connection.close()