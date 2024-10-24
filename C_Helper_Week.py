import re
import json

class C_Week:

    def __init__(self,data):
        
        self.result = {}
        json_data = json.loads(str(data).replace("\'","\""))

        keys = list(json_data.keys())
        values = list(json_data.values())
        n = 0
        for i in keys:
            self.result[str(self.clean_formator(i))] = values[n]
            n += 1

    def clean_formator(self,input_data):
        months = {
            "sentabr": "09",
            "oktabr": "10",
            "noyabr": "11",
            "dekabr": "12",
            "yanvar": "01",
            "fevral": "02",
            "mart": "03",
            "aprel": "04",
            "may": "05",
            "iyun": "06",
            "iyul": "07",
            "avgust": "08"
        }

        pattern = r'(\d{1,3}\.\s*|\d{1,2}(?:sentabr|oktabr|noyabr|dekabr|yanvar|fevral|mart|aprel|may|iyun|iyul|avgust)/|\d{1,2}(?:sentabr|oktabr|noyabr|dekabr|yanvar|fevral|mart|aprel|may|iyun|iyul|avgust))'
        matches = re.findall(pattern, input_data)

        result = []
        
        for match in matches:
        
            for month_name, month_number in months.items():
                if month_name in match:
                    day = match[:2] 
                    result.append(f"{int(day)} {int(month_number)}")

        return " ".join(result).split()
    
    def get(self):

        return self.result