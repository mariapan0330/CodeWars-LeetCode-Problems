# Time: O(1) | Space: O(1)

def possible_times(time):
    hour_count = 0
    minute_count = 0

    # figure out hours
    # if ?0
    if time[0] == "?" and time[1] != "?":
        for n in range(0,3):
            if int(str(n) + str(time[1])) <= 23:
                hour_count += 1
            else:
                break
    
    # if 0?
    if time[0] != "?" and time[1] == "?":
        for n in range(0,10):
            if int(str(time[0]) + str(n)) <= 23:
                hour_count += 1

    # if ??
    if time[0] == "?" and time[1] == "?":
        hour_count = 24;



    # figure out minutes
    # if ?0
    if time[3] == "?" and time[4] != "?":
        for n in range(0,6):
            if int(str(n) + str(time[4])) <= 59:
                # print(int(str(n) + str(time[4])))
                minute_count += 1
            else:
                break
    
    # if 0?
    if time[3] != "?" and time[4] == "?":
        for n in range(0,10):
            if int(str(time[3]) + str(n)) <= 9+(10*int(time[3])):
                # print(int(str(time[3]) + str(n)))
                minute_count += 1

    # if ??
    if time[3] == "?" and time[4] == "?":
        minute_count = 60;


    # print(f"{hour_count} {minute_count}")    
    if hour_count > 0 and minute_count > 0:
        return hour_count * minute_count
    elif hour_count > 0:
        return hour_count
    elif minute_count > 0:
        return minute_count
    else:
        return 1
    



print(possible_times("?3:00")) # 2
print(possible_times("??:??")) # 1440
print(possible_times("0?:1?")) # 100
print(possible_times("?0:?0")) # 18
print(possible_times("??:24"))