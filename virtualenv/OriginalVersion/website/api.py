from website.models import Video
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'
        # fields=('title',)
        
@api_view(['GET'])
def video_list(request):
    video_list=Video.objects.all()
    serializer=VideoSerializer(video_list,many=True)
    return Response