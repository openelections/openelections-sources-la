<div align="center">
 <img src="./assets/header.png"/></a>
</div>

PelicanBot is an automated tool designed to scrape and collect election result data for the state of Louisiana from the Secretary of State's website. It is a part of the OpenElections project, a volunteer-driven effort to make election data freely available and easily accessible to the public.

## Getting Started
The following instructions will guide you through setting up Pelican Bot and running it to scrape election results data:

1. **Set Up Environment Variables:**
    - Duplicate the `.env-template` file and rename the duplicate to `.env`.
    - Configure the necessary environment variables within the `.env` file as needed for your scraping session.
    - The `CAPTURE_RANGE` determines what election data to import. The default configuration is set to export all election data for the year 2022. These are the various options for that variable:

    | Option | Output |
    |-----------|-----------|
    | `YYYY`     | All elections for that year |
    | `YYYYMM`   | All election(s) for that month |
    | `YYYYMMDD` | Election data from that day |
    | `all` | All Election Data |


2. (Optional) **Configure the Config Files:**
   - Navigate to the `config` directory within Pelican Bot.
   - Adjust the YAML configuration files to your liking. You don't need to though...


3. **Run Pelican Bot:**
   - Activate the env:

     ```
     poetry shell
     ```

   - Tell the pelican to fly:
     ```
     python3 -m run
     ```

   - PelicanBot *should* begin downloading the election data files.

## Project Structure
- `app`: Contains the core application logic for the bot, including modules for historical data scraping and live data collection.
- `config`: YAML files that define scraping parameters and source URLs.
- `.env`: Environment configuration file where scraping session variables can be set.
- `run.py`: The main runner script for initiating scraping sessions.

## Contributing
If you wish to contribute to Pelican Bot or the OpenElections project, please refer to the [openelections-core repository](https://github.com/openelections/openelections-core) for guidelines on contributing and collaboration.
