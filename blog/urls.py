from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('blogView/<int:b_id>', views.blogView),
    # path('bolgContent/', views.blogContents),
    # path('about/', views.about),
    # path('search/', views.search),
    # path('tracker/', views.tracker),
    # path('product_view/<int:my_id>', views.product_view),
    # path('contact/', views.contact),
    # path('checkout/', views.checkout),
]
