import csv
import json

dayTypes = []
timeTypes = []
my_json = []
# ETC possible days : ['MF', 'W', 'F', 'MW', 'RECM', 'TUTH', 'RETU', 'RETH', 'M', 'TU', 'RECW']


def possibleDays(days):
    if days not in dayTypes:
        dayTypes.append(days)


def possibleTimeline(time):

    # ETC possible timeline
    # ['9:00 AM', '12:30 PM', '10:00 AM', '5:00 PM', '6:30 PM', '3:30 PM', '10:30 AM', '9:30 AM', '2:00 PM', '4:00 PM', '12:00 PM', '11:30 AM', '3:00 PM']
    # ['11:50 AM', '3:20 PM', '10:20 AM', '6:20 PM', '7:25 PM', '4:50 PM', '5:55 PM', '10:25 AM', '11:23 AM', '1:25 PM', '4:25 PM', '4:55 PM', '2:50 PM',
    # '2:55 PM', '12:20 PM', '11:25 AM', '1:50 PM', '11:20 AM', '4:20 PM', '5:50 PM']
    if time not in timeTypes:
        timeTypes.append(time)


def dayConverter(days):
    if days == 'MF':
        return ['MON', "FRI"]
    elif days == 'W' or days == 'RECW':
        return ['WED']
    elif days == 'F':
        return ['FRI']
    elif days == 'MW':
        return ['MON', 'WED']
    elif days == 'RECM' or days == 'M':
        return ['MON']
    elif days == 'TUTH':
        return ['TUE', 'THU']
    elif days == 'RETU' or days == 'TU':
        return ['TUE']
    elif days == 'RETH':
        return ['THU']
    else:
        return ['NULL']


def timeConverter(time):
    if time == '9:00 AM':
        return '9:00'
    elif time == '12:30 PM':
        return '12:30'
    elif time == '10:00 AM':
        return '10:00'
    elif time == '5:00 PM':
        return '17:00'
    elif time == '6:30 PM':
        return '18:30'
    elif time == '3:30 PM':
        return '15:30'
    elif time == '10:30 AM':
        return '10:30'
    elif time == '9:30 AM':
        return '9:30'
    elif time == '2:00 PM':
        return '14:00'
    elif time == '4:00 PM':
        return '16:00'
    elif time == '12:00 PM':
        return '12:00'
    elif time == '11:30 AM':
        return '11:30'
    elif time == '3:00 PM':
        return '15:00'
    elif time == '11:50 AM':
        return '11:50'
    elif time == '3:20 PM':
        return '15:20'
    elif time == '10:20 AM':
        return '10:20'
    elif time == '6:20 PM':
        return '18:20'
    elif time == '7:25 PM':
        return '19:25'
    elif time == '4:50 PM':
        return '16:50'
    elif time == '5:55 PM':
        return '17:55'
    elif time == '10:25 AM':
        return '10:25'
    elif time == '11:23 AM':
        return '11:23'
    elif time == '1:25 PM':
        return '13:25'
    elif time == '4:25 PM':
        return '16:25'
    elif time == '4:55 PM':
        return '16:55'
    elif time == '2:50 PM':
        return '14:50'
    elif time == '2:55 PM':
        return '14:55'
    elif time == '12:20 PM':
        return '12:20'
    elif time == '11:25 AM':
        return '11:25'
    elif time == '1:50 PM':
        return '13:50'
    elif time == '11:20 AM':
        return '11:20'
    elif time == '4:20 PM':
        return '16:20'
    elif time == '5:50 PM':
        return '17:50'
    else:
        return 'NULL'


with open('./Course List Excel/2022 Spring/ETC.csv', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    line_count = 0
    header = []
    values = []
    for row in reader:
        # in case breaking up with comma affects breaks course title
        # if the csv file is not for major, it is 13
        if (len(row) != 13):
            print(row)
        if line_count == 0:
            for ele in row:
                header.append(ele)
        else:
            for i in range(0, len(row)):
                value = row[i]
                #    0      1     2     3      4       5      6       7          8      9      10         11      12
                # [major, name, title, type, number, credit, days, startTime, endTime, room, instructor, hasLab, link]
                if i == 4:
                    if value != '':
                        value = int(value)
                if i == 5:
                    value = int(value)
                if i == 6:
                    value = dayConverter(value)
                if i == 7 or i == 8:
                    value = timeConverter(value)
                if i == 11:
                    value = False if value == "FALSE" else True
                values.append(value)
            temp_dict = {}
            for i in range(0, len(header)):
                if i == 4:
                    if values[i] != '':
                        temp_dict[header[i]] = values[i]
                else:
                    temp_dict[header[i]] = values[i]

            my_json.append(temp_dict)
            values = []
        line_count += 1

json_object = json.dumps(my_json, indent=2)

with open('etc.json', 'w') as outfile:
    outfile.write(json_object)
