from django.urls import path
from django.conf.urls import url 
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('api',views.api,name='api'),
    #path('updateTablesecond',views.updateTablesecond,name='updateTablesecond'),
    url(r'^external-books/',views.external_books),
    
    url(r'^api/external-books/name',views.finding),
    url(r'^api/external-books/',views.external_books),
    url(r'^api/v1/books/updateTablesecond', views.updateTablesecond),
    url(r'^api/v1/books/:[0-9]+/update', views.update),
    url(r'^api/v1/books/:[0-9]+/delete', views.deleteding),
    url(r'^api/v1/books/:[0-9]+', views.process),
    url(r'^api/v1/books$', views.books),
    url(r'^api/v1', views.search_options),
    url(r'^api/v1/books(?P<pk>[0-9]+)$', views.books),
    url(r'^api/', views.api_options)
    #url(r'^api/v1/published$', views.tutorial_list_published)

    #path('api/v1/books',views.books,name='books')
]