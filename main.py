from fastapi import FastAPI, UploadFile, File
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)  #get the dot env from mostafa

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type=file.content_type or "image/jpeg",
            ),
            """this is an image inside a blood bank, count the number of 
            the blood sacs, the number of the sacs for each blood type
            in this image and return the output formatted like this
            {
                "number_of_blood_sacs"= int,
                "A+"=int,
                "A-"=int,
                "b+"=int,
                "b-"=int,
                "o+"=int,
                "o-"=int,
                "ab+"=int,
                "ab-"=int,    
                "could_not_detect_type"=int            
            }
            """
        ]
    )
    return {"caption": response.text}
