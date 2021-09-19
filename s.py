
import base64 

def encode_email(email):
  coded= email.encode("utf-8")
  encode = base64.b64encode(coded)
  return encode.decode("utf-8")

