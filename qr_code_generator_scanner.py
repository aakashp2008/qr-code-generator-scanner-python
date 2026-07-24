import qrcode
import cv2
import os


def generate_qr():
    data = input("\nEnter the text or URL: ")

    filename = input("Enter QR Code file name (without extension): ") + ".png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(filename)

    print(f"\nQR Code saved successfully as '{filename}'")

def scan_qr():
    filename = input("\nEnter QR Code image file name: ")

    if not os.path.exists(filename):
        print("\nFile not found!")
        return

    image = cv2.imread(filename)

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    if data:
        print("\nQR Code Detected Successfully!")
        print("--------------------------------")
        print("Decoded Data:", data)
    else:
        print("\nNo QR Code found in the image!")
      
def menu():
    while True:
        print("\n======================================")
        print("   QR CODE GENERATOR & SCANNER")
        print("======================================")
        print("1. Generate QR Code")
        print("2. Scan QR Code")
        print("3. Exit")
        print("--------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_qr()

        elif choice == "2":
            scan_qr()

        elif choice == "3":
            print("\nThank you for using QR Code Generator & Scanner!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    menu()
