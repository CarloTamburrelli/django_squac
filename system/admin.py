from django.contrib import admin
from .models import SystemGame

#admin.site.site_header = "Login to Admin Panel"
#admin.site.site_title = "Game Admin"
#admin.site.index_title = "Welcome!!"
'''

class CustomizeAdminArea(admin.AdminSite):
	site_header = "Admin Custom Area"
	#login_template = 'templates/admin/login.html'

custom_admin = CustomizeAdminArea(name="Admin")
#custom_admin.register(SystemGame)




class SystemAdminCustom(admin.ModelAdmin):
	#exclude = ('name_field')
	#fields = ['user1', 'user2',('user1_points', 'user2_points')] 
	fieldsets = (
		('Sezione 1', {
			'fields' : ('user1', 'user2'),
			'description' : 'Una semplice descrizione'
			}),
		('Sezione 2', {
			'fields' : ('user1_points', 'user2_points')
			}),

	)
	#list_display = ('user1', 'user2',) # <--- colonne da mostrare nella tabella 
	#list_filter = ('created') <--- questo imposta gia' un filtro nella lista
	
	#change_list_template = "admin/percorso...html"

	pass

 
custom_admin.register(SystemGame, SystemAdminCustom)



admin.site.register(SystemGame, SystemAdminCustom)

'''
#admin.site.unregister(....)



'''
	models = django.apps.apps.get_models()

	for model in models:
		try:
			admin.site.register(model)
		except admin.sites.AlreadyRegistered:
			pass
	#admin.site.unregister(....) e se ti va di eliminare qualche modulo che non serve
'''



'''
	personalizza form
	class formclassico(forms.ModelForm):
		def init(self, *args, **kwargs):
			super(formclassico. self).__init__(*args, **kwargs)

		class Meta:
			model = Post


	class PostFormAdmin(Admin.ModelAdmin)
		form = formclassico
		... e qui aggiungi tutte le tue personalizzazioni

	e poi registri questo form come admin.site.register(Post, PostFormAdmin)



'''