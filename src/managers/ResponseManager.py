from types import FunctionType

class ResponseManager:
  """
  Class to process the response mechanism to the client
  """

  CORS = [
    "127.0.0.1",
  ]

  @staticmethod
  def response(start_response: FunctionType, body: any, statusCode: str, headers: dict) -> list:
    """
    Detects which headers to setup and which body to send

    Args:
      start_response (function): Function to set the response header and the response status code
      body (any): Response Body to be send
      statusCode (str): Status Code to be added to the start_response function
      headers (dict): Headers to be added in the start_response function
    
    Returns:
      list: bytes-like list with the body information
    """
    responseHeaders = ResponseManager.buildHeaders(headers)
    start_response(statusCode, responseHeaders)
    return [body.encode(encoding="utf-8")]
  
  @staticmethod
  def buildHeaders(headers: dict) -> list:
    """
    Using a main header as base, it returns the list of headers as wsgi uses in the response status
    
    Args:
      headers (dict): key-value dictionary with the header name and its value
    
    Returns:
      list: list<tuple> with the headers being used
    """
    MAIN_HEADERS = {
      "Content-Type": "application/json",
      "Server": f"WSGI {ResponseManager.CORS[0]}",
      "Access-Control-Allow-Origin": ", ".join(ResponseManager.CORS)
    }
    if headers is not None:
      MAIN_HEADERS.update(headers)
    return [(header, MAIN_HEADERS[header]) for header in MAIN_HEADERS]
