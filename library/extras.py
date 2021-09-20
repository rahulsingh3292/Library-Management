from django.core.mail import send_mail
from django.conf import settings 
from base64 import b64encode

def encode_email(email):
  coded= email.encode("utf-8")
  encoded = b64encode(coded)
  return encoded.decode("utf-8")
  
  
def registration_success(email):
  from_mail = settings.EMAIL_HOST_USER
  body = f"Your Book-Library Account is Created successfully. please Activate account your Account -  https://blogprojectbyrahul.herokuapp.com/accounts/activate?email={encode_email(email)}"
  subject = "Account Activation"
  return send_mail(subject,body,from_mail,[email])

def admin_account_activated(email, name):
  from_mail = settings.EMAIL_HOST_USER
  body = f"Hey {name} Your Admin Account is Activated. you can add,edit books in library.."
  subject = "Library Admin Account"
  return send_mail(subject,body,from_mail,[email])
  
def account_activated(email,name):
  from_mail = settings.EMAIL_HOST_USER
  body = f"Hey {name} Your Account is Activated. You can login now."
  subject = "Account Activated"
  return send_mail(subject,body,from_mail,[email])

def borrow_success(email,name,book):
  from_mail = settings.EMAIL_HOST_USER
  body = f"Hey {name} Book '{book}' is Added in your List. Plaese return book in few days. https://blogprojectbyrahul.herokuapp.com/Library/my_books/"
  subject = "Borrow Book Success"
  return send_mail(subject,body,from_mail,[email])

  