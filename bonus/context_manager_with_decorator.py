from contextlib import contextmanager


@contextmanager
def manage_file(file_path):
	file = open(file_path, 'w')
	try:
		yield file
	finally:
		file.close()
			

with manage_file('test.txt') as f:
	f.write('Example text')

