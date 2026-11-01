import logging
import os 
import sys
from networksecuirty.logging.Logger import logging
class execution(Exception):
    #this class is used to handle exceptions and log them to a file
    def __init__(self,error_message,error_dealits:sys):
        super().__init__(error_message)
        #this method is used to initialize the class and set the error message, error line and file name
        self.error_message = error_message
        #this method is used to get the error line and file name from the sys module
        _,_,exc_tb = sys.exc_info()
        #this method is used to get the error line and file name from the sys module
        self.error_line = exc_tb.tb_lineno
        #this method is used to get the error line and file name from the sys module
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        #this method is used to log the error message, error line and file name to a file


    def __str__(self):
        #this method is used to return the error message, error line and file name as a string
        return f"Error Message: {self.error_message}, Error Line: {self.error_line}, File Name: {self.file_name}"
        #this method is used to log the error message, error line and file name to a file
        self.file_name,self.error_line,str(self.error_message)
        #this method is used to log the error message, error line and file name to a file

if __name__ == "__main__":
    try:
        logging.info("This is an info message.")
    except Exception as e:
        raise execution(str(e),sys)
       