import configparser
import json
import logging
import random
from datetime import datetime, timedelta

import requests

# Load configuration data from config.properties file
config = configparser.ConfigParser()
config.read('data/config.properties')

BASE_URL = config.get('DEFAULT', 'url')


def setup_logging():
    logging.basicConfig(filename='logs/api_log.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


def generate_random_dates():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=random.randint(1, 10))
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")


def create_token():
    auth_data = {
        "username": config.get('DEFAULT', 'username'),
        "password": config.get('DEFAULT', 'password')
    }
    response = requests.post(f"{BASE_URL}/auth", json=auth_data)
    response.raise_for_status()
    return response.json()['token']
