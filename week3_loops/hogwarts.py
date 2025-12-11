
students = ["Hermoine", "Harry", "Ron","Paco"]
houses = ["Gryffindor","Gryffindor","Gryffindor","Slytherin"]


for student in students:
    print(student)

# len of something

for i in range(len(students)):
    print(i+1 ,students[i])

#dict
students = [
    {"name": "Hermoine", "house" : "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house" :"Gryffindor", "patronus": "Stag" },
    {"name": "Ron", "house" : "Gryffindor","patronus":"Erfan"},
    {"name": "Paco","house" : "Gryffindor","patronus":None}
]
#for student in students:
 #   print(student, students[student], sep=" ")

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")