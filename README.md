# Canadian Address Cleanup
Converts a list of Canadian addresses stored in a text file to an excel file with the address components seperated.

## Getting Started
### Prerequisites
Ensure both **regex and pandas** are pre-installed for your python instance

### Setup
- Create an inputs.txt file with addresses seperated by line
- Ensure addresses do not have commas or periods preceeding or following them
- Add commas to seperate the unit number field if not present already

### Running the program
- If run successfully, the outputs will be generated as an excel file with the name ***outputs***.  
- If ran via CLI, the program also outputs the results to the console.

## Examples
### Example  of inputs.txt
```
5, 827 12th Street, Parksville, BC V9P 8S8  
284 Orenda Rd, Unit 5, Brampton, ON L6T 5S3  
4180 Duke of York Blvd, Mississauga, ON L5B 0H7
```
### Output shown in console
```
        Unit          Street Address         City Province Postal Code
0          5         827 12Th Street   Parksville       BC     V9P 8S8
1     Unit 5           284 Orenda Rd     Brampton       ON     L6T 5S3
2       None  4180 Duke Of York Blvd  Mississauga       ON     L5B 0H7
```
***Note:*** The unit numbers of the first two addresses are seperated from the street address with a comma. Each line is representative of an address.