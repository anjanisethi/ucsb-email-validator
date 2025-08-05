# UCSB Email Validator

Created by **Anjani Sethi**  
Program Management Office, UC Santa Barbara ITS  
Undergraduate in Statistics & Data Science + Communication

This is a simple web app buit with [Streamlit](https://streamlit.io/) that helps users identify and export invalid
email addresses from a CSV contact list. It's designed for use with mailing lists that are meant to only
contain '@ucsb.edu' addresses (for internal UCSB communications or campaigns).

## Try it Out

[Launch the app](https://ucsb-email-validator.streamlit.app/)

## Features
- Upload a CSV file containing a designated email column
- Automatically flags valid and invalid emails, with only '@ucsb.edu' emails being considered valid
- Shows a running count of invalid emails row-by-row
- Allows you to download:
  - The full annotated CSV
  - A filtered list of **just the invalid emails**

## Requirements

- Python 3.7+
- pandas
- streamlit

## Project Files

- 'email_validator_app.py' - The main streamlit app
- 'requirements.txt' - Required Python packages for deployment
