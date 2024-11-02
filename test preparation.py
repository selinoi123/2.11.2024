#START

# עם מספר תלמידים בבית ספר ידוע מראש

students_school: int = 103
students_class: int = 30

number_classes: int = students_school // students_class
last_class: int = students_school % students_class

print(f"In a school there were {number_classes} full classes of 30 students.")
print(f"Class number {number_classes + 1} has {last_class} students.")

# מספר תלמידים בבית ספר לא ידוע

number_students: int = int(input("Enter the number of students :"))
students_class: int = 30

number_classes: int = number_students // students_class
last_class: int = number_students % students_class

print(f"In a school there were {number_classes} full classes of 30 students.")
print(f"Class number {number_classes + 1} has {last_class} students.")

#END