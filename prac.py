import re
import subprocess
import time
import googlemaps
from datetime import datetime

# Define your Google Maps API key
API_KEY = 'Your_api_key'

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=API_KEY)

def get_location():
    try:
        # Run the command to get location data
        output = subprocess.check_output("adb shell dumpsys location", shell=True).decode()
        
        # Extract latitude and longitude using regular expressions
        matches = re.findall(r'last location=Location\[fused ([\d.]+),([\d.]+)', output)
        if matches:
            latitude, longitude = matches[-1]  # Get the last recorded location
            return float(latitude), float(longitude)
    except Exception as e:
        print(f"Error getting location: {e}")
    return None, None

def send_location(latitude, longitude, destination):
    try:
        # Initialize the Google Maps client
        gmaps = googlemaps.Client(key=API_KEY)

        # Get directions between source (current location) and destination
        get_directions((latitude, longitude), destination)
    except Exception as e:
        print(f"Error sending location data: {e}")

def get_directions(source, destination):
    try:
        # Request directions via public transit
        directions_result = gmaps.directions(source, destination, mode="driving", departure_time=datetime.now())

        # Extract route details
        route = directions_result[0]['legs'][0]
        distance = route['distance']['text']
        duration = route['duration']['text']
        steps = route['steps']

        # Print route details
        print(f"Route from {source} to {destination}:")
        print(f"Distance: {distance}")
        print(f"Duration: {duration}")
        print("Steps:")
        for step in steps:
            instructions = re.sub('<[^<]+?>', '', step['html_instructions'])
            print(f"- {instructions} ({step['distance']['text']})")

    except googlemaps.exceptions.ApiError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Destination coordinates (latitude, longitude)
    destination = "SJT Building, VIT Vellore"

    while True:
        latitude, longitude = get_location()
        if latitude is not None and longitude is not None:
            print("\n")
            print(f"Latitude: {latitude}, Longitude: {longitude}")
            send_location(latitude, longitude, destination)
        time.sleep(10)  # Wait for 5 seconds before checking again
