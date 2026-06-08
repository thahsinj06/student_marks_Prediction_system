import sys # it is used for the script to access command line interface 
from src.logger import logging
def error_message(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_info="error occured in py script [{0}] line number [{1}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    return error_info
    

class CustomException(Exception):
    def __init__(self,error_info,error_detail:sys):
        super().__init__(error_info)
        self.error_info=error_message(error_info,error_detail=error_detail)
    def __str__(self):
        return self.error_info
