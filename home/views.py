from rest_framework import generics
from .serializer import(
    Commentserializers,
    Likecreateser
)
from .models import(
    CommentM,
    CreatelikeM,
)
class Createcommentview(generics.ListCreateAPIView):
    serializer_class = Commentserializers
    queryset = CommentM.objects.all()

class Createlikeview(generics.ListCreateAPIView):
    serializer_class = Likecreateser
    queryset = CreatelikeM.objects.all()
