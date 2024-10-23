from firebase_setup import add_baby_qr_code
from datetime import datetime

# QR code details
baby_id = "B001"
parent_id = "P001"
hospital_id = "H001"
qr_code_image_path = "qr_code_B001.png"
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Add QR code details to Firebase
add_baby_qr_code(baby_id, parent_id, hospital_id, qr_code_image_path, timestamp)

