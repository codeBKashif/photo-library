from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from library_api.models import Photo
from library_api.serializers import PhotoSerializer
from library_api.services import FileContent, UploadFileFactory, UploadToLocalDrive



class PhotoView(APIView):

    def post(self, request):
        serializer = PhotoSerializer(data=request.data, many=True)
        if serializer.is_valid():

            files = map(lambda x: FileContent(x["name"], x["file"], x["destinations"]), request.data)
            upload_file_factory = UploadFileFactory()
            upload_file_factory.upload(files)

            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK)
        else:
            return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, id=None):
        if id:
            photo = Photo.objects.get(id=id)
            serializer = PhotoSerializer(photo)
            return Response(serializer.data, status=status.HTTP_200_OK)


        filters = {}
        
        formats = request.GET.get("formats", None)
        name = request.GET.get("name", None)
        destinations = request.GET.get("destinations")

        if formats:
            filters["formats"] = formats
        if name:
            filters["name"] = name
        if destinations:
            filters["destinations"] = destinations

        queryset = Photo.objects.filter(**filters)
        serializer = PhotoSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Photo, id=id)
        item.delete()
        return Response({ "data": "Item Deleted"})