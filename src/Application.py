from types import FunctionType
from src.managers.RequestManager import RequestManager

class Application:
  def __call__(self, environ: dict, start_response: FunctionType) -> tuple:
    """
    Method to be called when make_server function starts

    Args:
      environ (dict): Enviroment variable with all the request data
      start_response (function): Function to setup the status code and response headers
    
    Returns:
      bytes: Byte sequence to be handled in the main layer
    """
    return RequestManager.process(environ, start_response)
