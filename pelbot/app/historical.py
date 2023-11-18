# pelbot/app/historical.py
"""
Captures historical election results.
"""
from .utils import logger, load_yaml_config
from datetime import datetime
from .history_class import make_history

def capture_history(capture_range):
    logger.info('Beginning historical import')
    try:
        if capture_range == "all":
            get_all()

        elif len(capture_range) == 4 and capture_range.isdigit():  # Check if the input is a year (YYYY)
            logger.info(f'Getting elections for year: {capture_range}')
            get_election_info(year=capture_range)

        elif len(capture_range) == 6 and capture_range.isdigit():  # Check if the input is a year and month (YYYYMM)
            logger.info(f'Getting elections for month: {capture_range[4:6]}, year: {capture_range[:4]}')
            get_election_info(year=capture_range[:4], month=capture_range[4:6])

        elif len(capture_range) == 8 and capture_range.isdigit():  # Check if the input is a year, month, and day (YYYYMMDD)
            logger.info(f'Getting elections for date: {capture_range}')
            get_election_info(year=capture_range[:4], month=capture_range[4:6], day=capture_range[6:8])

        else:
            logger.error(f"Invalid date format provided: {capture_range}")

    except Exception as e:
        logger.error(f"An error occurred while determining what to get: {e}", exc_info=True)


def get_election_info(year=None, month=None, day=None):
    logger.debug(f'Fetching election data for: Year={year}, Month={month}, Day={day}')
    raw_election_config = get_election_config(year, month, day)

    # Extract just the date items from raw election config
    elections = [election['date'] for election in raw_election_config]

    # Log the election dates we're about to process
    logger.info(f'Processing Elections: {elections}')
    for election in elections:
        try:
            success = process_election_data(election)
            if success:
                logger.info(f'Successfully processed election data for: {election}')
            else:
                logger.error(f'Failed to process election data for: {election}')
        except Exception as e:
            logger.error(f"An error occurred while processing election data for {election}: {e}", exc_info=True)

def process_election_data(election):
    election_data = make_history(election)
    if election_data is None:
        raise ValueError("Failed to process history data for the election.")
    return True


def get_all():
    logger.info('Fetching all elections data')
    current_year = datetime.now().year
    for year in range(1982, current_year + 1):
        get_election_info(year=str(year))

def get_election_config(year=None, month=None, day=None):
    try:
        all_config = load_yaml_config('elections')
        if all_config is None:
            raise ValueError("Elections configuration could not be loaded.")

        applicable_elections = []

        # Convert year to integer for dictionary key lookup
        int_year = int(year)

        # Access the Louisiana elections data
        la_elections = all_config.get('elections', {}).get('la', {})

        # If year is specified, filter the election dates for that year
        if int_year in la_elections:
            for election in la_elections[int_year]:
                date = str(election['date'])
                # Check if the date matches the provided month and/or day
                if (month is None or date[4:6] == month) and \
                   (day is None or date[6:8] == day):
                    applicable_elections.append(election)

        logger.info(f"Found {len(applicable_elections)} applicable elections for {year}.")
        return applicable_elections

    except Exception as e:
        logger.error(f"An error occurred while loading the elections configuration: {e}", exc_info=True)
        return None


