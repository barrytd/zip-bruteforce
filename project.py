from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        # Attempt to extract the zip file using the provided password
        zf_handle.extractall(pwd=password.encode())
        return True  # Extraction successful
    except RuntimeError as e:
        if "Bad password" in str(e):
            return False  # Incorrect password
        else:
            raise  # Other runtime error

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            # Iterate through password entries in rockyou.txt
            for line in f:
                password = line.strip().decode('utf-8')

                # Attempt to extract the zip file using each password
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password}")
                    break  # Stop iterating if the correct password is found

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()