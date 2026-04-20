import base64
import binascii

def b64_encode(data):
    return base64.b64encode(data.encode()).decode()

def b64_decode(data):
    try:
        return base64.b64decode(data.encode()).decode()
    except Exception:
        return "[!] Error: Invalid Base64 string."

def hex_encode(data):
    return binascii.hexlify(data.encode()).decode()

def hex_decode(data):
    try:
        return binascii.unhexlify(data.encode()).decode()
    except Exception:
        return "[!] Error: Invalid Hex string."

def main():
    print("--- CTF Data Converter ---")
    print("1. Base64 Encode")
    print("2. Base64 Decode")
    print("3. Hex Encode")
    print("4. Hex Decode")
    
    choice = input("\nSelect an option (1-4): ")
    text = input("Enter the string: ")

    if choice == '1':
        print(f"Result: {b64_encode(text)}")
    elif choice == '2':
        print(f"Result: {b64_decode(text)}")
    elif choice == '3':
        print(f"Result: {hex_encode(text)}")
    elif choice == '4':
        print(f"Result: {hex_decode(text)}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()