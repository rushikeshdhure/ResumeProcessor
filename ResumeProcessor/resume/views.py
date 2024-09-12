# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage
from .open_file import extract_resume_details

from django.http import HttpResponse
def home(request):
    return HttpResponse("Project is running!!!")

class ResumeExtractView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_path = default_storage.save(file.name, file)
        resume_data = extract_resume_details(file_path)
        return Response(resume_data)