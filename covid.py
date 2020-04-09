import requests

# colors available to use on print statements
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Request fails unless we provide a user-agent
api_response = requests.get(
    'https://thevirustracker.com/free-api?countryTotal=US', headers={"User-Agent": "Chrome"})
covid_stats = api_response.json()['countrydata']

# -- Break out individual stats --
# total cases
print(bcolors.WARNING + "Total Cases:", covid_stats[0]["total_cases"])
# active cases
print("Active Cases:", covid_stats[0]["total_active_cases"])
# new cases today
print("New Today:", covid_stats[0]["total_new_cases_today"])
# total recovered patients
print(bcolors.OKGREEN + "Total Recovered:", covid_stats[0]["total_recovered"])
# total deaths to date
print(bcolors.FAIL + "Total Deaths:", covid_stats[0]["total_deaths"])
# total new deaths today
print("Deaths Today:", covid_stats[0]["total_new_deaths_today"])
