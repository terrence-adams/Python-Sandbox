import requests
import json


r = requests.get('https://jsonplaceholder.typicode.com/posts')
#print(r.text)


with open('jsonExample1.json','w') as json_file:
    #json_file.write(json.dumps(r.text, sort_keys=True, indent= 3))
    json_file.write(r.text)
    #json_file.close()


with open('jsonExample1.json','r') as json_file:
    pyDict = json_file.read()


print(type(r.text))
print(type(pyDict))









