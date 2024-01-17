from logs.logging_config import logger
from .error_codes import ErrorCodes
from .models import MyInterest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math

def validate_input(name, interest):
    logger.info("start validate_input function")
    # Validate input data
    if not name:
        logger.error("validate_input function")
        return ErrorCodes.name_interest["NAME_EMPTY"], False

    if not interest:
        logger.error("validate_input function")
        return ErrorCodes.name_interest["INTEREST_EMPTY"], False

    if len(name) > 50:
        logger.error("validate_input function")
        return ErrorCodes.name_interest["NAME_SIZE_UPPER_LIMIT"], False

    if len(interest) > 100:
        logger.error("validate_input function")
        return ErrorCodes.name_interest["INTEREST_SIZE_UPPER_LIMIT"], False
    
    logger.info("end validate_input function")
    return None, True


def check_existing_name(name):
    logger.info("check_existing_name")
    if MyInterest.objects.filter(name=name).exists():
        return ErrorCodes.name_interest["NAME_EXISTS"], False
    return None, True


def pagination_function(objects,items_per_page,page_number):
    # create paginator instance
    paginator = Paginator(objects,items_per_page)

    try:
        # Get the page object for the current page
        current_page = paginator.page(page_number)
        return current_page,paginator
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        return paginator.page(1),paginator
    except EmptyPage:
        # If the requested page is out of range, return an empty list
        return paginator.page(1),paginator

def validate_id(id):
    try:
        id = int(id)
        if id < 1:
            return ErrorCodes.name_interest["INVALID_ID"], False
        return None, True
    except ValueError:
        return ErrorCodes.name_interest["INVALID_ID"], False
