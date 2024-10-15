import os

from django.shortcuts import render

from main.forms import UploadFileForm


def read_config():
    try:
        with open(os.path.join('config', 'config.json')) as c:
            config = c.read()
            return config
    except Exception as ex:
        return str(ex)


def list_userfiles():
    try:
        files = os.listdir('userfiles')
        return '\n'.join(files)
    except Exception:
        return "No userfiles found"


def handle_uploaded_file(f):
    with open(f"userfiles/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def index(req):
    if req.method == 'POST':
        form = UploadFileForm(req.POST, req.FILES)
        if form.is_valid():
            handle_uploaded_file(req.FILES["file"])

    f = UploadFileForm()
    return render(req, 'index.html', {
        'config': read_config(),
        'userfiles': list_userfiles(),
        'form': f,
    })
