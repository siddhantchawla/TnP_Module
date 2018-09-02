from django.urls import path,include

from . import views

urlpatterns = [
	path('',views.index, name = 'index' ),
	path('register/',views.register_page, name = 'register'),
	path('login/',views.login_page, name = 'login'),
	path('logout/',views.logout_page, name = 'logout'),
	path('home/',views.home, name = 'homeStudent'),
	path('home/coordinator',views.coordinator_home, name = 'homeCoordinator'),
	path('home/updateProfile',views.update_profile, name = 'update'),
	path('home/selected',views.placed, name = 'placed'),


	]