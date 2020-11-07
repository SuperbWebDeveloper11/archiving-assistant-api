from django.urls import include, path
# from rest_framework.urlpatterns import format_suffix_patterns
from .views import doc_api as doc_api
from .views import company_api as company_api
from .views import company_full_page_rendering as company_full
from .views import doc_full_page_rendering as doc_full

app_name = 'edoc'

urlpatterns = [
    # doc api urls
    path('api/doc/', doc_api.DocList.as_view()),
    path('api/doc/<int:pk>/', doc_api.DocDetail.as_view()),
    # company api urls
    path('api/company/', company_api.CompanyList.as_view()),
    path('api/company/<int:pk>/', company_api.CompanyDetail.as_view()),

    # company full pages rendering urls
    path('company/', company_full.CompanyList.as_view(), name='company_list'),
    path('company/add/', company_full.CompanyCreate.as_view(), name='company_add'),
    path('company/<int:pk>/detail/', company_full.CompanyDetail.as_view(), name='company_detail'),
    path('company/<int:pk>/update/', company_full.CompanyUpdate.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', company_full.CompanyDelete.as_view(), name='company_delete'),

    # doc full pages rendering urls
    path('doc/', doc_full.DocList.as_view(), name='doc_list'),
    path('doc/add/', doc_full.DocCreate.as_view(), name='doc_add'),
    path('doc/<int:pk>/detail/', doc_full.DocDetail.as_view(), name='doc_detail'),
    path('doc/<int:pk>/update/', doc_full.DocUpdate.as_view(), name='doc_update'),
    path('doc/<int:pk>/delete/', doc_full.DocDelete.as_view(), name='doc_delete'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)




