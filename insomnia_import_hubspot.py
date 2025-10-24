import http.client

conn = http.client.HTTPSConnection("api.hubapi.com")

payload = ""

headers = {
    'cookie': "__cf_bm=itbish2rDu5z0wche6UR1f62GfM_omC8o5v9YIVEg08-1761284367-1.0.1.1-ENs_Z.38yXrdELDrUlWnyuTY0y4hsXzsuI.j1Ns7rFf7cUp78KR_Snqh8kGsb5V3TSjZlcLTxQTlr7eTnEk5.8bhnzmnKiKq3fktEuZHHyU",
    'Authorization': "Bearer pat-na1-fb1b6c7c-b8d9-434b-8eeb-06141c774c65"
    }

conn.request("GET", "/crm/v3/objects/contacts?=&limit=20&after%3A20=&properties=email%2Cfirstname", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))