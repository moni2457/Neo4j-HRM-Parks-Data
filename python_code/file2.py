import csv

#read the csv file
with open('file1.csv', 'r') as input_file:
    file_read = csv.DictReader(input_file)
    with open('file2.csv', 'wb') as file_write:
        
        # column names to be included in file
        columnNames = ['ParkName', 'State', 'partySize', 'RateType', 'BookingType', 'Equipment']
        file_output = csv.DictWriter(file_write, fieldnames=columnNames, delimiter =',')
        file_output.writeheader()
        for line in file_read:
            
            # delete the columns not required in the file
            del line['Country']
            del line['Adult']
            del line['Child']
            del line['BookingStartDate']
            del line['BookingEnddate']
            del line['Night']
            del line['Permits']
            file_output.writerow(line)
print("file2 created")
