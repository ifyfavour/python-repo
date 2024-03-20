score = int(input("what's your score: "))

if score < 100 and score >= 90:
    print("Grade A")
if score < 90 and score >= 80:
    print("Grade B")
if score < 80 and score >= 70:
    print("Grade C")
if score < 70 and score >= 60:
    print("Grade D")
if score < 60 and score >= 50:
    print("Grade E")
else:
    print("F")