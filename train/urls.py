from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from froala_editor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('account/', include('account.urls')),
    path('station/', include('station.urls')),
    path('station/route/', include('route.urls')),
    path('froala_editor/', include('froala_editor.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += re_path(r'^media/(?P<path>.*)$', serve,
                       {'document_root': settings.MEDIA_ROOT}),
urlpatterns += re_path(r'^static/(?P<path>.*)$', serve,
                       {'document_root': settings.STATICFILES_DIRS[0]}),

handler404 = 'train.views.errorpage404'
handler500 = 'train.views.errorpage500'
