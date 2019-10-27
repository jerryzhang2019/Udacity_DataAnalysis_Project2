
# coding: utf-8

# In[3]:


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
    while True:
        city=input('Would you like to see data for Chicago,New York City,or Washington?').lower()
        global a_city
        a_city=city
        if city in ['chicago','new york city','washington']:
            break
        else:
            print('please input correct city name')
        
    #TO DO:get user input for month (all,january,february,...,june)
    while True:
        month=input('Which month? January,February,March,April,May,or June.').lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print('please input correct month')
                    
    #TO DO:get user input for day of week (all,monday,tuesday,...sunday)
    while True:
        day=input('Which day?Please input all,monday,tuesday...saturday,or sunday.').lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print('please input correct day')
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
      # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1   
        # filter by month to create the new dataframe
        df = df[df['month']==month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df =df[df['day_of_week']==day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
        # TO DO: display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create an month column
    df['month'] =df['Start Time'].dt.month
    # find the most common month (from 0 to 11)
    popular_month = df['month'].mode()[0]    
    print("\nMost popular month:", popular_month)
    # TO DO: display the most common day of week
    # extract day from the Start Time column to create an day column
    df['day'] =df['Start Time'].dt.day
    # find the most common day (from 0 to 6)
    popular_day = df['day'].mode()[0]    
    print("\nMost popular day:", popular_day)
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]    
    print("\nMost poupular hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station   
    popular_StartStation = df['Start Station'].mode()[0]    
    print('Most commonly used start station:', popular_StartStation)
    # TO DO: display most commonly used end station
    popular_EndStation = df['End Station'].mode()[0]    
    print('Most commonly used end station:', popular_EndStation)
    # TO DO: display most frequent combination of start station and end station trip
    combination_trip=df['Start Station'].astype(str)+' to '+df['End Station'].astype(str)
    combination_trip.describe()
    popular_combination_trip=combination_trip.describe()['top']
    print('Most frequent combination of start station and end station:',popular_combination_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #TO DO: display total travel time 
    total_TravelTime=df['Trip Duration'].sum()
    print('Total travel time:',total_TravelTime)
    # TO DO: display mean travel time 
    mean_TravelTime=df['Trip Duration'].mean()
    print("\nMean travel time:",mean_TravelTime)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if a_city in ['chicago','new york city']:
        gender=df['Gender'].value_counts()
        print(gender)    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest=df['Birth Year'].min()
        print('earliest year of bitrh:',earliest)
        most_recent=df['Birth Year'].max()
        print('most recent year of bitrh:',most_recent)
        most_common=df['Birth Year'].mode()[0]
        print('nost common year of birth:',most_common)
    else:  
        print("\nThis city does'nt has Gender and Birth Year.")
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

