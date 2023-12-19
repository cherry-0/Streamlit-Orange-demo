file_path = './requirements.txt'

# Read the contents of the file
with open(file_path, 'r') as file:
    content = file.read()

# Replace '=' with '==' in the content
modified_content = content.replace('=', '==')

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(modified_content)

print(f"The file {file_path} has been modified.")