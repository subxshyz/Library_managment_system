class BookNode:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def add_book(self, book_id, title):
        new_book = BookNode(book_id, title)
        if not self.head:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print("Book added successfully")

    def display_books(self):
        temp = self.head
        if not temp:
            print("No books available")
            return
        while temp:
            print(f"ID: {temp.book_id}, Title: {temp.title}")
            temp = temp.next

    def get_books_list(self):
        books = []
        temp = self.head
        while temp:
            books.append((temp.book_id, temp.title))
            temp = temp.next
        return books


def merge_sort(books):
    if len(books) <= 1:
        return books

    mid = len(books) // 2
    left = merge_sort(books[:mid])
    right = merge_sort(books[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


library = Library()

while True:
    print("\n1.Add Book 2.Display Books 3.Sort Books 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        library.add_book(book_id, title)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        books = library.get_books_list()
        sorted_books = merge_sort(books)
        print("\nSorted Books:")
        for b in sorted_books:
            print(f"ID: {b[0]}, Title: {b[1]}")

    elif choice == 4:
        break
    else:
        print("Invalid choice")
