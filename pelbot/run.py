# pelbot/run.py
import os
from dotenv import load_dotenv



def main():
    from app import logger, config_me, lets_fly

    config_me()  # Set envars based on main.yml
    logger.info("🚀 Starting the pelbot ")

    # Set capture type from envars
    capture_type = os.environ.get("CAPTURE_TYPE")
    capture_range = os.environ.get("CAPTURE_RANGE")

    logger.info(f'Capture Config:\n Type: {capture_type}\nRange: {capture_range}')

    try:
        lets_fly(capture_type, capture_range)

    except Exception as e:
        logger.error("An unexpected error occurred: %s", str(e), exc_info=True)

if __name__ == "__main__":
    load_dotenv()
    main()
