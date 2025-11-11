from django.urls import path, include
from rest_framework import routers
from noticia import views
from noticia.views import UploadImageView

router = routers.DefaultRouter()
router.register(r'note', views.NoteView ,'notes')
router.register(r'category', views.categoryView ,'categories')
router.register(r'label', views.LabelView ,'labels')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/upload-image/', UploadImageView.as_view(), name='upload-image'),
    path('api/v1/upload-image/', UploadImageView.as_view(), name='upload-image'),
    
    path('loginPage/', views.loginView, name='loginPage'),  
    path('register/', views.registerView, name='register'),  
    path('profile/', views.profileView, name='profile'),

]