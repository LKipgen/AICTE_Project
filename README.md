# Image Steganography Tool

A Python tool to hide secret messages in PNG images using a password.

## Algorithm
- **Pixel Manipulation**: The secret message is embedded into the RGB values of the image pixels.
- **Character Mapping**: Each character in the message is mapped to its ASCII value and stored in the image pixels.
- **Password Protection**: A password is required to decrypt the message, ensuring security.

## Encrypting a Message
To hide a secret message in an image

STEPS :
1. Load the input image (`city_view.png`).
2. Convert the secret message into ASCII values.
3. Embed each character into the image pixels (R, G, B channels sequentially).
4. Append a special character (`\0`) to mark the end of the message.
5. Save the encrypted image as `encryptedImage.png`.

## Decrypting a Message
To retrieve a hidden message from the encrypted image 

STEPS: 
1. Load the encrypted image (`encryptedImage.png`).
2. Verify the password.
3. Extract ASCII values from the image pixels (R, G, B channels sequentially).
4. Convert ASCII values back to characters until the special character (`\0`) is encountered.
5. Display the decrypted message.

## Usage
### Encrypt
1. Run `encrypt.py`.
2. Enter your message and password.
3. Encrypted image saved as `encryptedImage.png`.

### Decrypt
1. Run `decrypt.py`.
2. Enter the password.
3. Decrypted message will be displayed.

## Requirements
- Python 3.x
- OpenCV (`pip install opencv-python/cv2`)

