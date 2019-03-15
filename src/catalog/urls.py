from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('catalog', views.ItemModelList.as_view(), name="catalog"),
    path('item/add/', views.ItemCreateView.as_view(), name='item_add'),
    re_path(r'item/detail/(?P<slug>[-\w\d]+)/$',
            views.ItemDetailView.as_view(), name='item_detail'),
    re_path(r'item/update/(?P<slug>[-\w\d]+)/$',
            views.ItemUpdateView.as_view(), name='item_update'),
    re_path(r'item/delete/(?P<slug>[-\w\d]+)/$',
            views.ItemDeleteView.as_view(), name='item_delete'),
    path('item/list/', views.ItemListView.as_view(), name="item_list"),
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),


    # path('edit/<int:pk>', views.ItemUpdateView.as_view(), name='item_detail'),

    # re_path(r'item/(?P<slug>[-\w\d]+)/$',
    #         views.ItemDetailView.as_view(), name='item_detail'),

    # path('items/', views.item_list, name='item_list'),
    # path('items/create/', views.item_create, name='item_create'),


    # ,(?P<id>\d+)
    # path('basic-upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    # path('<slug:slug>,<int:id>/', views.article_detail, name='article'),

    # path('', views.ItemList.as_view(), name='catalog'),
    # path('company/add/', views.RecipeCreateView.as_view(), name='company-add'),
    # path('', views.RecipeCreateView.as_view()),
    # re_path(r'company/(?P<pk>[0-9]+)/$', views.CompanyUpdate.as_view(), name='company-update'),
    # re_path(r'company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company-delete'),
]
