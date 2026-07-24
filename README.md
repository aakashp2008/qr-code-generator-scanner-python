# QR Code Generator & Scanner

## 📌 Overview

The **QR Code Generator & Scanner** is a Python-based console application that allows users to generate QR codes from text or URLs and scan existing QR code images to retrieve the encoded information. The project demonstrates the use of third-party Python libraries for QR code generation and image processing.

This application is ideal for learning Python file handling, image processing, and working with external libraries.

---

## ✨ Features

- 📱 Generate QR codes from text or URLs
- 🔍 Scan and decode QR codes from image files
- 💾 Save generated QR codes as PNG images
- 📂 Validate image file existence before scanning
- 🖥️ Simple menu-driven interface
- ⚡ Fast and lightweight implementation

---

## 🛠️ Technologies Used

- Python 3
- qrcode
- Pillow (PIL)
- OpenCV (cv2)
- OS Module

---

## 📦 Required Libraries

Install the required libraries before running the project:

```bash
pip install qrcode[pil]
pip install opencv-python
```

---

## 📂 Project Structure

```
qr-code-generator-scanner-python/
│── qr_code_generator_scanner.py
│── README.md
│── sample_qr.png          # Generated after running the program
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/aakashp2008/qr-code-generator-scanner-python.git
```

Navigate to the project folder:

```bash
cd qr-code-generator-scanner-python
```

Run the program:

```bash
python qr_code_generator_scanner.py
```

---

## 💡 How It Works

### Generate QR Code

1. Select **Generate QR Code**.
2. Enter the text or URL.
3. Enter the file name.
4. The QR code image will be saved as a PNG file.

### Scan QR Code

1. Select **Scan QR Code**.
2. Enter the QR code image filename.
3. The application decodes and displays the stored information.

---

## 📸 Example

### Main Menu

```
======================================
   QR CODE GENERATOR & SCANNER
======================================
1. Generate QR Code
2. Scan QR Code
3. Exit
```

### Generated Output

```
QR Code saved successfully as 'github.png'
```

### Scanned Output

```
QR Code Detected Successfully!
--------------------------------
Decoded Data: https://github.com/aakashp2008
```

---

## 🎯 Learning Outcomes

Through this project, I gained experience in:

- Working with external Python libraries
- Generating QR codes programmatically
- Image processing using OpenCV
- File handling in Python
- Building menu-driven console applications
- Writing modular and reusable functions

---

## 🚀 Future Enhancements

- Scan QR codes using a webcam
- Support multiple QR codes in a single image
- Customize QR code colors
- Add company logo inside QR code
- Build a graphical user interface (Tkinter)
- Export scan history

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**AAKASH P**

- B.Tech Information Technology Student
- Aspiring Software Engineer
- Skilled in Python, Java, C, Data Structures, SQL, and Software Development

**GitHub:** https://github.com/aakashp2008
