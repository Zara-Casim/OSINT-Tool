import argparse
import subprocess
import json

def extract_metadata(image_path):
    try:
        result = subprocess.run(['exiftool', '-json', image_path], capture_output=True, text=True)
        metadata = json.loads(result.stdout)
        return metadata[0] if metadata else {}
    except Exception as e:
        print(f"Error extracting metadata: {e}")
        return {}

def main():
    parser = argparse.ArgumentParser(description='Extract metadata from an image file using exiftool')
    parser.add_argument('image', type=str, help='Path to the image file')
    args = parser.parse_args()
    
    metadata = extract_metadata(args.image)
    if metadata:
        for key, value in metadata.items():
            print(f"{key}: {value}")
    else:
        print("No metadata found.")

if __name__ == "__main__":
    main()
