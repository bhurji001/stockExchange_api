from django.shortcuts import render
import requests
import json

# Create your views here.
 
def index(request):
    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_e9bb46ce9c8f43959889b7f148ecceb4')
    api = api_request.json()

    # try:
    # api = json.loads(api_request.content)
    # except Exception as e:
        # api = "Error, data is not loading"
    return render(request, 'index.html',{'api': api})


