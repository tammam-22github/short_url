from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import HttpRequest, HttpResponse
from short_url.forms import *
from short_url.models import ShortUrl
import string, random
from .models import ShortUrl


# Create your views here.
def generateShortUrl():
    return "".join(random.choice(string.ascii_letters) for letter in range(19))


class ShortURlView(View):
    form_class = ShortUrlForm
    template_name = "short_url.html"
    context = {"form": form_class()}

    def get(self, request: HttpRequest):
        return render(request, self.template_name, context=self.context)

    def post(self, request: HttpRequest):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.shortUrl = generateShortUrl()
            form.save()
            return redirect("short_url:detail_url", form.pk)


class ShortURLDetailView(View):
    template_name = "short_url_detail.html"

    def get(self, request: HttpRequest, *args, **kwargs):

        try:
            pk = self.kwargs.get("pk")
            obj = get_object_or_404(ShortUrl, pk=pk)
        except ShortUrl.DoesNotExist:
            return HttpResponse("No ShortUrl matches the given query.")
        else:
            context = {"obj": obj}
            return render(request, self.template_name, context)


class RedirectToUrl(View):

    def get(self, request: HttpRequest, *args, **kwargs):
        shorturl = self.kwargs.get("short_url")
        obj = get_object_or_404(ShortUrl, shortUrl=shorturl)
        return redirect(obj.longUrl)
