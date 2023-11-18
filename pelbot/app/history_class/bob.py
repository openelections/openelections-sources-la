# pelbot/app/history_class/bob.py

import os
from app.utils import logger, load_yaml_config

def config_builder(schema_name="HumanReadableElectionResults"):
    """
    Loads the appropriate config for the historical source(s).
    """
    state = os.getenv("STATE", "LA").upper()
    schema_config = load_yaml_config('sources')

    for source in schema_config.get("sources", {}).get(state, {}).get("historical", []):
        if source.get("name") == schema_name:
            base_url = source["schema"]["base_url"]
            file_pattern = source["schema"]["file_pattern"]
            logger.debug(f'Base URL: {base_url}')
            logger.debug(f'File Pattern: {file_pattern}')
            return base_url, file_pattern

    logger.error(f"Schema named '{schema_name}' not found in sources configuration.")
    return None, None

def builder(election):
    logger.debug(f'Building URL for election data: {election}')
    base_url, file_pattern = config_builder()

    if base_url and file_pattern:
        election_str = str(election)
        YYYY, MM, DD = election_str[:4], election_str[4:6], election_str[6:]
        formatted_file_pattern = file_pattern.replace("MM-DD-YYYY", f"{MM}-{DD}-{YYYY}")
        request_url = base_url.replace("YYYYMMDD", election_str) + formatted_file_pattern
        logger.debug(f'Election data URL: {request_url}')
        return request_url, YYYY
    else:
        logger.error('Configuration data is missing for building the URL.')
        return None
