import datetime

'''Returns the number of minutes between start and end time'''
# EXAMPLE startime = "17:35"
def minutesBetween(start_time, end_time):
    (s_hr, s_min) = start_time.split(':') #s_hr, s_min : start minute and start hour
    (e_hr, e_min) = end_time.split(':') #e_hr, e_min : end minute and start hour

    # start and end time objects
    s_dt = datetime.timedelta(hours=int(s_hr), minutes=int(s_min))
    e_dt = datetime.timedelta(hours=int(e_hr), minutes=int(e_min))

    difference = e_dt - s_dt
    result = str(difference).split(":")
    ##print(result)
    r_hr = int(result[0])

    if r_hr > 0:
        return r_hr*60 + int(result[1])
    else:
        return int(result[1])


# if __name__ == '__main__':
#     print(minutesBetween("15:20", "17:55"))