import re

# open your csv and read 
with open('file2.csv', 'r') as string:
    csv_text = string.read()

find_string = 'Less than'
replace_string = 'LT'

# substitute the string in file
csv_text_lt = re.sub(find_string, replace_string, csv_text)

find_new_string = 'Single Tent'
replace_new_string = 'ST'

csv_text_st = re.sub(find_new_string, replace_new_string, csv_text_lt)

# open new file and save
new_csv_path = 'file3.csv' 
with open(new_csv_path, 'w') as string:
    string.write(csv_text_st)

print("file3 created")
