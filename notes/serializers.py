from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    url = serializers.HyperlinkedIdentityField(view_name="notes:note-detail")

    class Meta:
        model = Note
        fields = ['title', 'text', 'created', 'url', 'user']
