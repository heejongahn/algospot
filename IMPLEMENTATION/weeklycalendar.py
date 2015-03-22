##### Problem
#

##### Input
#

##### Output
#

dow_hash = {'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4,
            'Friday':5, 'Saturday':6}

permonth_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def week_to_string(week):
    week = [str(date) for date in week]
    output = ""
    for i in range(6):
        output = output + "%s " % week[i]

    output += week[6]

    return output


n = int(input())

for case in range(n):
    (month, day, dayoftheweek) = input().split(" ")
    (month, day) = (int(month)-1, int(day))
    dow = dow_hash[dayoftheweek]

    prior_month = (month + 11) % 12

    permonth = permonth_list[month]
    prior_permonth = permonth_list[prior_month]

    week = []

    for i in range(dow):
        week.append(day-dow+i)
    for i in range(7-dow):
        week.append(day+i)

    for i in range(7):
        if week[i] > permonth:
            week[i] = week[i] % permonth
        elif week[i] <= 0:
            week[i] = week[i] + prior_permonth

    print(week_to_string(week))
