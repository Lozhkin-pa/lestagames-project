import os

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .services.term_frequency import term_frequency


def index(request):
    if request.POST:
        files = request.FILES.getlist('file')
        files_name_list = []
        for f in files:
            path = os.path.join(settings.BASE_DIR, 'data')
            file_name = FileSystemStorage(location=path).save(f.name, f)
            files_name_list.append(file_name)
        result_tf_idf = term_frequency(files_name_list)
        context = {
            'result_tf_idf': result_tf_idf,
            'file_upload': True,
        }
    else:
        context = {
            'file_upload': False,
        }
    return render(request, 'index.html', context)
