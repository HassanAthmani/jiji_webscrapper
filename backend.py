import json
import urllib.request


#URL="http://127.0.0.1:5000"
URL="http://35.209.228.31:5000/"
req = urllib.request.Request(URL)
req.add_header('Content-Type', 'application/json; charset=utf-8')



#print(submitInvoice.submitInvoice(payload))
x={"product":"iphone","filter":"n","amount":"5","time":"d"}

body2=json.dumps(x)
jsondata=body2.encode('utf-8')
req.add_header('Content-Length', len(jsondata))

r = urllib.request.urlopen(req, jsondata)
print(r.read().decode()+"\n")