from flask import Flask, render_template, request, send_file
from datetime import datetime
import qrcode
import os
from firebase_setup import add_baby_qr_code  # Ensure this function is defined to insert data into your database
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Update the path as needed
QR_CODE_PATH = r'infant-Monitoring\qr_codes'

# Route for the home page with input form
@app.route('/')
def index():
    return render_template('index.html')

# Route for generating QR code
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    baby_id = request.form['baby_id']
    parent_email = request.form['parent_id']
    hospital_id = request.form['hospital_id']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    qr_code_image_path = os.path.join(QR_CODE_PATH, f"{baby_id}_qr_code.png")
    
    qr_data = (
        f"Baby ID: {baby_id}, Parent Email: {parent_email}, "
        f"Hospital ID: {hospital_id}, Timestamp: {timestamp}"
    )

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill='black', back_color='white')
    qr_image.save(qr_code_image_path)

    # Store QR code in Firebase
    add_baby_qr_code(baby_id, parent_email, hospital_id, qr_code_image_path, timestamp)

    # Send QR code to parents (email)
    send_qr_to_parents(parent_email, qr_code_image_path)

    return send_file(qr_code_image_path, as_attachment=True)

def send_qr_to_parents(parent_email, qr_code_path):
    # Set up email parameters
    msg = MIMEMultipart()
    msg['Subject'] = 'Your Baby\'s QR Code'
    msg['From'] = 'karenmalunga860@gmail.com'
    msg['To'] = parent_email

    # Attach the QR code image
    with open(qr_code_path, 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name=os.path.basename(qr_code_path))
    msg.attach(image)

    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('karenmalunga860@gmail.com', 'ofau bann xneh haky')
        server.sendmail('anthonymalunga5@gmail.com', parent_email, msg.as_string())

if __name__ == '__main__':
    if not os.path.exists(QR_CODE_PATH):
        os.makedirs(QR_CODE_PATH)
    app.run(debug=True)
