
# # 1. Library Book Tracker
# books = []

# def add_book(title, author, pages):
#     books.append({"title": title, "author": author, "pages": pages})

# def find_book(title):
#     for book in books:
#         if book["title"] == title:
#             return book
#         else:
#             return "Book not found."
#     return "Book not found."


# def show_books():
#     for book in books:
#         print(f"Title: {book['title']}, Author: {book['author']}, Pages: {book['pages']}")

# add_book("1984", "George Orwell", 328)
# add_book("Padre Rico", "Robert Kiyosaki", 99)
# print(books)
# print(find_book("1984"))
# show_books()

# # 2. Student Grade Manager
# students = {}

# def add_student(name):
#     students[name] = []

# def add_grade(name, grade):
#     if name in students:
#         students[name].append(grade)
#     else:
#         print("Student not found.")

# def get_average(name):
#     if name in students:
#         grades = students[name]
#         if grades:
#             return sum(grades) / len(grades)
#         else:
#             return "No grades available."
#     else:
#         return "Student not found."

# add_student("Alice")
# add_grade("Alice", 85)
# add_grade("Alice", 90)

# get_average("Alice")
# print(students)
# print(get_average("Alice"))  # No grades available






# # 3. Restaurant Menu Editor
# menu = []

# def add_dish(name, price, available=True):
#     menu.append({"name": name, "price": price, "available": available})

# def change_availability(name, available):
#     for dish in menu:
#         if dish["name"] == name:
#             dish["available"] = available
#             return
#     print("Dish not found.")

# def total_available_price():
#     total = 0
#     for dish in menu:
#         if dish["available"]:
#             total += dish["price"]
#     return total    

# add_dish("Pizza", 10.0)
# add_dish("salad", 5.0, False)
# print(menu)
# print(total_available_price())  

# # 4. Warehouse Box Counter
# types_of_boxes = {}
# def add_box(type, quantity):
#     types_of_boxes[type] = quantity 
# add_box("Box A", 5)
# print(types_of_boxes)


# def update_quantity(type, quantity1):
#     if type in types_of_boxes:
#         types_of_boxes[type] += quantity1

#     else:
#         print("Box type not found.")
# update_quantity("Box A", 3)
# print(types_of_boxes)
    

# def has_enough(type, quantity):
#     if type in types_of_boxes:
#         return types_of_boxes[type] >= quantity
#     else:
#         print("Box type not found.")
#         return False
# print(has_enough("Box A", 8))  
# print(has_enough("Box A", 10))  



# 5. Movie Rating System
movies = []
def add_movie(title):
    movies.append({"title": title, "rate": 0})
add_movie("Inception")
print(movies)

def rate_movie(title, rate):
    for movie in movies:
        if movie["title"] == title:
            movie["rate"] += rate
            return
    print("Movie not found.")
rate_movie("Inception", 5)
print(movies)
rate_movie("Inception", 4)
print(movies)

def average_rating(title):
    for movie in movies:
        if movie["title"] == title:
            if movie["rate"] > 0:
                return movie["rate"] / 2
            else:
                return "No ratings available."
    return "Movie not found."
print(average_rating("Inception"))  # Output: 4.5


  # Output: 5
# 6. Online Course Tracker

def add_course(): pass
def update_enrollment(): pass
def filter_by_hours(): pass

# 7. To-Do List Organizer
def add_task(): pass
def complete_task(): pass
def filter_tasks(): pass

# 8. Digital Wallet
def add_expense(): pass
def total_spent(): pass
def expense_percentages(): pass

# 9. Pet Adoption Center
def add_pet(): pass
def find_by_species(): pass
def older_than(): pass

# 10. Gym Membership System
def register_member(): pass
def change_plan(): pass
def unpaid_members(): pass
