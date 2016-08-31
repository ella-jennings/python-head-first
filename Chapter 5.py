line = "101; Johnny 'wave-boy' Jones; USA; 8.32; Fish; 21"
s = {}

#split hash into parts every time a semicolon is seen
(s['ID'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")

#display in the format below
print("ID: " + s['ID'])
print("Name:    " + s['name'])
print("Country: " + s['country'])
print("Average: " + s['average'])
print("Board:   " + s['board'])
print("Age:     " + s['age'])

def find_details(id2find):
    #open file to read data
    surfers_f = open("surfing_data.csv")
    #for loop to look through each line of file
    for each_line in surfers_f:
        #hash starts empty
        s = {}
        #line split assigns data to the hash using multiple assignment
        (s['ID'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(";")
        #check if ID supplied as a parameter is the same as the one from the file
        if id2find == int(s['id']):
            surfers_f.close()
            #a match will return the current hash
            return(s)
    surfers_f.close()
    #no match will return an empty hash
    return({})