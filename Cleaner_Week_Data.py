from bs4 import ResultSet
from C_Helper_Week import C_Week

class Week_Data:

    def __init__(self,data: ResultSet):
        
        self.result = {}
            
        f1 = data.find_all("option")
            
        for i in f1:
            if i["value"] != "":
                self.result[str(i.text).replace(" ","")] = str(i["value"])

        clear_week = C_Week(self.result)
        self.result = clear_week.get()
    
    def get(self):
        return self.result