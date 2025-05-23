import requests

class CurrencyConverter:
    def __init__(self, rate):
        self.rate = rate

    def convert_to_usd(self, amount_uah):
        return round(amount_uah / self.rate, 2)

def get_usd_exchange_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data[0]['rate']

def main():
    try:
        rate = get_usd_exchange_rate()
        print(f"Офіційний курс гривні до долара США: {rate} грн за 1 USD")
        amount_uah = float(input("Введіть суму в гривнях: "))
        converter = CurrencyConverter(rate)
        amount_usd = converter.convert_to_usd(amount_uah)
        print(f"Еквівалент у доларах США: {amount_usd} USD")
    except Exception as e:
        print(f"Сталася помилка: {e}")

if __name__ == "__main__":
    main()