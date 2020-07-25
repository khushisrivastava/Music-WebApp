from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    # serializer_class = PlaylistReadSerializer
    

    def get_serializer_class(self):
        method = self.request.method
        if method == 'GET':
            return PlaylistReadSerializer
        else:
            return PlaylistWriteSerializer
    
 
    @action(detail=False, methods=['post'])
    def add_song(self, request):
        data = request.data
        song_id = data.get('song_id')
        playlist_id = data.get('playlist_id')

        if not playlist_id:
            return Response({
                'detail': 'Provide playlist_id'
            }, status.HTTP_400_BAD_REQUEST)
        if not song_id:
            return Response({
                'detail': 'Provide song_id'
            }, status.HTTP_400_BAD_REQUEST)
        
        try:
            playlist = Playlist.objects.get(pk=playlist_id)
            playlist.song.add(song_id)
            return Response({
                'detail': 'Song Added'
            }, status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'detail': str(e)
            }, status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def delete_song(self, request):
        song_id = request.data.get('song_id')
        playlist_id = request.data.get('playlist_id')

        if not playlist_id:
            return Response({
                'detail': 'Provide playlist_id'
            }, status.HTTP_400_BAD_REQUEST)
        if not song_id:
            return Response({
                'detail': 'Provide song_id'
            }, status.HTTP_400_BAD_REQUEST)

        try:
            playlist = Playlist.objects.get(pk=playlist_id)
            playlist.song.remove(song_id)
            return Response({
                'detail': 'Song Removed'
            }, status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'detail': str(e)
            }, status.HTTP_400_BAD_REQUEST)

    # @action(detail=False, methods=['delete', 'post'])
    # def delete_playlist(self, request, pk=None):
    #     playlist_id = request.data.get('playlist_id')

    #     if not playlist_id:
    #         return Response({
    #             'detail': 'Provide playlist_id'
    #         }, status.HTTP_400_BAD_REQUEST)

    #     try:
    #         playlist = Playlist.objects.get(pk=playlist_id)
    #         playlist.delete()
    #         return Response({
    #             'detail': 'Playlist deleted'
    #         }, status.HTTP_200_OK)

    #     except Exception as e:
    #         return Response({
    #             'detail': str(e)
    #         }, status.HTTP_400_BAD_REQUEST)   


    