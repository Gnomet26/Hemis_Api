import json
import ast

class Analiz_Week:

    def __init__(self,data,day,month):

        self.result = {}
        keys = []
        values = []
        json_result = json.loads(str(data).replace("\'",""))

        for i in list(json_result.keys()):
            keys.append(ast.literal_eval(i))
        
        for i in list(json_result.values()):
            values.append(i)

        self.result = self.get_week_id(keys,values,day,month)

    def get_week_id(self,keys_,values_,day_,month_):
        
        result = None
        n = 0
        for i in keys_:
            if ((month_ == i[1]) and (month_ == i[3])):
                if(day_ >= i[0] and day_ <= i[2]):
                    result = values_[n]
                    break
    
            elif ((month_ == i[1]) and (month_ == i[3] - 1)):
                if((day_ >= i[0] and (month_ == i[1]) and (day_ > i[2]))):
                    result = values_[n]
                    break 
            elif (month_ == i[3] and month_ == i[1] + 1):
                if (day_ < i[0] and day_ <= i[2]):
                    result = values_[n]
                    break
            n += 1
        
        return result
    
    def get(self):
        return self.result