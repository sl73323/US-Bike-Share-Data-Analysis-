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
    city=input("Please select a city you would like to  explorre:").lower() 
    while city not in CITY_DATA:
        city=input("City not found, select another one :").lower()
    else:
        df=pd.read_csv(CITY_DATA[city])
    # TO DO: get user input for month (all, january, february, ... , june)
    df['Start Time'] =pd.to_datetime(df["Start Time"])
    df['month'] = df['Start Time'].dt.month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month=input("input a month from january to june: ")
    while month not in months:
        month=input("Input a month from January to June: ")
    else:   
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("input a day of week: ")
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    while day not in days:
          day=input("input a day of week: ")
    else:
        df = df[df['day_of_week'] == day.title()]

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
    df =pd.read_csv(CITY_DATA[city])
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   
    # TO DO: display the most common month
    df['Start Time'] =pd.to_datetime(df["Start Time"])
    df['month'] = df['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    print("most common month is:", popular_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day=df["day_of_week"].mode()[0]
    print("most common day of week:",popular_day)

    # TO DO: display the most common start hour
    df['hour']=df["Start Time"].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station   
    popular_start_station=df["Start Station"].mode()[0]
    print("most popular start station:",popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station=df["End Station"].mode()[0]
    print("most popular end station:",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_comb_station=(df["Start Station"]+"to"+df["End Station"]).mode()[0]
    print("most popular start and end station trip:",popular_comb_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()
    print("total travel time is:",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    print("Mean travel time is :",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type:",user_types)
    # TO DO: Display counts of gender
    if city in ("chicago","new york city"):
        user_gender=df["Gender"].value_counts()
        print("Gener :",user_gender)
    else:
        print("No gender data available")    
 
    # TO DO: Display earliest, most recent, and most common year of birth
    if city in ("chicago","new york city"):
        earliest_year=df["Birth Year"].min()
        recent_year=df["Birth Year"].max()
        common_year=df["Birth Year"].mode()[0]
        print("earliest year, most recent year,most common year of birth:",earliest_year,recent_year,common_year)
    else:
        print("No birth year data available") 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        rawdata=input("do you want to see raw data?")
        if rawdata.lower()=="yes":
            print(df.head(5))
        else:
            break  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        
            

if __name__ == "__main__":
	main()
