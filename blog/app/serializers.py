from rest_framework import serializers
from .models import Test, Blog2


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ['name']

class Blog2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog2
        fields = ['title','body','user_id','tag','create_time', 'update_time']