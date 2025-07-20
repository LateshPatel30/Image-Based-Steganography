import cv2
import os

def decrypt_image(input_path, entered_password, password_file_path):
    img = cv2.imread(input_path)

    if img is None:
        raise Exception(f"Could not read image: {input_path}")

    with open(password_file_path, "r") as file:
        saved_password = file.read()

    if entered_password != saved_password:
        return "YOU ARE NOT AUTHORIZED"

    c = {i: chr(i) for i in range(256)}
    message = ""
    n = m = z = 0
    while True:
        char_value = img[n, m, z]
        char = c[char_value]
        if char == "~":
            break
        message += char
        z = (z + 1) % 3
        if z == 0:
            m += 1
        if m == img.shape[1]:
            m = 0
            n += 1

    return message

if __name__ == "__main__":
    base_path = r"C:\Users\ASUS\Desktop\project"
    password = input("Enter passcode for Decryption: ")
    result = decrypt_image(
        input_path=os.path.join(base_path, "encryptedImage.png"),
        entered_password=password,
        password_file_path=os.path.join(base_path, "password.txt")
    )
    print(result)
