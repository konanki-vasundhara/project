import qrcode

def generate_qr(data, filename="qrcode.png"):
    # Create qr code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Example usage
if _name_ == "_main_":
    data = input("Enter data or URL for QR code: ")
    generate_qr(data)