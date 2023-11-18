# Raw Election Data 📊

Welcome to the raw election data directory. This repository contains the unprocessed files directly sourced from the state of Louisiana. These files are the foundational data that undergo further processing in the [openelections-data-la repository](https://github.com/openelections/openelections-data-la).

The data extraction and initial processing are automated using the [PelicanBot](pelbot). For more information on how PelicanBot works and its role in the data processing pipeline, check out the [pelbot](pelbot) directory.

The data cleaning & processing takes place in the [openelections-data-la repo](openelections-data-la) and the final results are stored in the [openelections-results-la repo](https://github.com/openelections/openelections-results-la).

## Directory Structure 📁
The data files in this directory are meticulously organized for ease of navigation and use. The structure is: `YYYY/YYYYMMDD.type`

Where:
    - `YYYY` represents the year of the election.
    - `YYYYMMDD` is the date of the election, formatted as year (YYYY), month (MM), and day (DD).
    - `type` denotes the file format, which can vary depending on the type of data (e.g., CSV, TXT).

**Suggestions about how to improve this structure welcome.**
