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
        "INVALID_EMAIL":generate_error_message("3002","Invalid Email id")
    }