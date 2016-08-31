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

