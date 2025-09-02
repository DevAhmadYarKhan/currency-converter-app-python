import requests as rq

url = "https://open.er-api.com/v6/latest/"

# Generates a dictionary of exchange rates normalized to the input currency, assigning 1 to the input currency and corresponding relative values to all others
def get_exchange_rates(initial_currency):
    response = rq.get(url + initial_currency)
    data = response.json()
    if data.get("result") == "success":
        rates = data["rates"]
        return rates
    else:
        return {}