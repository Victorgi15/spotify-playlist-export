import base64
import requests
from typing import Dict
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_token() -> str:
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers: Dict[str, str] = {
        'Authorization': f'Basic {auth_base64}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data: Dict[str, str] = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    token: str = response.json()['access_token']
    return token

def get_auth_header(token: str) -> Dict[str, str]:
    return {"Authorization": f"Bearer {token}"}
