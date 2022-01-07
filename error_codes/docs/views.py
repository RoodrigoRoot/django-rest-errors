from django.http import JsonResponse
from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView
from django.views import View
from error_codes.functions import category_all,  get_category_by_name, get_error_code
# Create your views here.


class DocsTemplateView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        categories = category_all()
        title = ''
        description = ''
        return render(request, self.template_name, locals())


class CategoriesDocsTemplate(View):
    template_name = "details_category.html"

    def get(self, request, name):
        category = get_category_by_name(name)
        errors_codes = category.error_set.all().order_by('error_code')
        return render(request, self.template_name, locals())


class ErrorDocTemplate(View):
    template_name = "details_errors_codes.html"

    def get(self, request, error_code):
        error_code = get_error_code(error_code)
        return render(request, self.template_name, locals())


class SearchDocTemplate(View):

    def get(self, request):
        param_error_code = request.GET.get('value', '')
        error_code = get_error_code(param_error_code)
        if not error_code:
            url = reverse('not-found')
            return JsonResponse({'url': url}, safe=False)
        url = reverse('error:error-code', kwargs={'error_code': error_code})
        return JsonResponse({'url': url}, safe=False)


class CodeNotFound(TemplateView):
    template_name = 'not_found.html'

