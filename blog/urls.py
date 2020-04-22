from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_blog/<int:blog_id>', views.delete_blog),
    path('update_blog/<int:blog_id>', views.update_blog)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
