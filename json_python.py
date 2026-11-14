import json
a={'name': 'nira','age':20,'dept':'cse'}
ajson=json.dumps(a,indent=5)
print(ajson)

with open('ajson.json','w') as f:
    json.dump(a,f)
    

