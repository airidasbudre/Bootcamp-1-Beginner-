score_list =  input("Add all scores? ").split()

highest = None

for i in score_list:
    if highest == None:
        highest = i
    elif int(i) > int(highest):
        highest = i
print(highest)

    

