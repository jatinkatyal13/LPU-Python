from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

# Class Based Views
# class CommonView(View):
#     def get_context(self):
#         return {
#             "name": "Jatin Katyal",
#             "languages": [
#                 "python",
#                 "GO",
#                 "cpp",
#                 "rust"
#             ]
#         }

# class HelloWorldView(CommonView):
#     def get(self, request):
#         context = self.get_context()

#         return render(request, "main/hello.html", context)

class HelloWorldView(TemplateView):
    template_name = "main/hello.html"

    def get_context_data(self, **kwargs):
        return {
            "name": "Jatin Katyal",
            "languages": [
                "python",
                "GO",
                "cpp",
                "rust"
            ]
        }
    

class TablePageView(TemplateView):
    template_name = "main/table.html"
