import cv2
import os

def encrypt_image(input_path, output_path, msg, password, password_file_path):
    img = cv2.imread(input_path)

    if img is None:
        raise Exception(f"Could not read image: {input_path}")

    d = {chr(i): i for i in range(256)}
    msg += "~"

    n = m = z = 0
    for char in msg:
        img[n, m, z] = d[char]
        z = (z + 1) % 3
        if z == 0:
            m += 1
        if m == img.shape[1]:
            m = 0
            n += 1

    cv2.imwrite(output_path, img)

    with open(password_file_path, "w") as file:
        file.write(password)

    return output_path

if __name__ == "__main__":
    base_path = r"C:\Users\ASUS\Desktop\project"
    encrypt_image(
        input_path=os.path.join(base_path, "mypic.jpg"),
        output_path=os.path.join(base_path, "encryptedImage.png"),
        msg=input("Enter secret message: "),
        password=input("Enter a passcode: "),
        password_file_path=os.path.join(base_path, "password.txt")
    )
