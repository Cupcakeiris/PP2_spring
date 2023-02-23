import json

with open("C:\KBTU\\2nd semester\pp2\TSIS4\json\sample-data.json") as f:
    data = json.loads(f.read())

print("Interface Status")
print("============================================================================================================")
print("DN\t\t\t\t\t\tDescr\t\t\tSpeed\t\t\tMTU")
print("--------------------------------------------\t----------------------\t---------------------\t------------")

i = 0
for line in data["imdata"]:
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["dn"], end="\t\t\t")
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["descr"], end="\t")
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["speed"], end="\t\t\t")
    print(data["imdata"][i]["l1PhysIf"]["attributes"]["mtu"], end="\t")
    print()
    i += 1