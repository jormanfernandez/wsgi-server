from re import search

class PathManager:
  def __init__(self, paths):
    self.paths = paths

  def extractHandler(self, requestPath: str) -> tuple:
    """
    Extracts which handler from the paths should be used
    and the arguments to be send in that handler acording to the route structure

    Returns:
      tuple: handler (function), kwargs (dict)
    """
    index, kwargs = self.getMatchs(requestPath)
    handler = self.paths[index]() if index is not None else None
    return handler, kwargs
  
  def getMatchs(self, path: str) -> tuple:
    """
    It get the index of the path if it matchs and the keyword arguments to be passed based on the url that it matches

    Args:
      path (str): request path to be compared
    
    Returns:
      tuple: index(str), kwargs(dict) The index is the key index in the paths attribute of the instance
    """
    index = None
    kwargs = {}

    requestPathSplited = path.rstrip("/").split("?")[0].split("/")[1:]

    for route in self.paths:
      routeSplited = route.rstrip("/").split("/")[1:]

      if len(requestPathSplited) != len(routeSplited):
        continue

      if ":" in route:
        isValid, matchs = self.getKwargs(routeSplited, requestPathSplited)
        if isValid:
          kwargs.update(matchs)
          index = route
          break
      elif requestPathSplited == routeSplited:
        index = route
        break

    return index, kwargs
  
  def getKwargs(self, route: list, requestPath: list) -> tuple:
    """
    If the url has variables defined as /<str:name> in it. It will extract those and put it in a dict returning this values
    and if the values in the url are invalid it will return False as firts value in the tuple

    Args:
      route (list): Route to be compared against the request
      requestPath (list): URI from the Request to be compared
    
    Returns:
      tuple: isValid(bool), matchs(dict)
    """
    matchs = {}
    isValid = True
    regex = "(\<[a-zA-Z]{3}:[a-zA-Z]{1,}\>)"

    for part in range(len(route)):
      if search(regex, route[part]) is not None:
        """
        If based on the regex this part in the route matches, it means its a variable and the data should be extracted
        """
        varType = route[part][1:4]
        """
        First three letters are the variable's type to be compared
        """
        varName = route[part][5:-1]
        """
        The rest is the variable's name
        """
        varData = self.getData(requestPath[part], varType)
        
        if varData is None:
          matchs = {}
          isValid = False
          break
        
        matchs[varName] = varData

      elif requestPath[part] != route[part]:
        matchs = {}
        isValid = False
        break

    return isValid, matchs
  
  def getData(self, varData: any, dataType: str) -> any:
    """
    Depending on the dataType passed, it will check if it matches with the data. If it doesn't it will return None

    Args:
      varData (any): Data to be checked
      dataType (str): For now, only can be checked int and str. Anything else will return None
    
    Returns:
      any: None if the data does not match the type, else the data sended in varData
    """
    data = None
    try:
      if dataType == "int" and search("[1-9]{1,}", varData) is not None:
        data = int(varData)
      elif dataType == "str" and search("[\w]{1,}", varData) is not None:
        data = str(varData)
    except BaseException as e:
      print(e)
    return data
