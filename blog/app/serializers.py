from rest_framework import serializers
from .models import Blog2


class Blog2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog2
        fields = ['id', 'title','body','user_id','tag','create_time', 'update_time']