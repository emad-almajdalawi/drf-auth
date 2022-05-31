from rest_framework import generics
from .models import Meme, MemeNoImg
from .serializers import MemeSerializer, MemeNoImgSerializer
from .permissions import OwnerOrReadOnly, CreateOrReadOnly, OwnerLogin, CreateLogin

class MemesListCreateAPI(generics.ListCreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = (CreateLogin,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class MemesDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = (OwnerOrReadOnly,)



class MemesNoImgListCreateAPI(generics.ListCreateAPIView):
    queryset = MemeNoImg.objects.all()
    serializer_class = MemeNoImgSerializer
    permission_classes = (CreateLogin,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)