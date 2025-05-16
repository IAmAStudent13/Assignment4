filename = "output.txt"

write_text = input("Enter text to write to the file: ")
with open(filename, 'w') as file:
    file.write(write_text + '\n')
print("Data successfully written to output.txt.\n")

append_text = input("Enter additional text to append: ")
with open(filename, 'a') as file:
    file.write(append_text + '\n')
print("Data successfully appended.\n")

print("Final content of output.txt:")
with open(filename, 'r') as file:
    print(file.read())
