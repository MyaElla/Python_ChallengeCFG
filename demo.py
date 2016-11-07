import requests
import json

res = requests.get('http://www.purgomalum.com/service/json?text=this%20is%20some%20test%20input')

data = res.json()
print data['result']