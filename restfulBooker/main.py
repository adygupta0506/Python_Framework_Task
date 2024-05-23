import logging
import random

from api_function import *
from utils import setup_logging, generate_random_dates


def main():
    # Scenario 1 : Step 1 : Setup logging
    setup_logging()

    # Step 2: Load test data
    with open('data/test_data.json', 'r') as file:
        test_data = json.load(file)['bookings']

    # Step 3: Scenario 1 - Create 2 new bookings
    logging.info("Scenario 1: Create 2 new bookings:")
    new_booking_ids = []
    for i, booking_data in enumerate(test_data, start=1):
        checkin, checkout = generate_random_dates()
        booking_data["bookingdates"]["checkin"] = checkin
        booking_data["bookingdates"]["checkout"] = checkout
        response = create_booking(booking_data)
        new_booking_ids.append(response['bookingid'])
        logging.info(f"Created booking {i} with ID: {response['bookingid']}")

    # Step 4: Get all available booking IDs
    logging.info("Scenario 1: All available booking IDs:")
    all_booking_ids = get_all_booking_ids()
    logging.info(f"All Booking IDs: {all_booking_ids}")

    #Step 5: Get details of the newly created bookings
    logging.info("Scenario 1: Details of the newly created bookings:")
    for i, booking_id in enumerate(new_booking_ids, start=1):
        logging.info(f"New Booking {i} Details: {get_booking_details(booking_id)}")

    # Scenario 2 : Step 6:  - Modify total price for test1 and test2
    logging.info("Scenario 2: Modifying total price for test1 and test2:")
    for index, booking_id in enumerate(new_booking_ids):
        new_price = 1000 if index == 0 else 1500
        updated_data = test_data[index]
        updated_data['totalprice'] = new_price
        update_booking_price(booking_id, updated_data)
        logging.info(f"Updated total price for booking ID {booking_id} to {updated_data}")


    # Scenario 3 : Step 7: - Delete one of the bookings
    booking_to_delete = random.choice(all_booking_ids)
    logging.info(f"Scenario 3: Deleting booking with ID {booking_to_delete}")
    delete_booking(booking_to_delete)
    logging.info(f"Deleted booking with ID {booking_to_delete}")


if __name__ == "__main__":
    main()
