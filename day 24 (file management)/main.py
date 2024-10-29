# OPEN THE FILE AND READ THE FILE

# file = open("my_file.txt")  # open the file
# contents = file.read()  # read the file content
# print(contents)

# file.close()  # to save resources, thus save laptop load

## or

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# same thing just without file.close() to prevent forgot to write the code

#   WRITE THING ON THE FILE.TXT USING PYTHON, WITH DELETE THE PREVIOUS ONE

# mode by default is read only
# w = write, a = append
with open("my_file.txt", mode="a") as file:
    file.write("a bunch of text 3")
