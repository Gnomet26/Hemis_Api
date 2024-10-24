import requests
from bs4 import BeautifulSoup,ResultSet
from marshrutizator import Marshrut
from Cleaner_Week_Data import Week_Data
from Analiz_Week_Id import Analiz_Week
from Clear_Time_Table import C_Table
from Time_Zona import Uzb_time_zona

class Hemis:
    def __init__(self,base_url,root_id,root_password,day):

        self.semester_data: ResultSet
        self.personal_data:ResultSet
        self.week_data:ResultSet

        self.result = None
        self.condition = None
        self.init_parsing(base_url,root_id,root_password,day)

    def init_parsing(self,base_url,root_id,root_password,day):
        try:
            self.date = Uzb_time_zona()
            with requests.Session() as sessiya:

                r1 = sessiya.get(url=f"{base_url}dashboard/login")
                csrf_token = BeautifulSoup(r1.text,"html.parser").find_all("meta")[4]["content"]

                try:
                    request_data = {
                        "_csrf-frontend": str(csrf_token),
                        "FormStudentLogin[login]": root_id,
                        "FormStudentLogin[password]": root_password
                    }

                    r2 = sessiya.post(url=f"{base_url}dashboard/login",data=request_data)
                    semester_list = BeautifulSoup(r2.text,"html.parser")
                    r3 = sessiya.get(url=f"{base_url}student/personal-data")
                    personal_list = BeautifulSoup(r3.text,"html.parser")

                    self.semester_data = semester_list
                    self.personal_data = personal_list
                
                    try:
                        semseter = Marshrut(self.semester_data,self.personal_data)
                        semester_id = semseter.get_personal_attr("Semestr")
                        r4 = sessiya.get(url=f"{base_url}education/time-table?semester={semester_id}")
                        week_list = BeautifulSoup(r4.text,"html.parser")
                        week_data = week_list

                        clear_week = Week_Data(week_data)
                        aw = Analiz_Week(clear_week.get(),self.date.sana("kun"),self.date.sana("oy"))
                        week_id = aw.get()
                        r5 = sessiya.get(url=f"{base_url}education/time-table?semester={semester_id}&week={week_id}")
                        end_result = BeautifulSoup(r5.text,"html.parser")
                        s = C_Table(end_result)
                        
                        if day == "today":
                            self.result = s.get_data()[self.date.hafta()]

                        elif day == "tomorrow":
                            self.result = s.get_data()[self.date.hafta2()]

                        elif day == "all":
                            self.result = s.get_data()

                        sessiya.close()

                    except:
                        self.condition = "Marshrut error"
                
                    self.condition = "Parsing succes closed :) ..."

                except:
                    self.condition = "login error"
        except:
            self.condition = "connection error"
    
    def get_result(self):

        return self.result
    
    def get_condition(self):

        return self.condition