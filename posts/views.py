from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from posts.models import *
from posts.serializers import ReplySerializer, ThoughtCreateSerializer, ThoughtSerializer



class ThoughtList(ListAPIView):

    serializer_class = ThoughtSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', ]

    renderer_classes = [JSONRenderer]
    # pagination_class = SmallPagination

    def get_queryset(self):
        queryset = Thought.objects.filter().order_by('-id')
        return queryset

    def post(self, request, format=None):
        anonymous = False
        if request.data.get('author') == None:
            anonymous = True

        serializer = ThoughtCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_anonymous = anonymous)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ThoughtDetail(APIView):
    def get_object(self, pk):
        try:
            return Thought.objects.get(pk=pk, )
        except Thought.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        val = self.get_object(pk)
        serializer = ThoughtSerializer(val)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        val = self.get_object(pk)
        serializer = ThoughtCreateSerializer(
            val, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        val = self.get_object(pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReplyList(ListAPIView):

    serializer_class = ReplySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['id', ]

    renderer_classes = [JSONRenderer]
    # pagination_class = SmallPagination

    def get_queryset(self):
        queryset = Reply.objects.filter().order_by('-id')
        return queryset

    def post(self, request, format=None):
        serializer = ReplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ReplyDetail(APIView):
    def get_object(self, pk):
        try:
            return Reply.objects.get(pk=pk, )
        except Reply.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        val = self.get_object(pk)
        serializer = ReplySerializer(val)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        val = self.get_object(pk)
        serializer = ReplySerializer(
            val, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        val = self.get_object(pk)
        val.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)