import time
import pandas as pd
import numpy as np
import utils.constants as constants
import utils.errors as errors


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Which one of the following cities (Chicago, New York or Washington) you want to see it's data ?\n").lower()
            if city not in constants.CITY_DATA.keys():
                raise errors.NotSupportedCity
            break
        except errors.NotSupportedCity:
            print("Invalid city! \n")
        
        
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Which month? all, january, february, ... , june\n").lower()
            if month not in constants.MONTHS and month != 'all':
                raise errors.NotSupportedMonth
            break
        except errors.NotSupportedMonth:
            print("Invalid month! \n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Which day? all, monday, tuesday, ... sunday\n").lower()
            if day not in constants.WEEK_DAYS and day != 'all':
                raise errors.NotSupportedDay
            break
        except errors.NotSupportedDay:
            print("Invalid day!\n")

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
    df = pd.read_csv(constants.CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        month = constants.MONTHS.index(month) +1
        
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['week_day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month= df['month'].mode()[0]
    print(f"The most common month: \n {constants.MONTHS[common_month - 1].title()}")

    # display the most common day of week

    common_day= df['week_day'].mode()[0]
    print(f"The most common day of week: \n {common_day}")

    # display the most common start hour
    start_hour_df = df['Start Time'].dt.hour
    common_hour = start_hour_df.mode()[0]
    print(f"The most common start hour: \n {common_hour}:00")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print(f"The most used start station: \n {common_start_station}")

    # display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print(f"The most used end station: \n {common_end_station}")

    # display most frequent combination of start station and end station trip
    common_combination_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start station and end station trip: \n {common_combination_station}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].sum()
    print(f"The total travel time in sec: \n {total_time}")
    print(f"The total travel time in Hours: \n {total_time/ (60 * 60)}")

    # display mean travel time
    mean_time = df["Trip Duration"].mean()
    print(f"The mean travel time in sec: \n {mean_time}")
    print(f"The mean travel time in Hours: \n {mean_time/ (60 * 60)}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"The counts of user types: \n {user_types}")

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print(f"The counts of gender: \n {gender}")

    # Display earliest, most recent, and most common year of birth
    earliest_yof = int(df['Birth Year'].min())
    recent_yof = int(df['Birth Year'].max())
    common_yof = int(df['Birth Year'].mode()[0])
    
    print(f"The earliest year of birth: \n {earliest_yof}")
    print(f"The most recent year of birth: \n {recent_yof}")
    print(f"The most common year of birth: \n {common_yof}")
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
