marks = {
    "raj": 70,
    "deepak": 99,
    "satwik": 100,
    "martha" : 55,
    0 : "blond",
}

#print(marks.items())
#print(marks.keys())
#print(marks.values())
#marks.update({"raj" : 75,"satwik": 80})
#print(marks)

print(marks.get("her"))  #prints none
print(marks.get["her"]) #prints error
