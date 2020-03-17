# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================
def findStationID(ID):
    global data
    i = 0
    sum = 0
    for row in data:
        if (row['station_id'] == ID):
            i += 1
            sum += float(row['PRES'])
    if (sum == 0):
        return [ID, 'NONE']
    else:
        return [ID, sum / i]
        
# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061240.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# Retrive ten data points from the beginning.

i = 0
while (i < len(data)):
    if (data[i]['PRES'] == '-99.000' or data[i]['PRES'] == '-999.000'):
        del data[i]
        i -= 1
    i += 1

output = []
output.append(findStationID('C0A880'))
output.append(findStationID('C0F9A0'))
output.append(findStationID('C0G640'))
output.append(findStationID('C0R190'))
output.append(findStationID('C0X260'))
#=======================================

# Part. 4
#=======================================
# Print result
print(output)
#========================================