from django.contrib import admin
from models import *

class EnlaceAdmin(admin.ModelAdmin):

	list_display = ('titulo','enlace','categoria','imagen_voto','es_popular')
	list_filter = ('categoria','usuario','titulo',) #generalmente lo que se repite
	search_fields = ('categoria__titulo','usuario__email')
	list_editable = ('titulo','enlace')
	list_display_links = ('categoria',)
	raw_id_fields = ('categoria','usuario',)
	def imagen_voto(self,obj):
		url = obj.mis_votos_en_imagen_rosada()
		tag = '<img src="%s" >' %url
		return tag

	imagen_voto.allow_tags = True
	imagen_voto.admin_order_field = 'votos'

class CategoriaAdmin(admin.ModelAdmin):
	pass #es lo mismo que usar break;

admin.site.register(Categoria)
admin.site.register(Enlace,EnlaceAdmin)