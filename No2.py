# from statistics import mean

def get_grade(s1, s2, s3):
#     score = mean([s1, s2, s3]) #using mean is good for readability and scaling later
    score = (s1 + s2 + s3) / 3 #1st put it in parentheses to follow the BODMAS rule
     #always do computation before condition
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

print(get_grade(70, 50, 80))