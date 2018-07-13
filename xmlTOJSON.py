import json
import xmltodict
import datetime

def formatDate():
	dt = datetime.datetime.now()
	return dt.strftime("%d/%m/%Y")

with open("C:\\Users\\90499\\XMLtranslation\\strings.xml") as fd:
    XMLstring = fd.read()

rawJSON = xmltodict.parse(XMLstring)

# insert formatting code here and initialize finalJSON

userName = input("Who are you: ")
for objs in rawJSON["resources"]["string"]:
	objs["Screen_Name"] = objs["@name"]
	del objs["@name"]
	objs["Owner"] = "Sehun Park"
	objs["OtherLanguages"] = [{'Contents': objs["#text"], 'Language': 'English', 'Editor': userName, 'Date': formatDate()}]
	del objs["#text"]

for objsArrs in rawJSON["resources"]["string-array"]:
	objsArrs["Screen_Name"] = objsArrs["@name"]
	del objsArrs["@name"]
	objsArrs["Owner"] = "Sehun Park"
	objsArrs["OtherLanguages"] = [{'Contents': objsArrs["item"], 'Language': 'English', 'Editor': userName, 'Date': formatDate()}]
	del objsArrs["item"]

	
# End of formatting code

finalJSONString = json.dumps(rawJSON, indent=4)
print("\nFinal JSON output(output.json):")
print(finalJSONString)
 
with open("C:\\Users\\90499\\XMLtranslation\\output.json", 'w') as f:
    f.write(finalJSONString)
	
wait = input("All done. Press enter to continue: ")
