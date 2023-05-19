#used to store information which comes in a key value pair each
#for example Name: johnsmith .... in this name is key smith is value
customer = {
    "name": "john Smith",
    "age": 30,
    "age2": 40,# value can be as string boolean or int
    "is_verified": True
}
print(customer["name"])
print(customer.get("name"))#difference is it returns none if undefined key is called
print(customer.get("day", "Jan 1 1980")) # in this as day is not defined we are optionally adding Jan 1.....
print(customer.get("name", "johnny"))# you can see ebethough we specified the names it took first defined name only
customer["birthdate"] = "Jan 1 1980"
print(customer) #we can add values to dictionary later also