from src.views.HomeView import HomeView
from src.views.UserPetView import UserPetView
from src.views.SinglePersonView import SinglePersonView

urls = {
  "/": HomeView,
  "/person/<str:name>": SinglePersonView,
  "/user/<str:username>/<str:petType>/<str:petName>": UserPetView,
}
"""
URLS to be matched on every request indicating the handler to every one.
"""
