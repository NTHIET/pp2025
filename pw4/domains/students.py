class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.__id = student_id
        self.__name = student_name
        self.__dob = student_dob
        
    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def __str__(self): return f"{self.__name} (ID:{self.__id}, DoB:{self.__dob})"