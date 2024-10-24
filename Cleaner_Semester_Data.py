from bs4 import ResultSet
from C_Helper_Semester import C_Semester

class Semester_Data:

    def __init__(self,data: ResultSet):
        
        self.result = {}
        f1 = data.find("ul",class_ = "pagination")
        f2 = f1.find_all("a")   
        for i in f2:
            self.result[str(i.text)] = str(i["href"])
        
        json_data = C_Semester(self.result).get()
        self.result = json_data

    def get(self):
        return self.result