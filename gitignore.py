# Open the file in read mode
file = open("data.txt", "r")

# Read the entire contents of the file
content = file.read()

# Print the content
print(content)

# Close the file
file.close()

# Open the file in write mode
file = open("data.txt", "w")

# Write content to the file
file.write("Hello, World!")

# Close the file
file.close()