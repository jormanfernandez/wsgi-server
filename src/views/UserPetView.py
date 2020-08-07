from src.views.BaseView import BaseView
from src.util.Request import Request

class UserPetView(BaseView):
  def get(self, request: Request, username: str, petType: str, petName: str):
    self.statusCode = self.HTTPStatusCodes.OK
    self.body = {
      "data": f"Hi {username}. How's your {petType}? I'm sure {petName} is really awesome!"
    }
