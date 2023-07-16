# base_enc.py
import base64

def base_enc(source_name):
    with open(source_name, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode('utf-8')

    filename = 's.txt'
    with open(filename, 'w') as file:
        file.write(encoded_string)

    print(encoded_string)
