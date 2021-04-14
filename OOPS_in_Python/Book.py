class Book:
	def getBookInfo(self):
		self.bookName = input("Enter Book Name: ")
		self.authorName = input("Enter Author Name: ")
		self.numberOfPages = int(input("Enter Number of pages: "))

	def printBookInfo(self):
		print("Book name: ", self.bookName)
		print("Author Name: ", self.authorName)
		print("Numer of Pages: ", self.numberOfPages)

b = Book()
print("Enter Book Details : ")
b.getBookInfo()
print(" ")
b.printBookInfo()

