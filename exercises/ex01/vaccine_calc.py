"""A vaccination calculator."""

__author__ = "730313954"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

population = int(input("Population: "))
doses_admin = int(input("Doses administered: "))
doses_per_day = int(input("Doses per day: "))
target_percent = int(input("Target percent vaccinated: "))

people_admin = doses_admin / 2
percentage_of_population_admin = people_admin / population
percentage_of_target_left = (target_percent / 100) - percentage_of_population_admin
people_needed_to_be_vaccinated = percentage_of_target_left * population
people_vaccinated_each_day = doses_per_day / 2
number_of_days_until_target_reached = people_needed_to_be_vaccinated / people_vaccinated_each_day

days_needed = round(number_of_days_until_target_reached)

today: datetime = datetime.today()
td_for_target_days: timedelta = timedelta(days_needed)
future: datetime = today + td_for_target_days

target_string = str(target_percent)
days_string = str(days_needed)
future_string = str(future.strftime("%B %d, %Y"))

print("We will reach " + target_string + "% vaccination in " + days_string + " days, which falls on " + future_string)

