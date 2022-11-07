def letters(str):
    d = {"upper_case" : 0, "lower_case" : 0}
    for i in str :
        if i.isupper():
           d["upper_case"] += 1
        elif i.islower():
            d["lower_case"] += 1
        else: 
            pass 
             
    print(" String : ", str)
    print("upper case count:",d["upper_case"] )     
    print("lower case count : ",d["lower_case"])

letters("VEDant is my Son'S NAMe")