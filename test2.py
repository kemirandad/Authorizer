from datetime import datetime

CONST = 200000000

date = '2019-02-13T10:00:00.000Z'
date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
date = date.strftime('%Y%m%d%H%M%S%f')

date2 = '2019-02-13T11:00:00.000Z'
date_number2 = datetime.strptime(date2, '%Y-%m-%dT%H:%M:%S.%fZ')
date_number2 = date_number2.strftime('%Y%m%d%H%M%S%f')

print(date)

"""
if int(date_number2[:12]) - int(date_number[:12]) <= CONST:
    print(True)
print(False)
"""