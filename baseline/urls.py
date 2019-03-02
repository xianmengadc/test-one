from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'companyList', views.CompaniesViewset)
router.register(r'datalist', views.CompaniesViewset)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('user_admin/', views.user_admin, name='user_admin'),
    path('xxxq/', views.xxxq, name='xxxq'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),

    path('edit_com/<str:street_district>/<int:cid>/', views.edit_com, name='edit_com'),

    path('edit_611_1/<cid>/', views.edit_611_1, name='edit_611_1'),
    path('delete_611_1/<cid>/', views.delete_611_1, name='delete_611_1'),
    path('edit_611_2/<cid>/', views.edit_611_2, name='edit_611_2'),
    path('edit_611_3/<cid>/', views.edit_611_3, name='edit_611_3'),
    path('edit_611_4/<cid>/', views.edit_611_4, name='edit_611_4'),
    path('edit_611_5/<cid>/', views.edit_611_5, name='edit_611_5'),
    path('edit_611_6/<cid>/', views.edit_611_6, name='edit_611_6'),
    path('baseline/<str:district>/', views.baseline, name='baseline'),
    path('basedata/<str:street_district>/', views.basedata, name='basedata'),

    path('accounts/', include('django.contrib.auth.urls')),
    # path('baseline/dgn', views.baseline, name='baseline/nym'),
    # path('baseline/tyl', views.baseline, name='baseline/nym'),
    # path('baseline/wyl', views.baseline, name='baseline/nym'),
    # path('baseline/cal', views.baseline, name='baseline/nym'),
    # path('baseline/zjc', views.baseline, name='baseline/nym'),

    url(r'^list/<str:name>/$', views.dataView),

]

urlpatterns += [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
handler404 = views.page_not_found #改动2