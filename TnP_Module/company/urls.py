from django.urls import path,include

from . import views

urlpatterns = [
	path('',views.add_companies, name = 'add' ),
	path('application/<int:company_id>/',views.add_applications),
	path('delete_company/<int:company_id>/',views.delete_company),
	path('handling/',views.handling_comapnies, name = 'handling'),
	path('handling/details/<int:company_id>/',views.details, name = 'details'),


	]