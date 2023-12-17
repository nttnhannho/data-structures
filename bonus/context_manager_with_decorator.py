from contextlib import contextmanager


@contextmanager
def manage_file(file_path):
    file = open(file_path, 'w')
    try:
        yield file
    finally:
        file.close()


def main():
    with manage_file('test.txt') as f:
        f.write('Example text')


if __name__ == '__main__':
    main()

