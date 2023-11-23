import os


def get_file_path():
    print(os.getcwd())


def print_detail(*args):
    """prints firstname, middlename and lastname"""
    print(f"First Name: {args[0][0]}")
    print(f"Middle Name: {args[0][1]}")
    print(f"Last Name: {args[0][2]}")


class FileManipulation:
    def __init__(self, file_name=None, first_name="IKEGBUNAM", middle_name="UDOKIKE", last_name="DANIEL"):
        self._file_name = file_name
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name

    # Create a file and insert first_name, middle_name, and last_name
    def insert_name(self):
        if self._file_name is None or not self._file_name.endswith(".txt"):
            print("Please enter a file name and make sure it ends with .txt")
        else:
            try:
                with open(self._file_name, 'w') as file:
                    # Inserting names in the file
                    file.write(f"{self._first_name}\n")
                    file.write(f"{self._middle_name}\n")
                    file.write(f"{self._last_name}")
                    # File will be created and closed automatically
            except FileNotFoundError:
                print(f"{self._file_name} not found!")
            except PermissionError:
                print(f"You don't have permissions {self._file_name}!")
            except IsADirectoryError:
                print(f"{self._file_name} is a directory not a file!")

    # Read file details
    def read_file(self):
        detail = []
        try:
            with open(self._file_name, 'r') as file:
                for line in file:
                    detail.append(line.strip())
                print_detail(detail)
        except FileNotFoundError:
            print(f"{self._file_name} not found!")
        except PermissionError:
            print(f"You don't have permissions {self._file_name}!")
        except IsADirectoryError:
            print(f"{self._file_name} is a directory not a file!")


# instantiation
obj = FileManipulation("my_details.txt")
obj.insert_name()
obj.read_file()


# Print the absolute path using os
get_file_path()
