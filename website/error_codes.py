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
        "NAME_EXISTS":generate_error_message("2004","name already exists")
    }