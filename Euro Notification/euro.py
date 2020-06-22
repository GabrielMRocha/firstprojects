import requests, json
from send_email import send_email

def AlphpaFetcher(from_currency, to_currency, api_key) :

	alpha_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

	final_url = alpha_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key

    # Fire a get req to API
	req_ob = requests.get(final_url)

    # get the results in dictionary from JSON response

	result = req_ob.json()

	return result["Realtime Currency Exchange Rate"]['5. Exchange Rate']
# Main Function


# currency code
from_currency = "EUR"
to_currency = "BRL"

# pass your api key here
api_key = "LVA6PCS7X1U20ZT5"

# Call the AlphpaFetcher
send_email ("gabrielmar.rocha@gmail.com", AlphpaFetcher(from_currency, to_currency, api_key))
