def find_details(id2find):
    #open file to read data
    surfers_f = open("surfing_data.csv")
    #for loop to look through each line of file
    for each_line in surfers_f:
        #hash starts empty
        s = {}
        #line split assigns data to the hash using multiple assignment every time semicolon is seen
        (s['ID'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(";")
        #check if ID supplied as a parameter is the same as the one from the file
        if id2find == int(s['ID']):
            surfers_f.close()
            #a match will return the current hash
            return(s)
    surfers_f.close()
    #no match will return an empty hash
    return({})

lookup_ID = int(input("Enter the ID of the surfer: "))
surfer = find_details(lookup_ID)
if surfer:
    # display in the format below
    print("ID: " + surfer['ID'])
    print("Name:    " + surfer['name'])
    print("Country: " + surfer['country'])
    print("Average: " + surfer['average'])
    print("Board:   " + surfer['board'])
    print("Age:     " + surfer['age'])