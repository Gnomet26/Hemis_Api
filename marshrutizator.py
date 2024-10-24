from bs4 import ResultSet
from Cleaner_Semester_Data import Semester_Data
from Cleaner_Personal_Data import Personal_Data
from Get import Get

class Marshrut:
    def __init__(self,semester_data: ResultSet ,personal_data: ResultSet):

        self.semester = Semester_Data(semester_data)
        self.personal = Personal_Data(personal_data)
        
    def get_personal_attr(self,key_):
        
        if key_ == "Semestr":
            a = Get(self.personal.get()["Semestr"]).int_()
            return self.semester.get()[str(a)]