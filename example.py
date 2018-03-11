r"""
This file & \creates empty file
"""

filename = "sample.json"

# Create empty file
def create_file():
    """ This function creates empty file """
    with open(filename, "w") as file:
        file.write("") # writing empty string
