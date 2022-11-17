import sqlite3

id = 0
name_id = {}
task = []
known_names = []



persons_database = sqlite3.connect('Labb11/persons.db')
score_database = sqlite3.connect('Labb11/score.db')

persons_cursor = persons_database.cursor()
score_cursor = score_database.cursor()

read_file = open("Labb11/score2.txt", "r")
for line in read_file:
    line_split = line.split(" ")
    first_name = line_split[2]
    last_name = line_split[3]
    known_names = line_split[2] + " " + line_split[3]
    task = line_split[1]
    score = int(line_split[4][0])
    
    if known_names in name_id.values():
        score_cursor("INSERT INTO scores VALUES (name_id['known_name'],task,score)")
        




"""student_scores = {}
max_scores = []
high_score = 0

read_file = open("Labb2/score2.txt", "r")
for line in read_file:
    line_split = line.split(" ")
    name = line_split[2] + " " + line_split[3]
    score = int(line_split[4][0])

    #Check if key is added to dict, if added add value to score
    if name not in student_scores.keys():
        student_scores.update({name: score})
    else:
        student_scores[name] += score"""


"""
c = conne.cursor()

c.execute(CREATE TABLE people(
    id,
    first name,
    last name
))

conne.commit()

conne.close()
"""
"""
c = conne.cursor()

c.execute(CREATE TABLE scores(
    id,
    task,
    score
))

conne.commit()

conne.close()
"""