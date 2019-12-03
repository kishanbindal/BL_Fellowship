import re

inp = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91-xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016"

inp = re.sub('<<name>>','Kishan',inp)
inp = re.sub('<<full name>>','Kishan Bindal',inp)
inp =  re.sub('xxxxxxxxxx','9738478938',inp)
inp = re.sub('01/01/2016','03/12/2019',inp)
print(inp)