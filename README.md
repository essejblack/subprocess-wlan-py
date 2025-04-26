# Wi-Fi Password Extractor

A simple Python script that uses the **subprocess** library to extract Wi-Fi profiles and their corresponding passwords from a Windows machine.

## Features

- Extracts saved Wi-Fi profiles on Windows systems.
- Retrieves SSID and corresponding Wi-Fi password (if available).
- Simple to use and requires no external libraries other than Python's built-in modules.

## Technologies

- Python 3.x
- subprocess (for executing system commands)
- Regular Expressions (for parsing the output)

## Setup and Usage

1. Ensure you have Python 3.x installed on your system.
2. Clone or download this repository to your local machine.
3. Install Requirements
```
pip install subprocess
```
4. Run the script with administrative privileges (as it requires access to network profiles):

```bash
python wifi_password_extractor.py
```
5.The script will output the SSID and the corresponding password of all saved Wi-Fi networks on your system.

Note: Make sure to run the script with necessary permissions to access Wi-Fi credentials.
