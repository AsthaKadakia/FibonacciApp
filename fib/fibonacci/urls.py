from django.conf.urls import url
from fibonacci import views

urlpatterns = [
    # Disabling the Admin for our API site
    # from django.contrib import admin
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^fibonacci/(?P<name>\w+)$', views.fibonacci_view, name='fibonacci'),
    url(r'^fib/(?P<name>\w+)$', views.fib_view(), name='fib'),
]