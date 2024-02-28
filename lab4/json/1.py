import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open("data.json", "r") as file:
    s = json.load(file)
    for item in s["imdata"]:
        print(f"{item['l1PhysIf']['attributes']['dn']}                               {item['l1PhysIf']['attributes']['speed']}  {item['l1PhysIf']['attributes']['mtu']}")