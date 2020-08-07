from dotenv import load_dotenv
load_dotenv()

from os import getenv
from wsgiref.simple_server import make_server
from src.Application import Application

if __name__ == "__main__":
  port = int(getenv("PORT"))
  host = getenv("HOST")
  app = Application()

  print(f"* * * STARTING AT {host}:{port}")

  try:
    srv = make_server(host, port, app)
    srv.serve_forever()
    """
    The servers keeps listening to any HTTP Request on the `host`:`port` specified
    """
  except:
    print("* * * FINISHING SERVER")
