import requests,json

x = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

res = requests.get(x)
data = json.loads(res.content)
print(data)

li = data["states"]
def get_state_id(state):
    for i in li:
        if i["state_name"] == state:
            print(i["state_id"])
            break

state = input("Enter the state: ")
get_state_id(state)
