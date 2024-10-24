
class Get:
    def __init__(self,data):

        self.int_d = ""
        self.str_d = ""

        for i in data:
            try:
                self.int_d += str(int(i))
            except:
                self.str_d += str(i)

    def str_(self):
        return self.str_d

    def int_(self):
        return self.int_d