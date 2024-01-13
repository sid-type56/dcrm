from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from rest_framework import serializers
from .models import Record ,MyInterest
from rest_framework import generics
from .serializers import MyModelSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .auxillaryFunctions import *
import json
# Create your views here.

def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"Error login")
            return redirect('home')
    return render(request,'home.html',{})



def logout_user(request):
    logout(request)
    messages.success(request,'you have been logged out!!')
    return redirect('home')

def register_user(request):
    return render(request,'register.html',{})


class MyModelListAPIView(generics.ListAPIView):
    queryset = Record.objects.all()
    serializer_class=MyModelSerializer

@require_http_methods(['GET'])
def show_records_of_interest(request):
    # Retrieve all instances of the MyInterest model
    interests = MyInterest.objects.all()

    # Convert queryset to a list of dictionaries (each instance is represented as a dictionary)
    interests_list = [{'name': interest.name, 'interest': interest.interest,} for interest in interests]

    # Return the result as JSON
    return JsonResponse({'interests': interests_list}, safe=False)

@require_http_methods(['POST'])
@csrf_exempt
def add_interests(request):
     # Get the name and interest from the POST request

    # Parse JSON data from the request body
    json_data = json.loads(request.body.decode('utf-8'))
    
    # Get the name and interest from the parsed JSON data
    name = json_data.get('name', '')
    interest = json_data.get('interest', '')

    # name = request.POST.get('name','')
    # interest = request.POST.get('interest','')
    print('name',name)
    print('interest',interest)

    # Validate input data
    validation_result, is_valid = validate_input(name, interest)
    
    if not is_valid:
        return JsonResponse(validation_result, status=400)



    try:
        # Create an instance of MyInterest model
        new_interest=MyInterest(name=name,interest=interest)
        # Save the instance to the database
        new_interest.save()
        return JsonResponse({'message': 'Interest added successfully'}, status=201)
    except Exception as e:
        # Return an error response if something goes wrong
        return JsonResponse({'error': str(e)}, status=500)