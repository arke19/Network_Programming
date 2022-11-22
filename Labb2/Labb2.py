

student_scores = {}
max_scores = []
high_score = 0
name_id = {}
id = 0

read_file = open("Labb2/score2.txt", "r")
for line in read_file:
    line_split = line.split(" ")
    name = line_split[2] + " " + line_split[3]
    score = int(line_split[4][0])
    if name != name_id:
        name_id[name] = id
        id += 1
        print(name_id)
        print(" ")



    #Check if key is added to dict, if added add value to score
    if name not in student_scores.keys():
        student_scores.update({name: score})
    else:
        student_scores[name] += score

    #Check for highest scoring students
    if student_scores[name] > high_score:
        high_score = student_scores[name]
        max_scores.clear()
        max_scores.append(name)
    elif student_scores[name] == high_score:
        max_scores.append(name)
        

print(max_scores, "Have the highest score of:", high_score)
