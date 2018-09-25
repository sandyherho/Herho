from django.shortcuts import render

# Create your views here.

def home(request):
	import requests
	import json

	# Mengambil data harga Crypto
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,XLM,LTC,USDT,ADA,XMR,DASH&tsyms=IDR")
	price = json.loads(price_request.content)

	# Mengambil berita Crypto 
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)

	return render(request, 'home.html', {'api' : api, 'price' : price})

def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=IDR")
		crypto = json.loads(crypto_request.content)
		return render(request,'prices.html', {'quote' : quote, 'crypto' : crypto})
	
	else:
		notfound = "Enter a crypto currency symbol into the form above ..."
		return render(request, 'prices.html', {'notfound' : notfound})
