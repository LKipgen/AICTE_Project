import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

# Load the password from the file
with open("password.txt", "r") as f:
    password = f.read().strip()

# Get the password for decryption
pas = input("Enter passcode for Decryption: ")

# Verify the password
if password == pas:
    # Initialize variables for pixel manipulation
    m, n, z = 0, 0, 0
    message = ""

    # Decrypt the message from the image
    while True:
        # Get the ASCII value of the pixel
        char_code = img[n, m, z]
        # Convert the ASCII value to a character
        char = chr(char_code)
        # Stop if the special character is encountered
        if char == "\0":
            break
        # Append the character to the message
        message += char
        # Move to the next pixel
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT auth")
