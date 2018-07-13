import json
import xmltodict
import datetime
 
with open("C:\\Users\\90499\\XMLtranslation\\strings.xml") as fd:
    XMLstring = fd.read()

rawJSON = xmltodict.parse(XMLstring)

# insert formatting code here and initialize finalJSON

names = []
for objs in rawJSON["resources"]["string"]:
  #Add the code here

# End of formatting code

finalJSONString = json.dumps(rawJSON, indent=4)
print("\nFinal JSON output(output.json):")
print(finalJSONString)
 
with open("C:\\Users\\90499\\XMLtranslation\\output.json", 'w') as f:
    f.write(finalJSONString)
	
wait = input("All done. Press enter to continue: ")
