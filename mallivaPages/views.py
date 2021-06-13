from django.shortcuts import render
from django.urls import URLPattern, get_resolver


# Create your views here.
def index(request):
    """
    To be continued
    """
    url_list = {"url_patterns": get_resolver().url_patterns}
    print(URLPattern.resolve)

    return render(request, "mallivaPages/index.html", context=url_list)
