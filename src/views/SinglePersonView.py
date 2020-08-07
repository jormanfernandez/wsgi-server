from src.views.BaseView import BaseView
from src.util.Request import Request

class SinglePersonView(BaseView):
  def get(self, request: Request, name: str):
    self.statusCode = self.HTTPStatusCodes.OK
    self.body = {
      "data": f"Hey!!! So you are {name}"
    }
  
  def post(self, request: Request, name: str):
    self.statusCode = self.HTTPStatusCodes.OK
    reqBody = request.jsonBody()
    self.body = {
      "data": f"Hey!!! My name is {name}. You are {reqBody['name']}, right?"
    }
