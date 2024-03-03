class ErrorCodes:

    @staticmethod
    def generate_error_message(code,message):
        return {
                "status":"error",
                "code":code,
                "message":message
                }

    name_interest={
        "NAME_SIZE_UPPER_LIMIT":generate_error_message("2000"," Name should not exceed 100 characters"),
        "INTEREST_SIZE_UPPER_LIMIT":generate_error_message("2001"," Interest should not exceed 100 characters"),
        "NAME_EMPTY":generate_error_message("2002"," name cannot be empty"),
        "INTEREST_EMPTY":generate_error_message("2003","interest cannot be empty"),
        "NAME_EXISTS":generate_error_message("2004","name already exists"),
        "INVALID_ID":generate_error_message("2005","invalid id")
    }

    registration={
        "NAME_SIZE":generate_error_message("3000","Names should be in the limit 2-50 characters"),
        "INVALID_PHONE_NUMBER":generate_error_message("3001","Invalid phone number"),
        "INVALID_EMAIL":generate_error_message("3002","Invalid Email id"),
        "EMAIL_ALREADY_EXISTS":generate_error_message("3003","Email already exists"),
        "MISSING_EMAIL":generate_error_message("3004","Email is required"),
        "MISSING_BASIC_PERSONAL_INFO":generate_error_message("3005","First name, Last name, Email and Password are required"),
        "INVALID_PASSWORD":generate_error_message("3006","password require atlest 1 alphabet , 1 digit, length between 8-128 and should contain special characters")
    }

    unexpected_errors={
        "UNKNOWN_ERROR":generate_error_message("1000","Unknown Error")
    }