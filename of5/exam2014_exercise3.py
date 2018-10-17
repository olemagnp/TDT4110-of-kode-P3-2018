
weather_data = [[12.0, 2.4, 8.2],
                [6.1, 0.6, 11.9],
                [8.3, -3.5, 0.0],
                [11.6, -5.2, 0.0],
                [15.3, 2.8, 14.3]]


def weather_stats(data):
    num_days = len(data)
    total_rain = 0
    maximum_temp = data[0][0]
    maximum_day = 0
    minimum_temp = data[0][1]
    minimum_day = 0

    for i in range(len(data)):
        total_rain += data[i][2]
        if maximum_temp < data[i][0]:
            maximum_temp = data[i][0]
            maximum_day = i
        if minimum_temp > data[i][1]:
            minimum_temp = data[i][1]
            minimum_day = i
    print(f"There are {num_days} days in this period")
    print(f"The highest temp was {maximum_temp} C on day number {maximum_day + 1}")
    print(f"The lowest temp was {minimum_temp} C on day number {minimum_day + 1}")
    print(f"There was a total of {total_rain:.1f} mm rain")

weather_stats(weather_data)