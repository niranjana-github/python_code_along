import json
a={'name':'nira','age':20,'dept':'dsbs'}
with open('ajson.json','r') as f:
    a=json.load(f)
    print(a)