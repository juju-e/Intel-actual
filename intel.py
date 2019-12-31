import requests
from termcolor import colored
def get_status_code(res):
   if res.status_code != 404:
      return True
   else:
      return False
def on_github(username):
   res=requests.get("http://www.github.com/"+str(username))
   if get_status_code(res):
        return "user Present on github"
   else:
       return ""
def on_tumblr(username):
    res=requests.get("https://"+str(username)+".tumblr.com")
    if get_status_code(res):
        return "User present on Tumblr"
    else:
        return ""
def on_dev_dot_to(username):
   res=requests.get("https://dev.to/"+str(username))
   if get_status_code(res):
        return "user present on dev.to"
   else:
        return ""

def main():
 username=input(colored("[*]please enter theu sername you want to search for-->","green"))
 print(colored(on_github(username),"yellow"))
 print(colored(on_tumblr(username),"yellow"))
 print(colored(on_dev_dot_to(username),"yellow"))



main()
