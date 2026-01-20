class Course:
    def __init__(self, course_id, course_name, course_credits):
        self.__id = course_id
        self.__name = course_name
        self.__credits = course_credits
        
    def get_id(self): return self.__id
    def get_credits(self): return self.__credits
    def __str__(self): return f"{self.__name} ({self.__id})"