import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    i = 0
    while i != 1:
        city = input("Please choose a city; Chicago, New York City, Washington: ").lower()
        if city in cities:
            i = 1
        else:
            i = 0
            print("Please choose a city from Chicago, New York City, or Washington.")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march','april','may','june']
    i = 0
    while i != 1:
        month = input("Please choose from January to June: ").lower()
        if month in months:
            i = 1
        else:
            i = 0
            print("The month you entered is not valid.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    i = 0
    while i != 1:
        day = input("Please choose Monday thorough Sunday: ")
        day = day.lower()
        if day in days:
            i = 1
        else:
            i = 0
            print("The data you entered is not valid.")


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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", common_month)



    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", common_day_of_week)


    # TO DO: display the most common start hour
    common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station is :", common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequent combination of station and end station is : {}, {}"
            .format(common_start_end_station[0], common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time is :", total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time is :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].count()
    print("Counts of user types:", user_counts)


    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("Counts of Gender: ", gender_counts)
    except:
        print("There is no gender data.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = df['Birth Year'].min()
        print("The earliest birth year is: ", earliest_birth_year)
        most_recent_birth_year = df['Birth Year'].max()
        print("The most recent birth year is: ", most_recent_birth_year)
        common_birth_year = df['Birth Year'].mode()
        print("The common birth year is: ", common_birth_year)
    except:
        print("There is no birth data.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def total_data(df):
    raw_data = input('Would you like to see more data? Yes or No: ')
    raw_data = raw_data.lower()

    if raw_data == 'yes':
        print(df.iloc[:5])
        total_data(df)
    else:
        print("End of data")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        total_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
