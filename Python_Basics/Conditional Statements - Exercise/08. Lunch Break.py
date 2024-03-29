from math import ceil

movie = input()
time_episode = int(input())
time_break = int(input())

time_lunch = time_break * 0.125
time_rest = time_break * 0.25

time_left = time_break - time_lunch - time_rest

if time_episode <= time_left:
    time_left -= time_episode
    print(f'You have enough time to watch {movie} and left with {ceil(time_left)} minutes free time.')
else:
    time_episode -= time_left
    print(f"You don't have enough time to watch {movie}, you need {ceil(time_episode)} more minutes.")
