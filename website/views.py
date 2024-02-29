from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from rest_framework import serializers
from .models import Record ,MyInterest,MyImages
from rest_framework import generics
from .serializers import MyModelSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .auxillaryFunctions import *
import json
from logs.logging_config import logger
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from .error_codes import ErrorCodes
import re
from dotenv import load_dotenv
import os
load_dotenv()
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
        return JsonResponse({'status':'success','message': 'Interest added successfully'}, status=201)
    except Exception as e:
        # Return an error response if something goes wrong
        logger.error("add_interest function", str(e))
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(['POST'])
@csrf_exempt
def image_upload(request):
    logger.info("Image Upload")    
    try:
        m_name = request.POST.get('name','')
        m_image =request.FILES.get('image','')
        print({'name':m_name,'image':m_image})
        logger.info({'name':m_name,'image':m_image})
        new_my_images=MyImages(name=m_name,image=m_image)
        new_my_images.save()
        return JsonResponse({'success':'data succesfully added'},status=200)
    except Exception as e:
        return JsonResponse({'error':e},status=500)
    

@require_http_methods(['POST'])
@csrf_exempt
def tell_time(request):
    logger.info('Tell Time')
    time = timezone.now()
    return JsonResponse({'time':time})


@require_http_methods(['GET'])
def show_image(request):
    logger.info('show_image function')
    json_request=request.body.decode('utf-8')
    json_data=json.loads(json_request)
    image_id=json_data.get('id',0)
    logger.info({'image_id\t':image_id})
    try:
        validation_result,is_valid=validate_id(image_id)
        if not is_valid:
            return JsonResponse(validation_result,status=400)
        new_my_images = MyImages.objects.filter(id=image_id).first()
        print('no problem here')
        if not new_my_images:
            return JsonResponse(ErrorCodes.name_interest['INVALID_ID'])
        image_data={
            'id':new_my_images.id,
            'name':new_my_images.name,
            'image':new_my_images.image.url
        }
        return JsonResponse({'status':'success','image':image_data},encoder=DjangoJSONEncoder)
    except Exception as e:
        return JsonResponse({'error':e},status=500)
    

@require_http_methods(['POST'])
@csrf_exempt
def add_user(request):
    logger.info('add_user')
    phone_number_pattern = os.getenv("PHONE_NUMBER_PATTERN")
    
    try:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        validating_emails(email)
        if(len(first_name)>50 or len(first_name)<2 or len(last_name)>50 or len(last_name)<2):
            return JsonResponse(ErrorCodes.registration["NAME_SIZE"],status=400)
        if(not re.match(phone_number_pattern,phone)):
            return JsonResponse(ErrorCodes.registration["INVALID_PHONE_NUMBER"])
        new_record = Record(first_name=first_name,last_name=last_name,phone=phone)
        new_record.save()
        logger.info("new user {0} added".format(first_name))
        return JsonResponse({"status":"success","message":"{0} added succesfully".format(first_name)},status=201)
    except Exception as e:
        logger.error("add_user ",str(e))
        return JsonResponse({"error":str(e)},status=500)