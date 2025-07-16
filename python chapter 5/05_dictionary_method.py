mydict = {
    "fast" : "In a quick manner",
    "prem" : "student",
    "marks" : "100",
    "another mydict" : {"harry": "player"},
    1 : 2
}
# Dictionary methods

print(list(mydict.keys()))
print(mydict.values())
print(mydict.items())
print(mydict)

updatemydict = {
    "lokesh" : "friend",
    "shayam" : "worker"
}
mydict.update(updatemydict)
print(mydict)

print(mydict.get("prem"))
print(mydict["prem"])


print(mydict.get("prem2"))
print(mydict["prem2"])