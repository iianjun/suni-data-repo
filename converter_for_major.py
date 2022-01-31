import csv
import json

dayTypes = []
timeTypes = []
my_json = []


def possibleDays(days):
    if days not in dayTypes:
        dayTypes.append(days)


def possibleTimeline(time):
    if time not in timeTypes:

        timeTypes.append(time)


def dayConverter(days):
    # major
    # major possible days : ['MW', 'TUTH', 'RECM', 'F', 'TU', 'TH', 'M', 'RECW', 'RETU', 'W']
    if days == 'MW':
        return ['MON', 'WED']
    elif days == 'TUTH':
        return ['TUE', 'THU']
    elif days == 'RECM' or days == 'M':
        return ['MON']
    elif days == 'F':
        return ['FRI']
    elif days == 'TU' or days == 'RETU':
        return ['TUE']
    elif days == 'TH':
        return ['THU']
    elif days == 'RECW' or days == 'W':
        return ['WED']


def timeConverter(time):
    # major possible start time: ['3:30 PM', '5:00 PM', '12:30 PM', '10:30 AM', '9:00 AM', '2:00 PM', '9:30 AM']
    # major possible end time: ['4:50 PM', '6:20 PM', '1:25 PM', '11:50 AM', '10:20 AM', '3:20 PM', '1:50 PM', '1:20 PM', '2:55 PM', '4:25 PM', '11:20 AM', '5:55 PM']
    # major
    if time == '3:30 PM':
        return '15:30'
    elif time == '5:00 PM':
        return '17:00'
    elif time == '12:30 PM':
        return '12:30'
    elif time == '10:30 AM':
        return '10:30'
    elif time == '9:00 AM':
        return '9:00'
    elif time == '2:00 PM':
        return '14:00'
    elif time == '9:30 AM':
        return '9:30'
    elif time == '4:50 PM':
        return '16:50'
    elif time == '6:20 PM':
        return '18:20'
    elif time == '1:25 PM':
        return '13:25'
    elif time == '11:50 AM':
        return '11:50'
    elif time == '10:20 AM':
        return '10:20'
    elif time == '3:20 PM':
        return '15:20'
    elif time == '1:50 PM':
        return '13:50'
    elif time == '1:20 PM':
        return '13:20'
    elif time == '2:55 PM':
        return '14:55'
    elif time == '4:25 PM':
        return '16:25'
    elif time == '11:20 AM':
        return '11:20'
    elif time == '5:55 PM':
        return '17:55'


with open('all.csv', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    line_count = 0
    header = []
    values = []
    for row in reader:
        # in case breaking up with comma affects breaks course title
        # if the csv file is not for major, it is 13
        if (len(row) != 12):
            print(row)
        if line_count == 0:
            for ele in row:
                header.append(ele)
        else:
            for i in range(0, len(row)):
                value = row[i]
                #     0        1       2       3        4        5          6           7         8         9           10       11
                # ['major', 'name', 'title', 'type', 'credit', 'days', 'startTime', 'endTime', 'room', 'instructor', 'hasLab', 'link']
                if i == 4:
                    value = int(value)
                if i == 5:
                    value = dayConverter(value)
                if i == 6 or i == 7:
                    value = timeConverter(value)
                if i == 10:
                    value = False if value == 'FALSE' else True
                values.append(value)
            temp_dict = {}
            for i in range(0, len(header)):
                temp_dict[header[i]] = values[i]

            my_json.append(temp_dict)
            values = []

        line_count += 1

json_object = json.dumps(my_json, indent=4)

with open('all_major.json', 'w') as outfile:
    outfile.write(json_object)
