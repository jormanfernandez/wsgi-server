from http import HTTPStatus
from json import dumps as jsonDump
from src.util.Request import Request
from src.exceptions.NotFoundException import NotFoundException

class BaseView:
  """
  Base handler for each request done to the server
  """

  ALL_METHODS = [
    "head",
    "options",
    "get",
    "post",
    "patch",
    "put",
    "delete"
  ]

  headers = {}
  HTTPStatusCodes = HTTPStatus
  statusCode = None
  body = None

  @property
  def allowedMethods(self) -> list:
    """
    Returns the allowed request method for the view

    Returns:
      list
    """
    allowedMethods = []

    for method in self.ALL_METHODS:
      if hasattr(self, method):
        allowedMethods.append(method.upper())

    return allowedMethods


  def handle(self, request: Request, **kwargs) -> tuple:
    """
    Handles the method request done to a specific uri. If it does not have the method, it will throw a NotFoundException

    Args:
      request (Request): Request sent to the server
      kwargs
    
    Returns:
      tuple: statusCode, headers and body
    """
    self.headers.update({
      "Access-Control-Allow-Methods": ", ".join(self.allowedMethods)
    })
    method = request.method.lower()
    if method in self.ALL_METHODS and hasattr(self, method):
      getattr(self, method)(request, **kwargs)
      return self.serialize()
    else:
      raise NotFoundException()
  
  def options(self, request: Request, **kwargs):
    self.statusCode = self.HTTPStatusCodes.OK
  
  def setHeader(self, header: str, value: any):
    """
    Can set a response header to the handler

    Args:
      header (str): Header name to be modified
      value (any): Value of the header
    """
    self.headers[header] = value
  
  def setHeaders(self, headers: dict):
    """
    Updates the header's list

    Args:
      headers (dict): key-value dict with the headers
    """
    self.headers.update(headers)

  def serialize(self) -> tuple:
    """
    Returns a serialized tuple to setup the response process
    This can vary depending on the need

    Returns:
      tuple: statusCode(str), headers(dict), body(any)
    """
    statusCode = self.getStatusCode()
    body = self.getBody()
    
    return statusCode, self.headers, body
  
  def getStatusCode(self) -> str:
    """
    Based on the defined status code from the HTTPStatus, it will read the value and phrase from it
    to returned

    Returns:
      str
    """
    if self.statusCode is None:
      self.statusCode = self.HTTPStatusCodes.NOT_FOUND
    return f"{self.statusCode.value} {self.statusCode.phrase}"

  def getBody(self) -> any:
    """
    It returns a value that was set in the body

    Returns:
      any
    """
    try:
      return jsonDump(self.body) if self.body is not None else ""
    except:
      return self.body
