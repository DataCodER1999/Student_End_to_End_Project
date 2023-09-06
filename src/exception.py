# Sys Liabrary provides various functions and variables that are used to manipulate different parts of the python runtime
import sys
import logging

def get_error_message(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno,error    
        )

    return error_message
    

class CustomException(Exception):

    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_detail=error_details)

    
    def __str__(self):
        return self.error_message
    

if __name__ == '__main__':
    try:
        print(5/0)
    
    except Exception as e:
        logging.info("Division by zero")
        raise CustomException(e,sys)