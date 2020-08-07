from types import FunctionType
from cgi import parse_qs
from src.routes.Router import Router
from src.util.Request import Request
from src.managers.ResponseManager import ResponseManager

class RequestManager:
  """
  Class to handle every request to the server
  """

  router = Router()

  @staticmethod
  def process(environ: dict, start_response: FunctionType) -> list:
    """
    Process every request looking in the router and passing the returned data to the response manager

    Args:
      environ (dict): Enviroment variable with all the request data
      start_response (function): Function to setup the status code and response headers
    
    Returns:
      bytes: Byte sequence to be handled in the main layer
    """
    request = Request(environ)
    status, headers, body = RequestManager.router.go(request)
    return ResponseManager.response(start_response, body, status, headers)
