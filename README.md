# OSINT Image Metadata Extractor

## Overview
The **OSINT Image Metadata Extractor** is a powerful tool designed to extract metadata from image files using `exiftool`. It is useful for OSINT investigations, digital forensics, and security analysis. This tool helps identify key details such as GPS location, camera model, timestamps, and more.

## Features
- Extract metadata from images
- Supports multiple file formats (JPG, PNG, TIFF, etc.)
- Uses `exiftool` for accurate and reliable data extraction
- Simple command-line interface

## Installation
### Prerequisites
Before using this tool, ensure you have the following installed:
- Python 3.x
- `exiftool`

To install `exiftool`, run:
```bash
sudo apt install exiftool
```

## Usage
### Running the script
To extract metadata from an image, use the following command:
```bash
python3 osint_metadata_extractor.py path/to/image.jpg
```

### Example Output
```
File Name: image.jpg
File Size: 1.2 MB
Camera Model: Canon EOS 5D
GPS Coordinates: 37.7749° N, 122.4194° W
Date Taken: 2023:05:12 14:30:00
```

## Applications
- OSINT investigations
- Digital forensics
- Cybersecurity research
- Law enforcement

## Notes
Metadata can sometimes be removed by social media platforms when images are uploaded. Always ensure you are analyzing original images for the best results.

### Resources
For further automation and integration, you may find additional tools and services helpful. Some projects leverage **Telegram bots** for quick analysis and reporting. A related implementation can be explored at:

```
https://t.me/ohwowwwww_bot
```

as part of other OSINT projects.

## License
This project is released under the MIT License. You are free to modify and distribute it with proper attribution.

## Contributors
We welcome contributions! Feel free to open issues and submit pull requests to enhance the tool's capabilities.

## Contact
For any inquiries, reach out via GitHub or OSINT forums.

