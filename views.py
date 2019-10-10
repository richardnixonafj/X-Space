from django.shortcuts import render
import requests


def github(request): user = {}


if 'username' in request.GET: username = request.GET['username']
url = 'https://api.github.com/users/ % s' % username
response = requests.get(url)
user = response.json()
return render(request, 'core/github.html', {'user': user})
