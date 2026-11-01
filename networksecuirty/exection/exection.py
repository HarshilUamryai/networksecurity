import logging
import os 
import sys
from networksecuirty.logging.Logger import logging
class execution:
    def __init__(self,error_message,error_dealits:sys):
        self.error_message = error_message
        _,_,exc_tb = sys.exc_info()
        self.error_line = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return f"Error Message: {self.error_message}, Error Line: {self.error_line}, File Name: {self.file_name}"
        self.file_name,self.error_line,str(self.error_message)

if __name__ == "__main__":
    try:
        logging.info("This is an info message.")
    except Exception as e:
        raise execution(str(e),sys)
       