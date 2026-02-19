import base64
import os
filenume = 0

try:
    while True:
        choice = input("choose type of encoding: b64, hex, binary, sha256, sha512, md5: ").lower()
        if choice == "b64":
            os.system("cls" if os.name == "nt" else "clear")
            choice = input("encode or decode (e/d): ").lower()
            if choice == "e":
                os.system("cls" if os.name == "nt" else "clear")
                txt = input("Enter the text to encode: ")
                encoded_bytes = base64.b64encode(txt.encode("utf-8"))
                encoded_str = encoded_bytes.decode("utf-8")
                print("> ", encoded_str)
                open(f"output{filenume}.txt", "w").write(encoded_str)
                filenume += 1
                input("Press Enter to continue...")
            elif choice == "d":
                os.system("cls" if os.name == "nt" else "clear")
                txt = input("Enter the text to decode: ")
                decoded_bytes = base64.b64decode(txt.encode("utf-8"))
                decoded_str = decoded_bytes.decode("utf-8")
                print("> ", decoded_str)
                open(f"output{filenume}.txt", "w").write(decoded_str)
                filenume += 1
                input("Press Enter to continue...")
        elif choice == "hex":
            os.system("cls" if os.name == "nt" else "clear")
            choice = input("encode or decode (e/d): ").lower()
            if choice == "e":
                os.system("cls" if os.name == "nt" else "clear")
                txt = input("Enter the text to encode: ")
                encoded_str = txt.encode("utf-8").hex()
                print("> ", encoded_str)
                open(f"output{filenume}.txt", "w").write(encoded_str)
                filenume += 1
                input("Press Enter to continue...")
            elif choice == "d":
                os.system("cls" if os.name == "nt" else "clear")
                txt = input("Enter the text to decode: ")
                decoded_bytes = bytes.fromhex(txt)
                decoded_str = decoded_bytes.decode("utf-8")
                print("> ", decoded_str)
                open(f"output{filenume}.txt", "w").write(decoded_str)
                filenume += 1
                input("Press Enter to continue...")
        elif choice == "binary":
            os.system("cls" if os.name == "nt" else "clear")
            choice = input("encode or decode (e/d): ").lower()
            if choice == "e":
                os.system("cls" if os.name == "nt" else "clear")
                txt = input("Enter the text to encode: ")
                encoded_str = ' '.join(format(ord(char), '08b') for char in txt)
                print("> ", encoded_str)
                open(f"output{filenume}.txt", "w").write(encoded_str)
                filenume += 1
                input("Press Enter to continue...")
            elif choice == "d":
                os.system("cls" if os.name == "nt" else "clear")
                txt = input("Enter the text to decode: ")
                decoded_str = ''.join(chr(int(b, 2)) for b in txt.split())
                print("> ", decoded_str)
                open(f"output{filenume}.txt", "w").write(decoded_str)
                filenume += 1
                input("Press Enter to continue...")
        elif choice == "sha256":
            os.system("cls" if os.name == "nt" else "clear")
            txt = input("Enter the text to hash: ")
            import hashlib
            hashed_str = hashlib.sha256(txt.encode("utf-8")).hexdigest()
            print("> ", hashed_str)
            open(f"output{filenume}.txt", "w").write(hashed_str)
            filenume += 1
            input("Press Enter to continue...")
        elif choice == "sha512":
            os.system("cls" if os.name == "nt" else "clear")
            txt = input("Enter the text to hash: ")
            import hashlib
            hashed_str = hashlib.sha512(txt.encode("utf-8")).hexdigest()
            print("> ", hashed_str)
            open(f"output{filenume}.txt", "w").write(hashed_str)
            filenume += 1
            input("Press Enter to continue...")
        elif choice == "md5":
            os.system("cls" if os.name == "nt" else "clear")
            txt = input("Enter the text to hash: ")
            import hashlib
            hashed_str = hashlib.md5(txt.encode("utf-8")).hexdigest()
            print("> ", hashed_str)
            open(f"output{filenume}.txt", "w").write(hashed_str)
            filenume += 1
            input("Press Enter to continue...")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
            os.system("cls" if os.name == "nt" else "clear")
        os.system("cls" if os.name == "nt" else "clear")
except Exception as e:
    print("An error occurred:", str(e))
    input("Press Enter to exit...")
        