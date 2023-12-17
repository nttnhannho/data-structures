class ManageFile:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.file_path, self.mode)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
    	if self.file:
    		self.file.close()
    
    def write(self, text):
    	if self.mode == 'w':
    		self.file.write(text)
    
    def read(self):
    	if self.mode == 'r':
    		for line in self.file:
    			print(line)


def main(): 
	with ManageFile('test.txt', 'w') as f:
		f.write('Example text\n')
		f.write('Nhan Nguyen')

	with ManageFile('test.txt', 'r') as f:
		f.read()


if __name__ == '__main__':
	main()
