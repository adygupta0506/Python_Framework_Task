import requests
import json

from utils import BASE_URL, create_token


def create_booking(booking_data):
    response = requests.post(f"{BASE_URL}/booking", json=booking_data)
    return response.json()


def get_all_booking_ids():
    response = requests.get(f"{BASE_URL}/booking")
    return [booking['bookingid'] for booking in response.json()]


def get_booking_details(booking_id):
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    return response.json()


def update_booking_price(booking_id, new_price):
    auth_token = create_token()
    headers = {'Cookie': f'token={auth_token}'}
    response = requests.patch(f"{BASE_URL}/booking/{booking_id}", json={"totalprice": new_price}, headers=headers)
    return response.json()


def delete_booking(booking_id):
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}")
    return response.status_code
