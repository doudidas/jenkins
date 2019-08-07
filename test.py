import sys 
locationURL = sys.argv[1]
test = ""
output = locationURL.partition("requests/")[2]
print(output)