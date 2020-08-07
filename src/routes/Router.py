from src.managers.PathManager import PathManager
from src.exceptions.NotFoundException import NotFoundException
from src.views.NotFoundView import NotFoundView
from src.views.ErrorView import ErrorView
from src.routes.urls import urls
from src.util.Request import Request

class Router:
  """
  Router class which will detect what handler to use
  """

  path = PathManager(urls)
  
  def go(self, request: Request) -> tuple:
    """
    Function to execute a specific handler based on a request

    Args:
      request (Request): Request from the client
    
    Returns:
      tuple: 3 parts tuple with status code, headers and body
    """
    handler, kwargs = self.path.extractHandler(request.uri)
    try:
      if handler is None:
        raise NotFoundException
      
      return handler.handle(request, **kwargs)
    except NotFoundException as e:
      return NotFoundView().handle(request)
    except BaseException as e:
      return ErrorView().handle(request, e)
