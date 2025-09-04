import base64
import os

def convert_zip_to_base64():
    zip_path = input("Enter the path to the .zip file: ").strip()

    if not os.path.exists(zip_path):
        print("File not found!")
        return

    try:
        with open(zip_path, "rb") as f:
            file_bytes = f.read()

        base64_string = base64.b64encode(file_bytes).decode("utf-8")

        output_path = os.path.splitext(zip_path)[0] + ".b64.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(base64_string)

        print(f"Conversion complete! Saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")


def convert_base64_to_zip():
    txt_path = input("Enter the path to the Base64 .txt file: ").strip()

    if not os.path.exists(txt_path):
        print("File not found!")
        return

    try:
        with open(txt_path, "r", encoding="utf-8") as f:
            base64_string = f.read()

        file_bytes = base64.b64decode(base64_string)

        output_path = os.path.splitext(txt_path)[0] + ".restored.zip"
        with open(output_path, "wb") as f:
            f.write(file_bytes)

        print(f"Conversion complete! Restored ZIP: {output_path}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("Choose an option:")
    print("1. Convert ZIP to Base64")
    print("2. Convert Base64 to ZIP")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        convert_zip_to_base64()
    elif choice == "2":
        convert_base64_to_zip()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
