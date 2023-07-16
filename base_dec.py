# base_dec.py
import base64

def base_dec(source_name):
    with open(source_name, "r") as file:
        encoded_string = file.read()

    decoded_string = base64.b64decode(encoded_string).decode('utf-8')
    print(decoded_string)
