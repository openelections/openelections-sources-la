# pelbot/app/__init__.py
import os
from .utils import configure_logger, logger, load_yaml_config
from .historical import capture_history
from .live import live_stream

def config_me():
    """
    Loads the main configuration and sets up the logging environment.
    """
    try:
        main_config = load_yaml_config('main')
        if main_config is None:
            raise ValueError("Main configuration could not be loaded.")

        os.environ["LOG_LEVEL"] = main_config["logging"]["level"]
        os.environ["LOG_VERBOSE"] = str(main_config["logging"]["verbose"]).lower()


        configure_logger()
        logger.info("Configuration loaded successfully.")
    except Exception as e:
        logger.error(f"An error occurred while loading configuration: {e}", exc_info=True)

def lets_fly(capture_type, capture_range=None):
    try:
        if capture_type == "live":
            live_stream()
        elif capture_type == "historical":
            capture_history(capture_range)
        else:
                logger.error(f"Invalid capture_type provided: {capture_type}. Valid options are: historical, live")

    except Exception as e:
        logger.error(f"Something went wrong during liftoff: {e}", exc_info=True)
