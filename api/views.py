# from django.shortcuts import render
# from django.http import JsonResponse

# # Create your views here.


# def home(request):
#     return JsonResponse({'info': 'Django react course', 'name': 'shivam'})


from django.shortcuts import render
from rest_framework import generics, status, viewsets
import io
import csv
import pandas as pd
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer, FileUploadSerializer, SaveVideoSerializer


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    queryset = Video.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file, sep=';')




        for row in reader.itertuples():
            new_video = Video(
                id=row[7],
                VideoLink=row[1],
                description = row[2],
                duration=row[3],
                thumb=row[4],
                embed_code=row[5],
                tags=row[6],
                quality=row[9],
            )
            new_video.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer




#  id = models.CharField(primary_key=True, max_length=30)
#     VideoLink = models.TextField(unique=True)
#     duration = models.CharField(max_length=200)
#     thumb = models.TextField(unique=True)
#     embed_code = models.TextField(unique=True)
#     tags = ArrayField(models.CharField(max_length=200), blank=True)
#     quality = models.CharField(max_length=30)