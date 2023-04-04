class MyError(Exception):
    def __str__(self):
       return "myerror가 발생하였습니다."