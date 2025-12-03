# import requests

# files = {"file": open("image.png", "rb")}

# resp = requests.post("http://127.0.0.1:8000/caption", files=files)
# print(resp.json())


import requests
import os

# --- Configuration ---
# 1. Ensure the URL matches the running FastAPI Agent endpoint
# It must be /upload, not /caption
AGENT_URL = "http://127.0.0.1:8000/caption"
IMAGE_FILENAME = "image.png"

# --- Main Logic ---

def run_test_upload():
    """Runs the raw image upload test to the FastAPI Agent."""
    
    if not os.path.exists(IMAGE_FILENAME):
        print(f" Error: Image file '{IMAGE_FILENAME}' not found.")
        print("Please make sure you have an image named 'image.png' in this folder.")
        return

    try:
        # 1. Read the image file as raw binary data
        with open(IMAGE_FILENAME, "rb") as f:
            image_bytes = f.read()

        print(f"Read image: {len(image_bytes)} bytes. Sending to Agent at {AGENT_URL}...")

        response = requests.post(
            AGENT_URL,
            data=image_bytes,
            headers={
                "Content-Type": "image/jpeg"
            }
        )

        print("\n--- Server Analysis Response ---")
        try:
            response_json = response.json()
            print(response_json)
        except requests.exceptions.JSONDecodeError:
            print("Could not decode JSON response. Raw text response:")
            print(response.text)
            response_json = {}

        if response.status_code == 200 and response_json.get('status') == 'success':
            print("\nTest Successful: Image analyzed and Firebase update initiated.")
        elif response.status_code == 200:
             print(f"\nTest Warning: Server returned success but details may be missing.")
        else:
            print(f"\n Test Failed: HTTP Status Code {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("\n Error: Could not connect to the Agent.")
        print("Please ensure your Python Agent (blood_bank_agent.py) is running on port 8000.")
    except Exception as e:
        print(f"\n An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_test_upload()