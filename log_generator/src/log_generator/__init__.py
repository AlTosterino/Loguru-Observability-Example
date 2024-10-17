import random
from loguru import logger
from datetime import datetime
import uuid
import time
import threading

# Simulated user actions
user_actions = [
    "Login",
    "View Product",
    "Add to Cart",
    "Checkout",
    "Logout",
    "Search Product",
    "View Order History",
    "Apply Discount Code",
    "Leave Feedback",
]

# Simulated product categories
product_categories = [
    "Electronics",
    "Books",
    "Clothing",
    "Home & Garden",
    "Toys",
    "Sports",
]


# Function to generate random user journey logs
def generate_user_journey_logs(user_id):
    journey_length = random.randint(5, 15)  # Random number of actions between 5 and 15
    for _ in range(journey_length):  # Simulate user actions
        action = random.choice(user_actions)
        category = (
            random.choice(product_categories)
            if action in ["View Product", "Add to Cart", "Search Product"]
            else None
        )
        product_id = (
            str(uuid.uuid4()) if category else None
        )
        duration = random.randint(1, 10)
        success = random.choices([True, False], weights=[80, 20], k=1)[0]

        log_context = {
            "user_id": user_id,
            "action": action,
            "timestamp": datetime.now().isoformat(),
            "session_id": str(uuid.uuid4()),
            "product_id": product_id,
            "category": category,
            "duration": duration,
            "success": success,
        }

        if not success:
            logger.bind(**log_context).error(
                f"Action '{action}' failed for User ID {user_id}"
            )
        elif duration > 8:
            logger.bind(**log_context).warning(
                f"Action '{action}' took unusually long ({duration}s) for User ID {user_id}"
            )
        elif action == "Checkout" and not success:
            logger.bind(**log_context).critical(
                f"Critical failure during checkout for User ID {user_id}"
            )
        else:
            logger.bind(**log_context).info(
                f"Action '{action}' completed successfully for User ID {user_id}"
            )

        time.sleep(random.uniform(0.5, 2.5))


def simulate_user_journey(user_id):
    print(f"Starting user journey for User ID: {user_id}")
    generate_user_journey_logs(user_id)
    print(f"User journey completed for User ID: {user_id}")


def main():
    number_of_users = 10
    threads = []
    while True:
        for _ in range(number_of_users):
            user_id = str(uuid.uuid4())
            thread = threading.Thread(target=simulate_user_journey, args=(user_id,))
            threads.append(thread)
            time.sleep(random.uniform(0.5, 4.5))
            thread.start()

        for thread in threads:
            thread.join()
