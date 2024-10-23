import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase Admin SDK with credentials
cred = credentials.Certificate(
    r'C:\Users\tony\source\repos\Infant-Monitroing-System\infant-monitoring-system-1104d-firebase-adminsdk-w4r7q-c43ddd20e7.json'
)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://infant-monitoring-system-1104d-default-rtdb.firebaseio.com'
})

# Function to add baby QR code data to Firebase
def add_baby_qr_code(baby_id, parent_id, hospital_id, qr_code_image_path, timestamp):
    try:
        ref = db.reference('baby_qr_codes')
        ref.push({
            'baby_id': baby_id,
            'parent_id': parent_id,
            'hospital_id': hospital_id,
            'qr_code_image_path': qr_code_image_path,
            'timestamp': timestamp
        })
        print("QR code data added to Firebase.")
    except Exception as e:
        print(f"An error occurred: {e}")
