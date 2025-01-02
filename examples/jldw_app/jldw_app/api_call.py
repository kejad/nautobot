import requests

def make_api_call(url, params=None, headers=None, verify=False):
    try:
        response = requests.get(url, params=params, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API call: {e}")
        return None

# Move the API call configuration to your Django view
def get_devices_data():
    url = "https://demo.nautobot.com/api/dcim/devices"
    token = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    params = {
        "position": 40
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Token {token}"
    }

    return make_api_call(url, params=params, headers=headers, verify=False)
