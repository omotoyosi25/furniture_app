from django.urls import path
from .views import home_page_view, shop, design, contact, about
# ,shop,design,contact,about



urlpatterns=[
    path('', home_page_view, name='home'),
    path('shop/', shop, name='shop'),
    path('design/', design, name='design'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]