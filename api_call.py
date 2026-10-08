from google import genai
from dotenv import load_dotenv
import os

#Loading env's
load_dotenv()

my_api_key = os.getenv("GEMINI_API")

#initialize client

client = genai.Client(api_key=my_api_key)


#functions

def debugger(pil_images,option):
    if option=="Hints":
        prompt = """Analyze the given images and if there are bugs and error in codes gives necessary hints to solve the bug/error do not write/re-write code
         solution just only give hints."""
    elif option=="Solution with Code":
        prompt = """Analyze the given images and if there are bugs and error in codes ,at first tell what is the problem then write/re-write the code without error to solve the bug/error and give the code as code format"""

    response = client.models.generate_content(
        model = "gemini-3.5-flash-lite",
        contents=[pil_images,prompt]
    )
    return response.text