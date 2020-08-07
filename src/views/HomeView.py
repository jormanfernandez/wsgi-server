from src.views.BaseView import BaseView
from src.util.Request import Request

class HomeView(BaseView):
  def get(self, request: Request):
    self.statusCode = self.HTTPStatusCodes.OK
    self.body = {
      "data": "Hi!"
    }
