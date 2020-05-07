"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

with open('src/foo.txt') as foo:
    read_data = foo.read()
    print(read_data)

#if using `with`, the file is automatically closed after the block ends.
assert foo.closed == True, "Should be True"

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('src/bar.txt', 'w') as bar:
    txt = """line 1
line 2
line 3"""
    bar.write(txt)

with open('src/bar.txt') as bar:
    assert bar.read() == """line 1
line 2
line 3""", "Should match string exactly"