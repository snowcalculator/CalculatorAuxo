def add_time(start, duration, start_day=None):
    
    # Split the start time into hour, minute and period (AM or PM)
    start_time_reformat = start.replace(':', ' ')
    start_time_split = start_time_reformat.split(' ', 3)

    # Split the duration into hour and minute
    duration_split = duration.split(':', 2)
    if int(duration_split[1]) >= 60:
        return "Error: duration minutes should be less than 60"
    
    # Add minutes and determine if minutes exceed 60:
    minutes = int(duration_split[1]) + int(start_time_split[1])
    if minutes >= 60:
        minutes_final = minutes - 60
        hour_to_add = 1
    else:
        hour_to_add = 0
        minutes_final = minutes

    if minutes_final == 0 or minutes_final < 10:
        minutes_final = str("0")+ str(minutes_final)
    
    # Converting the hours into military time
    if start_time_split[2] == "PM" and int(start_time_split[0]) < 12:
        start_military_hour = 12 + int(start_time_split[0])
    else:
        start_military_hour = int(start_time_split[0])

    # Adding the hours 
    hour_military = start_military_hour + int(duration_split[0]) + hour_to_add
    
    # Return to 12-hour format
    hour_final = hour_military % 12
    if hour_final == 0:
        hour_final = 12
    
    # Determining the period (AM or PM)
    hour_period = hour_military % 24
    if hour_period < 12:
        period = "AM"
    if hour_period >= 12:
        period = "PM"
    if hour_period == 0:
        period = "AM"
    
    # Determining the number of days
    if hour_military < 24:
        final_day = ""
        days_n = 0
    if hour_military < 48 and hour_military >= 24:
        final_day = " (next day)"
        days_n = 1
    if hour_military >= 48 :
        days = hour_military / 24
        days_n = str(days).split(".",2)[0]
        final_day = f" ({days_n} days later)"

    # Indicate the day
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    # User gave the start day
    if start_day:
        start_day_index = days.index(start_day.lower())
        final_day_index = (start_day_index + int(days_n))%7
        final_day_name = days[final_day_index].capitalize()
        # If end day is same as start day
        if final_day_name.lower() != start_day.lower():
            new_time = f"{hour_final}:{minutes_final} {period}, {final_day_name}{final_day}"
        # End day is not same as start day
        else:
            new_time = f"{hour_final}:{minutes_final} {period}, {final_day_name}"

    # User did not give the start day
    else:
        final_day_name = ""
        new_time = f"{hour_final}:{minutes_final} {period}{final_day}"

    return new_time
