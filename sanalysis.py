import pandas as pd
df = pd.read_csv("internship_bootcamp_data.csv")


# taking student name and returning animal
def student_animal(name):
	student = df["First Name"]
	animal = df["Fav animal"]
	student_info = animal.loc[student == name]
	return student_info
print(student_animal("Rie"))
print(student_animal("Lynette"))
print(student_animal("Mia"))
print(student_animal("Sabrina"))