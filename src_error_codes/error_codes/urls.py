from django.urls import path
from error_codes.docs.views import (DocsTemplateView, CategoriesDocsTemplate,
                                    ErrorDocTemplate, SearchDocTemplate)

app_name = 'error'

urlpatterns = [
    path('docs/', DocsTemplateView.as_view(), name='catalog'),
    path('category/<str:name>/', CategoriesDocsTemplate.as_view(), name='error-category'),
    path('code/<str:error_code>/', ErrorDocTemplate.as_view(), name='error-code'),
    path('search', SearchDocTemplate.as_view(), name='search'),
]

