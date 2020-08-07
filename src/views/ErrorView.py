from src.views.BaseView import BaseView
from src.util.Request import Request

class ErrorView(BaseView):
  def handle(self, request: Request, errors: any) -> tuple:
    self.statusCode = self.HTTPStatusCodes.BAD_REQUEST

    self.body = {
      "message": "There has been an error in your request"
    }
    self.body.update(self.extractErrors(errors))
    return self.serialize()

  def extractErrors(self, errors: any) -> dict:
    return {"error": e}
