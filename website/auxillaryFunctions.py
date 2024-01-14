from logs.logging_config import logger
from .error_codes import ErrorCodes
from .models import MyInterest

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
    if MyInterest.objects.filter(name=name).exists():
        return ErrorCodes.name_interest["NAME_EXISTS"], False
    return None, True
