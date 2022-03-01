"""
    CHAPTER 13
    TUTORIAL 159
    ADVANCE FUNCTION PRACTICE 2
"""
roll_no = [1, 2, 3, 4]
math = [100, 90, 80, 70]
science = [90, 70, 60, 50]
english = [100, 99, 95, 85]

percentage = []
for pair in zip(math, science, english):
    rounded = round(((sum(pair)/400)*100), 2)
    percentage.append(rounded)
print(percentage)