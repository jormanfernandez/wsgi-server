from src.views.BaseView import BaseView
from src.util.Request import Request

class NotFoundView(BaseView):
  def handle(self, request: Request, **kwargs) -> tuple:
    self.statusCode = self.HTTPStatusCodes.NOT_FOUND

    self.body = {
      "error": "Not Found"
    }
    return self.serialize()
