import firebase_admin
from firebase_admin import credentials, db
import os

def init_firebase():
    """Initializes the connection to Firebase using the service_account.json file."""
    if not firebase_admin._apps:
        cred_path = os.path.join(os.path.dirname(__file__), "iot-midterm-project-firebase-adminsdk-fbsvc-8942c88c7b.json")
        
        if os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://iot-midterm-project-default-rtdb.europe-west1.firebasedatabase.app'
            })
            print(" Firebase Connected")
        else:
            print(" WARNING: service_account.json not found! Firebase updates will fail.")

def update_inventory(data):
    """Updates the inventory/bloodBags node in Realtime Database."""
    try:
        # Only try to update if Firebase is initialized
        if firebase_admin._apps:
            ref = db.reference('inventory/bloodBags')
            ref.update(data)
            print("Inventory updated in Firebase!")
        else:
            print(" Firebase not connected, skipping update.")
            
    except Exception as e:
        print(f" Error updating Firebase: {e}")