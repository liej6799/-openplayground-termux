import openplayground
import dotenv
import os
import sys

token_name = "OPENPLAYGROUND_TOKEN"
email_name = "OPENPLAYGROUND_EMAIL"

dotenv_file = dotenv.find_dotenv()

if (dotenv.load_dotenv(dotenv_file) == False):
  open(".env", "a+")
    
auth = openplayground.Auth()

print("openplayground-cli")
print("-----------------------")
print("openplayground-cli")
print("CLI app for OpenPlayground utilizing openplayground-api")
print("-----------------------")
if os.environ.get(email_name) is None:
	os.environ[email_name] = input("Please enter openplayground's email: \n")
	dotenv.set_key(dotenv_file, email_name, os.environ[email_name])
  
if os.environ.get(token_name) is None:
  print("there is no token, preparing to authenticate...")
  auth.login_part_1(os.environ[email_name])
  os.environ[token_name] = auth.login_part_2(input("enter otp key: \n"))
  dotenv.set_key(dotenv_file, token_name, os.environ[token_name])

client = openplayground.Client(os.environ[token_name])

print("Select the models list: \n")
for models in client.get_models():
  print(models)

# prompt = "Summarize the GNU GPL v3."
# for chunk in client.generate("openai:gpt-4", prompt, maximum_length=1000):
#   if chunk["event"] == "infer":
#     print(chunk["message"], end="", flush=True)
