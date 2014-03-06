

# This opens the input file and splits it into lines of strings. You'll want to
# remember this for the future -- you'll be using it a lot.
data = open('nycdonors_cleanme.csv', 'r').readlines()

# This list should contain the final output
# I added the header row first
output = [data[0]]

# Here's a little work on the header row to make it consistent with the rest of the data
output[0] = output[0].upper().replace('\n', '').split(',')

# Cleanup the rest of the data
for line in data[1:]:
    # Just a bit of added cleanup because of the file format. Leave this in.
    line = line.replace('\n', '').split(',')

    # Replace the HTML code for 'space' with an actual space.
    line[15] = line[15].replace('&nbsp;', ' ')
    
    # make all strings uppercase
    new_line = []
    for item in line:
    	if isinstance(item, str) == True:
    		item = item.upper()
    		new_line.append(item)	
    	else:
    		pass
    # make the `amount` field a float
    new_line[20] = float(new_line[20])
    output.append(new_line)


print output # This will show your final output