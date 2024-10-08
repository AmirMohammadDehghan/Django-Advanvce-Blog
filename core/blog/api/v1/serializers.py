from rest_framework import serializers
from ...models import Post




# class PostSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    # fields = '__all__'
    fields = ['id','author', 'title','category', 'status' , 'content','created_date', 'published_date']