# pelbot/app/history_class/request.py

import os
import requests
from requests.exceptions import RequestException
from app.utils import logger

def make_get_request(url, YYYY, election):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        logger.info(f"GET request to {url} successful.")

        # Create the directory for the year if it doesn't exist
        output_dir = os.path.join('..', 'data', YYYY)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Extract the extension from the filename in the URL
        _, extension = os.path.splitext(url.split("/")[-1])

        # Construct the output filename and path
        filename = f"{election}{extension}"
        output_path = os.path.join(output_dir, filename)

        # Write the file contents to the output path
        with open(output_path, 'wb') as file:
            file.write(response.content)
        logger.info(f"File saved to {output_path}")
        return True
    except RequestException as e:
        logger.error(f"GET request to {url} failed: {e}")
        return False
