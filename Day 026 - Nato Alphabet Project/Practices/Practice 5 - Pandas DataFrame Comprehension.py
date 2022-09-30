student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

#for (key, value) in student_dict.items():
    #print(value)

import pandas
student_df = pandas.DataFrame(student_dict)
#print(student_df)

# loop through a Data Frame
#for (key,value) in student_df.items():
#    print(value)

for (index, row) in student_df.iterrows():
    print(f" Student {row.student} scored {row.score}")