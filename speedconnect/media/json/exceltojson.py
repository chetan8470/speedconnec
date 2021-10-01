import pandas as pd
import json

# excel_file = 'pincode.xlsx'
data = pd.read_csv("pincode.csv") 
# pincode = pd.read_excel(excel_file)
# df = pd.DataFrame(excel_file)
# print(df.head())
pincode_data = {}
for i, j in data.iterrows():
    j_data = j.to_dict()
    # print(i,'\n',j_data['Area'])
    
    if str(j_data['Pin code']) in list(pincode_data.keys()):
        pincode_data[str(j_data['Pin code'])]['area'][str(j_data['Area'])] = {
            'services_for_SDH' : str(j_data['Services for SDH'])
        }
    else:   
        pincode_data[str(j_data['Pin code'])] = {
            'state' : str(j_data['State']),
            'sub_area' : str(j_data['Sub Area']),
            'area' : {
                str(j_data['Area']) : {
                    'service_for_sdn' : str(j_data['Services for SDH'])
                }
            }
        }
    
# print('dic form', pincode_data)
json_object = json.dumps(pincode_data, indent = 4)
with open("pincode.json", "w") as outfile:
    outfile.write(json_object)


   