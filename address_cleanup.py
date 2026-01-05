import re
import pandas as pd

def address_extract(input_add):
    # Setup dictionary for ouput storage
    split_add = [None]*5


    # Clean input address string, set to lowercase and seperate into a list
    input_add = input_add.strip().lower().split(",")


    # Ensure list has at minimum street, city, province (3) elements - flag if not
    if len(input_add) < 3:
        raise Exception('Address not complete or missing seperators: ' + ''.join(input_add))


    # Identify the postal code, remove from address string, format with space and save to dictionary
    postal = re.search(r" (\D\d\D \d\D\d)| (\D\d\D\d\D\d)",input_add[-1])
    if not postal:
        raise Exception('Postal code is incorrect or not found.'+ ''.join(input_add))
    
    input_add[-1] = re.sub(r" (\D\d\D \d\D\d)| (\D\d\D\d\D\d)", "",input_add[-1])
    split_add[4] = postal.group().strip()
    
    if split_add[4][3] != " ":
        split_add[4] = split_add[4][:3]+" "+split_add[4][3:]
    split_add[4] = split_add[4].upper()


    # Extract the province, format to 2 letter form and save
    province = input_add.pop().strip()
    province = re.sub(r'[^a-z]', '', province)

    province_abbrev = {
    'alberta': 'ab',
    'british columbia': 'bc',
    'manitoba': 'mb',
    'new brunswick': 'nb',
    'newfoundland and labrador': 'nl',
    'northwest territories': 'nt',
    'nova scotia': 'ns',
    'nunavut': 'nu',
    'ontario': 'on',
    'prince edward island': 'pe',
    'quebec': 'qc',
    'saskatchewan': 'sk',
    'yukon': 'yt'
    }

    for key in province_abbrev:
        if key == province:
            province = province_abbrev[key]

    if province not in province_abbrev.values():
        raise Exception('Province incorrect or not found.')

    split_add[3] = province.upper()


    # Extract and save city information w/ formatting
    split_add[2] = input_add.pop().strip().title()


    # Check and save unit number is present, else save city information
    if len(input_add) > 1:
        for location,value in enumerate(input_add):
            find = re.search(r"\d+ \S+.*", value)
            if find != None:
                input_add.pop(location)
        split_add[1] = find.group().title().strip()
        split_add[0] = input_add.pop().title().strip()
    else:
        split_add[1] = input_add.pop().title().strip()

    return split_add


# Open file in read and get all addresses in a list
input_file = open("inputs.txt", "r")
inputs = input_file.read().splitlines()

# Setup dictionary to store cleaned addresses
clean_addr_dict = dict.fromkeys(['Unit','Street Address','City','Province','Postal Code'])
for keys in clean_addr_dict:
    clean_addr_dict[keys] = []

# Run cleaning & save to dictionary
for addresses in inputs:
    output = address_extract(addresses)
    clean_addr_dict['Unit'].append(output[0])
    clean_addr_dict['Street Address'].append(output[1])
    clean_addr_dict['City'].append(output[2])
    clean_addr_dict['Province'].append(output[3])
    clean_addr_dict['Postal Code'].append(output[4])

#Create data frame and output to excel
output = pd.DataFrame.from_dict(clean_addr_dict)
output.to_excel('outputs.xlsx',index=False)
print (output)