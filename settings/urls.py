from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import (ProfileAPIList, ProfileAPIUpdate, ProfileAPIDestroy,
                            PostAPIList, PostAPIUpdate, PostAPIDestroy,
                            CommentAPIList, CommentAPIUpdate, CommentAPIDestroy
                            )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/profile/', ProfileAPIList.as_view()),
    path('api/v1/profile/<int:pk>/', ProfileAPIUpdate.as_view()),
    path('api/v1/profiledelete/<int:pk>/', ProfileAPIDestroy.as_view()),
    path('api/v2/post/', PostAPIList.as_view()),
    path('api/v2/post/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v2/postdelete/<int:pk>/', PostAPIDestroy.as_view()),
    path('api/v3/comment/', CommentAPIList.as_view()),
    path('api/v3/comment/<int:pk>/', CommentAPIUpdate.as_view()),
    path('api/v3/commentdelete/<int:pk>/', CommentAPIDestroy.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

