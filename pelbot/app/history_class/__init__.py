# pelbot/app/history_class/__init__.py

from app.utils import logger
from .request import make_get_request
from .bob import builder

def make_history(election):
    logger.info(f"Getting data for election: {election}")
    request_url, YYYY = builder(election)
    if request_url:
        response = make_get_request(request_url, YYYY, election)
        if response:
            return True
        else:
            logger.error(f"Failue: {election}")
    else:
        logger.error(f"Failed to build request URL for election: {election}")
    return True
