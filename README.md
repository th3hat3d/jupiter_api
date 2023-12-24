# The Jupiter API
An API to make automated retrieving of stats and data from the Jupiter grading system easier for students and teachers. Currently in its beta stage for now, and new features will be released as soon as I can implement them.

## Install Locally
To install, run `pip3 install -r requirements.txt` to retrieve the necessary modules. After this, run `python3 app.py` to host the API.
Additionally, install Docker and run: `docker pull selenium/standalone-chrome` and `docker run --rm -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome`

## Basic Usage
Usage of the API will be fully documented when I get the chance. For now, here's the basic format for all API queries:
```
user=<your username>&pass=<your password>
```
To switch terms, include a `school_year` parameter, with the value being in `<year1><year2>` format.
Example:
```
school_year=20212022
```
## Features
Current features:
- List classes
- Switch between school terms
- Download profile picture

List of features to implement:
- [x] HTTPS in the Flask API
- [ ] Automatic handling of browser instances
- [ ] Rate limiting
- [x] Listing teachers (will fix commas for multiple teachers soon)
- [x] Calculating (MP) GPA
- [ ] Listing assignment grades
- [x] Calculating class averages and letter grades
- [ ] View to-do list
- [ ] Listing class assignments
- [ ] All features under teacher accounts

No credentials are ever seen by me on my hosted instance (https://jupiterapi.deadandbeef.com). I swear on my life.
