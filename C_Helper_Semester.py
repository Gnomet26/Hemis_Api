import json

class C_Semester:

    def __init__(self,data):

        self.result = {}

        a = json.loads(str(data).replace("\'","\""))
        keys = list(a.keys())
        values = list(a.values())

        for i in range(len(a.keys())):
            if self.get_number(values[i]) != None:
                self.result[str(keys[i])] = self.get_number(values[i])

    def get_number(self,input_d:str):

        if "".join(filter(str.isdigit, input_d)) != "":

            return "".join(filter(str.isdigit, input_d))
        else:
            return None
        
    def get(self):
        return self.result 