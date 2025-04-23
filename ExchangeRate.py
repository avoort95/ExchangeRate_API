import requests
import pandas as pd

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=545aca5268249b9b0ae97980e08cb4a9'

response = requests.get(url)
data = response.json()
print(data)

rates = data['rates']
print(rates)
print(type(rates))

df = pd.DataFrame.from_dict(rates, orient='index')
print(df.nunique())
print(df)
df = df.reset_index()
df.columns = ['currency', 'rate']
print(df.head())

amount = float(input(f"Enter the amount of euros you wish to convert: "))
while True:
    currency = str(input(f"Enter the target currency: ")).upper()
    if len(currency) > 3:
        print("Input exceeds 3 characters. Please try again.")
    elif currency not in df['currency'].values:
        print("Currency not found. Please try again.")
    else:
        target_rate = float(df[df['currency'] == currency]['rate'].values[0])
        total = amount * target_rate
        print(f"{amount} EUR is equal to {total} {currency} based on the current rate of {target_rate}")
        break
