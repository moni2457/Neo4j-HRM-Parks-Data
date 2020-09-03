import csv

with open('file1.csv' , 'wb') as output_file:
    with open('DNR_Camping_Parks_Reservation_Data_2016.csv') as csv_file:
        # reading and writing the csv file
        write_file = csv.writer(output_file, delimiter =',')
        file_data = csv.reader(csv_file, delimiter=',')
        for row in file_data:
            write_file.writerow(row)
print("file1 created")
