from rest_framework import serializers
from .models import(
    CommentM,
    CreatelikeM,
)
class Commentserializers(serializers.ModelSerializer):
    class Meta:
        model = CommentM
        fields = "__all__"



class Likecreateser(serializers.ModelSerializer):
    class Meta:
        model = CreatelikeM
        fields = "__all__"
