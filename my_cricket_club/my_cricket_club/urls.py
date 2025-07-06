from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/members/')),  # Redirect root to /members
    path('members/', include('members.urls')),  # DO NOT add 'members/' again in the app urls
    path('admin/', admin.site.urls),
]
