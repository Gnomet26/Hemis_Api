from flask import Flask,request,jsonify
from Hemis import Hemis

class WebApi(Flask):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.add_url_rule('/HemisApi/v1/','base_url',self.get_params,methods=['POST'])

    def get_params(self):

        data = request.json
        h = Hemis(data["base_url"],data["root_ld"],data["root_password"],data["day"])

        return jsonify(condition = h.get_condition(),result = h.get_result()),443

if __name__ == "__main__":
    app = WebApi(__name__)
    app.run(debug=True)