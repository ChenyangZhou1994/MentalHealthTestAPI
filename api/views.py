from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from SA import model_predict

# Create your views here.
class SubmitView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)
        sentence = request.data.get('sentence')
        # inputValue = str(inputValue)
        print(type(sentence))
        print(sentence)
        data = model_predict.work(self, sentence=sentence)
        return Response(data)
