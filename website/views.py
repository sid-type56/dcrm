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
# from .logs.logging_config import logger
from logs.logging_config import logger

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







# APIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPIAPI
    

@require_http_methods(['GET'])
def show_records_of_interest(request):
    logger.info("show_records function")
    # Retrieve all instances of the MyInterest model
    interests = MyInterest.objects.all().order_by('name')
    # Set the number of items per page
    items_per_page=10
    # Get the current page from the request's GET parameter
    page_number = request.GET.get('page',1)
    current_page,paginator = pagination_function(interests,items_per_page,page_number)
    # Convert queryset to a list of dictionaries 
    # (each instance is represented as a dictionary)
    interests_list = [{'id':interest.id,
                       'name': interest.name, 
                       'interest': interest.interest
                       } for interest in current_page.object_list]

    # Return the result as JSON
    return JsonResponse({'count': paginator.count, 
                         'interests': interests_list, 
                         'current_page': current_page.number, 
                         'total_pages': paginator.num_pages
                         }, 
                         safe=False)



@require_http_methods(['POST'])
@csrf_exempt
def add_interests(request):
    logger.info("start add_interest function")

    # Parse JSON data from the request body
    json_data = json.loads(request.body.decode('utf-8'))
    
    # Get the name and interest from the parsed JSON data
    name = json_data.get('name', '')
    interest = json_data.get('interest', '')

    logger.info("name: {0}\ninterest: {1}".format(name, interest))

    # Validate input data
    validation_result, is_valid = validate_input(name, interest)
    
    if not is_valid:
        return JsonResponse(validation_result, status=400)

    try:
        # Check if the name already exists
        validation_result, is_valid = check_existing_name(name)
        if not is_valid:
            return JsonResponse(validation_result, status=400)

        # Create an instance of MyInterest model
        new_interest = MyInterest(name=name, interest=interest)

        # Save the instance to the database
        new_interest.save()

        logger.info("end add_interest function")
        return JsonResponse({'message': 'Interest added successfully'}, status=201)
    except Exception as e:
        # Return an error response if something goes wrong
        logger.error("add_interest function", str(e))
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["PUT"])
@csrf_exempt
def delete_interests(request):
    logger.info("delete_interests")
