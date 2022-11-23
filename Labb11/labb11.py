import sqlite3

"""
sources for help

https://www.youtube.com/watch?v=pd-0G0MigUA&t=509s&ab_channel=CoreySchafer

https://www.youtube.com/watch?v=FrTQSPSbVC0&ab_channel=TheCSClassroom

https://stackoverflow.com/questions/49953709/how-to-deal-with-an-id-that-needs-to-be-matched-to-multiple-ids-in-sqlite

https://www.sqlitetutorial.net/what-is-sqlite/

https://www.sqlitetutorial.net/sqlite-unique-constraint/

CREATE TABLE IF NOT EXISTS shapes(
    shape_id INTEGER PRIMARY KEY,
    background_color TEXT,
    foreground_color TEXT,
    UNIQUE(background_color,foreground_color)
);
"""


persons_database = sqlite3.connect('Labb11/persons.db')

c = persons_database.cursor()


def create_tables():
    c.execute("""CREATE TABLE IF NOT EXISTS persons(
        id INTEGER PRIMARY KEY, 
        first_name TEXT, 
        last_name TEXT,
        UNIQUE(first_name,last_name))""")
    
    c.execute("""CREATE TABLE IF NOT EXISTS scores(
        personsid INTEGER, 
        task INTEGER, 
        score INTEGER,
        UNIQUE(personsid,task),
        FOREIGN KEY (personsid) REFERENCES persons(id))""")
    

def insert_data():
    read_file = open("Labb11/score2.txt", "r")
    for line in read_file:
        line_split = line.split(" ")
        person = line_split[2],line_split[3]

        c.execute("INSERT OR IGNORE INTO persons (first_name, last_name) VALUES(?, ?)", person)
        id = c.execute("SELECT id FROM persons WHERE first_name==? AND last_name==?", person)
        id = id.fetchone()

        values = [id[0], str(line_split[1]), str(line_split[4])]
        c.execute("INSERT OR IGNORE INTO scores (personsid, task, score) VALUES(?, ?, ?)", values)


def print_persons():
    c.execute("SELECT * FROM persons")
    print(c.fetchall())



def print_scores():
    c.execute("SELECT * FROM scores")
    print(c.fetchall())

#const top10 = sql.prepare("SELECT * FROM scores WHERE guild = ? ORDER BY points DESC LIMIT 10;").all(message.guild.id);
#SELECT score FROM Link JOIN Scores ON  Score_ID = Scores.ID JOIN Player ON Player_ID = Player.id WHERE Player.id = 2 ORDER BY Score DESC LIMIT(2);
def print_highscore():
    for row in c.execute("SELECT SUM(score) as high_score, first_name, last_name From persons JOIN scores ON id=personsid Group BY first_name, last_name ORDER BY high_score DESC LIMIT 10"):
        print(row)

def print_low_taskscore():
    for row in c.execute("SELECT SUM(score) as low_taskscore, task FROM scores GROUP BY task ORDER BY low_taskscore, task ASC LIMIT 10"):
        print(row)

create_tables()
insert_data()
print_highscore()
print_low_taskscore()


persons_database.commit()

persons_database.close()
