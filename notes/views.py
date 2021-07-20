from django.shortcuts import get_object_or_404
from notes.serializers import NoteSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Note
from .permissions import IsOwner


class NoteViewSet(viewsets.ModelViewSet):
    """
    NoteViewSet - CRUD for user notes.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        notes = user.note.all()
        return notes

    def retrieve(self, request, pk, *args, **kwargs):
        notes = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(notes, context={'request': request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
