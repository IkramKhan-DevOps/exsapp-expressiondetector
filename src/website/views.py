import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView
from src.website.models import ScanImage


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name='website/home.html')

    def post(self, request, *args, **kwargs):
        from base64 import b64decode
        from core.settings import BASE_DIR, HOST_ADDRESS

        data_uri = request.POST['image']
        header, encoded = data_uri.split(",", 1)
        data = b64decode(encoded)

        name = str(str(uuid.uuid4()) + '.png')
        path = f"{BASE_DIR}/media/images/{name}"
        address = f"images/{name}"

        with open(path, "wb") as f:
            f.write(data)
            s = ScanImage.objects.create(image_url=address)

        return HttpResponse(s.pk)


class ImageListView(ListView):
    queryset = ScanImage.objects.all()
    template_name = 'website/scanimage_list.html'
    paginate_by = 20


class ImageDetailView(DetailView):
    model = ScanImage
    template_name = 'website/scanimage_detail.html'
