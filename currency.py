import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
    response = requests.get(url)
    data = response.json()
    if "result" in data and data["result"] is not None:
        return data["result"]
    else:
        print("Error fetching data. Please check currency codes.")
        return None

def main():
    print(" Currency Converter ")
    from_currency = input("Enter base currency (e.g., USD, INR, EUR): ").upper()
    to_currency = input("Enter target currency (e.g., INR, USD, GBP): ").upper()
    amount = float(input("Enter amount: "))

    rate = get_exchange_rate(from_currency, to_currency)

    if rate:
        converted_amount = amount * rate
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}\n")

if __name__ == "_main_":
    main()