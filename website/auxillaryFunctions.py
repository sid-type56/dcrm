from .error_codes import ErrorCodes

def validate_input(name, interest):
    # Validate input data
    if not name:
        return ErrorCodes.name_interest["NAME_EMPTY"], False

    if not interest:
        return ErrorCodes.name_interest["INTEREST_EMPTY"], False

    if len(name) > 50:
        return ErrorCodes.name_interest["NAME_SIZE_UPPER_LIMIT"], False

    if len(interest) > 100:
        return ErrorCodes.name_interest["INTEREST_SIZE_UPPER_LIMIT"], False

    return None, True
