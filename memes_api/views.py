from rest_framework import generics
from .models import Meme
from .serializers import MemeSerializer
from .permissions import OwnerOrReadOnly, CreateOrReadOnly

class MemesListCreateAPI(generics.ListCreateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = (CreateOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class MemesDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    permission_classes = (OwnerOrReadOnly,)