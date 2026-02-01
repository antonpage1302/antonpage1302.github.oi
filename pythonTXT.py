filename = input("Enter file name (example: myfile.txt): ")
text = input("Enter the text to save: ")

# write to file
with open(filename, "w") as file:
    file.write(text)

print("\nFile saved. Reading file...\n")

# read file
with open(filename, "r") as file:
    content = file.read()

print("File content:")
print(content)
