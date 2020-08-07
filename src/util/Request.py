from cgi import parse_qs
from json import loads as jsonLoads

class Request:
  """
  Holding the environ variable used in the particular request to return in a more legible way the data inside of it
  """
  def __init__(self, environ: dict):
    self.__environ = environ
  
  @property
  def uri(self) -> str:
    """
    URI requested by the client
    """
    return self.__environ.get("PATH_INFO", "")
  
  @property
  def method(self) -> str:
    """
    Request method used by the client
    """
    return self.__environ.get("REQUEST_METHOD", "")
  
  @property
  def headers(self) -> dict:
    """
    Returns the headers located in the request. All the headers set by the client have the preffix HTTP_
    So this property returns those headers
    """
    HEADER_PREFFIX = "HTTP_"
    headers = {}

    for header in self.__environ:
      if header.startswith(HEADER_PREFFIX) is False:
        continue
      headerName = header[len(HEADER_PREFFIX):]
      headers[headerName] = self.__environ[header]

    return headers
  
  def __getBody(self) -> str:
    """
    Private method to read the body data from the request

    Returns:
      str: String containing the body data
    """
    try:
        requestBodySize = int(self.__environ.get("CONTENT_LENGTH", 0))
    except (ValueError):
        requestBodySize = 0
    requestBody = self.__environ["wsgi.input"].read(requestBodySize)
    return requestBody
  
  def plainBody(self) -> str:
    """
    Returns the plain body sended to the server

    Returns:
      str
    """
    return self.__getBody()
  
  def jsonBody(self) -> dict:
    """
    It parsed the body as a json if it matches or it will throw an error

    Returns:
      dict
    """
    requestBody = self.__getBody()
    return jsonLoads(requestBody)
