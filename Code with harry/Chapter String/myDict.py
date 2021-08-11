myDict = {
    "guru" : "prasad",
    "tejal" : "gharte",
    "satyawan": "Mrunali",
    "vipul" : "mj wali",
    2 : 20
}
print(myDict.keys()) # this is used for the get all keys from the dictionary
print(myDict.values()) # This is used for the getting vlue of all values from the  dictionary
print(myDict.items()) # This is used for getting the all contents  from the dictionary 

updatedDict = {
   " Bhushan" : "bhushnali"
}
myDict.update(updatedDict) # update the dictionary as "key value" pair
print(myDict)


# print(myDict.get("vipull"))
# print(myDict["guruu"]) # it throws an error but it will not throws an error 
print(myDict.get("satywan"))
print(myDict["tejall"])# its throws an error bcoz we did not use a get method always use it