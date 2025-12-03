from fastapi import FastAPI, UploadFile, Request
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import firebase_handler
import json



load_dotenv()
firebase_handler.init_firebase()
app = FastAPI()

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)  #get the dot env from mostafa

@app.post("/caption")
async def caption_image(request: Request):
    image_bytes = await request.body()
    
    if not image_bytes:
        return {"status": "error", "message": "No image data"}
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg",
            ),
            """this is an image inside a blood bank, count the number of 
            the blood sacs, and only respond with the number
            """
        ]
    )
    print(response)
    # clean_text = response.text.replace("```json", "").replace("```", "").strip()
    # print(f"Gemini Result: {clean_text}")
        
    # analysis_data = json.loads(clean_text)

    number = response.candidates[0].content.parts[0].text.strip()
    firebase_handler.update_inventory({"bloodBags": int(number)})


    return {"status": "success", "data": response}
