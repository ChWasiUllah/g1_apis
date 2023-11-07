from django.shortcuts import get_object_or_404
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from djoser.conf import settings
from djoser.utils import decode_uid


import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class CustomActivationView(APIView):
    def get(self, request, uid, token):
        protocol = 'https://' if request.is_secure() else 'http://'
        web_url = protocol + request.get_host()
        post_url = web_url + "/api/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}

        try:
            result = requests.post(post_url, data=post_data)
            result.raise_for_status()  # Raise HTTPError for bad requests
            message = result.text
            response_data = {
                'success': True,
                'message': message if message else 'Activation successful.'
            }
        except requests.exceptions.HTTPError as err:
            # Handle HTTP errors (status codes other than 2xx)
            response_data = {
                'success': False,
                'message': f'Activation failed: {err}'
            }
        except requests.exceptions.RequestException as err:
            # Handle non-HTTP request exceptions (e.g., network errors)
            response_data = {
                'success': False,
                'message': f'Error during activation: {err}'
            }

        return Response(response_data)

from django.shortcuts import render
from django.http import HttpResponse

class CustomPasswordResetConfirmView(APIView):
    def get(self, request, uid, token):
        response_data = {'uid': uid, 'token': token}
        return Response(response_data)

