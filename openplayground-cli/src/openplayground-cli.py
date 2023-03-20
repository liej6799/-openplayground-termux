import openplayground
import dotenv
import os
import sys
import tempfile

token_name = "OPENPLAYGROUND_TOKEN"

temp = tempfile.gettempdir() + "/openplayground.env"

if (dotenv.load_dotenv(temp) == False):
  open(temp, "a+")
    
auth = openplayground.Auth()

print("-----------------------")
print("openplayground-cli")
print("CLI app for OpenPlayground utilizing openplayground-api")
print("-----------------------")
if os.environ.get(token_name) is None:
  # TODO : check is token valid
  print("there is no token, preparing to authenticate...")
  auth.login_part_1(input("Please enter openplayground's email: \n"))
  os.environ[token_name] = auth.login_part_2(input("enter otp key: \n"))
  dotenv.set_key(temp, token_name, os.environ[token_name])

client = openplayground.Client(os.environ[token_name])

print("Select the models list: \n")
for models in client.get_models():
  print(models)

# prompt = "Summarize the GNU GPL v3."
# for chunk in client.generate("openai:gpt-4", prompt, maximum_length=1000):
#   if chunk["event"] == "infer":
#     print(chunk["message"], end="", flush=True)
    