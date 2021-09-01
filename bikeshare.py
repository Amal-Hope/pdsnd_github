import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_f = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    great = input("Hi I'm Amal ^_^, What is your name: ")
    print("Hello! {} I hope you fine Let\'s explore some US bikeshare data!".format(great))
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nPlease enter which city you want explore it chicago, "
                     "new york city or washington?\n").lower()
        if city in CITY_DATA:
            break
        else:
            print("\nSorry, type city name correct!")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWant from you choose month from the six first months "
                      "January to June to filter it or all for 'all'?\n").lower()
        if month in month_f:
            break
        else:
            print("\nSorry, choice month from the six first!")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nwhich day you will to filter or type 'all' for all?\n").lower()
        if day in('monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                  'saturday', 'sunday', 'all'):
            break
        else:
            print("\nSorry, type day name correct!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.day_name()

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) +1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df["month"].mode()[0]
    print("\nThe most common month is:", common_month)
    # display the most common day of week
    common_day = df["day"].mode()[0]
    print("\nThe most common day is:", common_day)
    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    common_hour = df["hour"].mode()[0]
    print("\nThe most common start hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df["Start Station"].mode()[0]
    print("\nThe most commonly used start station is:", start_station)
    # display most commonly used end station
    end_station = df["End Station"].mode()[0]
    print("\nThe most commonly used end station is:", end_station)
    # display most frequent combination of start station and end station trip
    combination_station = (df["Start Station"] + " " + df["End Station"]).mode()[0]
    print("\nThe most frequent combination of start station and end station trip "
          "is: ", combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df["Trip Duration"].sum()
    print("\nThe total travel time is: ", total_travel)
    # display mean travel time
    avg_travel = df["Trip Duration"].mean()
    print("The average travel time is: ", avg_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nCounts of users types is: ", df["User Type"].value_counts())
    # Display counts of gender
    if "Gender" in df:
        print("\nCounts of gender is: ", df["Gender"].value_counts())
    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest = df["Birth Year"].min()
        print("Earliest year of birth is: ", earliest)
        most_recent = df["Birth Year"].max()
        print("\nMost recent year of birth is: ", most_recent)
        most_common = df["Birth Year"].mode()[0]
        print("\nMost common year of birth is :", most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw(df):
    raw = 0
    while True:
        display = input("\nDo you want to display five new lines of data? y/n: \n").lower()
        if display == "y":
            print(df[raw:raw+5])
            raw += 5
        elif display == "n":
            break
        else:
            print("Please enter 'y' or 'n' !!")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
