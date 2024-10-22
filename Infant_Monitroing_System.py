import qrcode
from datetime import datetime

def generate_baby_qr_code(output_file):
    """
    Collect user input for baby ID, parent ID, hospital ID, and generate a QR code.

    Parameters:
        output_file (str): The filename for saving the generated QR code image.
    """
    try:
        # Step 1: Collect user input
        baby_id = input("Enter Baby ID: ")
        parent_id = input("Enter Parent ID: ")
        hospital_id = input("Enter Hospital ID: ")

        # Step 2: Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Step 3: Create the data to encode in the QR code
        data = {
            "baby_id": baby_id,
            "parent_id": parent_id,
            "timestamp": timestamp,
            "hospital_id": hospital_id
        }

        # Step 4: Convert the dictionary to a string for encoding in the QR code
        qr_data = (
            f"Baby ID: {data['baby_id']}, "
            f"Parent ID: {data['parent_id']}, "
            f"Timestamp: {data['timestamp']}, "
            f"Hospital ID: {data['hospital_id']}"
        )

        # Step 5: Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code (1 is the smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=4  # Thickness of the border
        )

        # Step 6: Add data to the QR code
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Step 7: Create an image from the QR code
        qr_image = qr.make_image(fill='black', back_color='white')
        
        # Step 8: save an qrcode image
        qr_image.save("baby_qr_code.png")  # Save as PNG


        print(f"QR code generated and saved as {output_file}")

    except Exception as e:
        print(f"Error generating QR code: {e}")

# Example usage
if __name__ == "__main__":
    output_filename = input("Enter the filename for the QR code (e.g., 'baby_qr_code.jpeg'): ")
    generate_baby_qr_code(output_filename)
