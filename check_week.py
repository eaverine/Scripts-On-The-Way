import datetime

weekDays = ('Week','monday','tuesday','wednesday','thursday','friday','saturday','sunday')

day_date = datetime.date(2006,1,2)

first_day = day_date.replace(day = 1)

if weekDays[first_day.isoweekday()] == 'saturday':
    first_day = day_date.replace(day = 3)  #Make the first day of the week a Monday
if weekDays[first_day.isoweekday()] == 'sunday':
    first_day = day_date.replace(day = 2)  #Make the first day of the week a Monday

print(first_day.isocalendar())
if first_day.month == 1 and first_day.day == 1 and first_day.isocalendar()[1] != 1:
    if day_date.isocalendar()[1] > 6:                   
        week_value = 1                                  
    else:                                               
        week_value = day_date.isocalendar()[1] + 1
else:
    week_value = day_date.isocalendar()[1] - first_day.isocalendar()[1] + 1

print(week_value)
