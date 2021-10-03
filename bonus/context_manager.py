from contextlib import contextmanager


class ManageFile:
    def __init__(self, filename_):
        self.__filename = filename_

    def __enter__(self):
        print("Enter...")
        self.__file = open(self.__filename, 'w')
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exit...")
        if self.__file:
            self.__file.close()


@contextmanager
def open_managed_file(filename):
    file = open(filename, "w")
    try:
        yield file
    finally:
        file.close()


if __name__ == "__main__":
    with ManageFile("note.txt") as f:
        f.write("Test...")

    with open_managed_file("note2.txt") as f:
        f.write("Test2...")
