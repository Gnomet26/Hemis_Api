from bs4 import ResultSet

class Personal_Data:

    def __init__(self,data: ResultSet):
        
        self.result = {}
        for i in data.find_all("tr"):
            self.result[str(i.find("th").text).replace("\"","`")] = str(i.find("td").text).replace("\"","`")
                    
    def get(self):
        return self.result