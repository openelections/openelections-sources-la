# pelbot/app/utils/load_yaml.py
"""
Loads YAML config files and outputs applicable configs
"""
import os
import yaml
from .logging import logger


def load_yaml_config(config_name):
    """
    Loads a YAML configuration file by name from the config directory.

    Args:
        config_name (str): The name of the configuration to load (without .yml extension).

    Returns:
        dict: The loaded configuration as a dictionary, or None if not found or on error.
    """
    config_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'config')
    config_filepath = os.path.join(config_dir, f"{config_name}.yml")

    logger.debug("📄 Loading YAML config from: %s", config_filepath)
    try:
        with open(config_filepath, 'r') as file:
            config = yaml.safe_load(file)
            logger.debug('✅ YAML config loaded successfully')
            # Load the entire config to the terminal
            # logger.debug(f'YAML Config Content:\n {config}')
            return config
    except FileNotFoundError:
        logger.error("🚨 YAML config file not found: %s", config_filepath)
        return None
    except yaml.YAMLError as e:
        logger.error("🚨 Error parsing YAML config file: %s", str(e))
        return None
    except Exception as e:
        logger.error("🚨 An undefined error occurred while loading YAML configuration: %s", str(e))
        return None
