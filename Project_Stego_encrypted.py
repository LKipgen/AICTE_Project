import cv2
import os

# Load the image
img = cv2.imread("night.png")  # Replace with the correct image path

# Get the secret message and password from the user
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Append a special character to mark the end of the message
msg += "\0"  # Null character to indicate the end of the message

# Create dictionaries to map characters to their ASCII values and vice versa
d = {chr(i): i for i in range(255)}

# Initialize variables for pixel manipulation
m, n, z = 0, 0, 0

# Encrypt the message into the image
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.png", img)
print("Image encrypted and saved as 'encryptedImage.png'")

# Save the password to a file (for decryption)
with open("password.txt", "w") as f:
    f.write(password)

# Optionally, open the encrypted image
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows
