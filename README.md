# Real-Time Location Tracking with Google Maps Integration

This Python script utilizes the Google Maps API to track real-time location using an Android device and provides directions from the current location to a specified destination. It extracts latitude and longitude coordinates using the adb shell command and fetches directions using the Google Maps API.

Prerequisites
Python 3 installed
Google Maps API key
googlemaps library installed (pip install -U googlemaps)
Android Debug Bridge (adb) installed and device connected
Setup
Obtain a Google Maps API key from the Google Cloud Console.
Install the required Python libraries: googlemaps.
Ensure that adb is installed and your Android device is connected to the computer.
Usage
Replace 'Your_api_key' in the script with your Google Maps API key.

Specify the destination address or coordinates in the destination variable.

Run the script using Python:
-> python location_tracker.py

The script will continuously fetch the current location of the device and provide directions to the specified destination.

Features
Real-time location tracking using adb shell command.
Google Maps integration for fetching directions.
Continuous monitoring of location updates.
Display of route details including distance, duration, and step-by-step instructions.
Note
Ensure that your Google Maps API key has the necessary permissions for the Directions API.
The adb command might require additional setup or permissions based on your device and operating system.

Author
Chirag Vats

License
This project is licensed under the MIT License.
