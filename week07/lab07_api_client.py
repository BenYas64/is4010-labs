import json
import requests


def get_api_data(url, timeout=10):
    """Return parsed JSON from url, or None when the request or decoding fails."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raise an error for HTTP errors
        return response.json()
    except (requests.RequestException, json.JSONDecodeError, ValueError):
        return None