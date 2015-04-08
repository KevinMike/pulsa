from random import choice

frases = ['Leonidas esta sentado','fredy se fue','borussia dortmund']
def ejemplo(request):
	return {'frase': choice(frases)}

from django.core.urlresolvers import reverse

def menu(request):
	menu = {'menu': [
		{'name': 'Home', 'url': reverse('home')},
		{'name': 'Add', 'url':reverse('add')},
	]}
	for item in menu['menu']:	
		if request.path == item['url']:
			item['active'] = True
	return menu