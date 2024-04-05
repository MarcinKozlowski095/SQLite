import sqlite3

con = sqlite3.connect('esmartdata.sqlite3')
cur = con.cursor()
#Create table esmartdata_instructor
cur.execute('''DROP TABLE IF EXISTS "esmartdata_instructor"''')
cur.execute('''CREATE TABLE "esmartdata_instructor"(
                id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                first_name  TEXT NOT NULL,
                last_name   TEXT NOT NULL,
                description TEXT NOT NULL
            )''')
#Create tabe esmartdata_course
cur.execute('''DROP TABLE IF EXISTS "esmartdata_course"''')
cur.execute('''CREATE TABLE "esmartdata_course"(
                id            INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                title         TEXT NOT NULL,
                subtitle      TEXT NOT NULL,
                description   TEXT NOT NULL,
                category      TEXT NOT NULL,
                subcategory   TEXT NOT NULL,
                language      TEXT NOT NULL,
                length        TEXT NOT NULL,
                rating        REAL NOT NULL,
                referral_link TEXT NOT NULL,
                instructor_id INTEGER NOT NULL,
                FOREIGN KEY(instructor_id) REFERENCES esmartdata_instructor(id)
                ON DELETE CASCADE ON UPDATE CASCADE
            )''')
#Add values to esmartdata_instructor
cur.execute('''INSERT INTO "esmartdata_instructor" (id, first_name, last_name, description)
               VALUES 
               (1, "Paweł", "Krakowiak", "Data Scientist/Python Developer/Securities Broker"),
               (2, "takeITeasy", "Academy", "Akademia Programowania")''')
               
# Create Index
cur.execute('''DROP INDEX IF EXISTS esmartdata_course_instructor_id_idx''')
cur.execute('''CREATE INDEX esmartdata_course_instructor_id_idx 
               ON esmartdata_course(instructor_id)''')

# Open the SQL file 'load_esmartdata_course.sql'               
with open('load_esmartdata_course.sql', 'r', encoding='utf-8') as file:
    sql = file.read()
cur.executescript(sql)


# Execute an SQL SELECT statement to retrieve the 'title' column
select_title = cur.execute('''SELECT title FROM esmartdata_course''').fetchall()
for row in select_title:
    print(row[0])

# Select and print the sorted list of subcategories   
select_subcategory = cur.execute('''
    SELECT DISTINCT subcategory
    FROM esmartdata_course
''').fetchall()
subcategory = []
for row in select_subcategory:
    subcategory.append(row[0])
subcategory.sort()
print(subcategory)

# Count the number of courses for each instructor
group = cur.execute('''SELECT instructor_id, COUNT(*) AS num_courses 
                       FROM esmartdata_course
                       GROUP BY instructor_id''').fetchall()
for row in group:
    print(row)
    
# Left join, group by id and count the number of courses for each instructor
left_join = cur.execute('''
    SELECT esmartdata_instructor.id,
           first_name,
           last_name,
           COUNT(*) AS num_courses
    FROM esmartdata_course
    LEFT JOIN esmartdata_instructor ON esmartdata_course.instructor_id = esmartdata_instructor.id
    GROUP BY esmartdata_course.instructor_id
''').fetchall()
for row in left_join:
    print(row)
# Left join, group by id and count average rating for each instructor
avg_rating = cur.execute('''
    SELECT esmartdata_instructor.id,
           first_name,
           last_name,
           ROUND(AVG(rating), 2) AS avg_rating
    FROM esmartdata_course
    LEFT JOIN esmartdata_instructor ON esmartdata_course.instructor_id = esmartdata_instructor.id
    GROUP BY esmartdata_course.instructor_id
''').fetchall()
for row in avg_rating:
    print(row)
#Left join and filter the courses where the title contains 'Ćwicze'
exercises = cur.execute('''
    SELECT first_name,
           last_name,
           title,
           subcategory
    FROM esmartdata_course
    LEFT JOIN esmartdata_instructor ON esmartdata_course.instructor_id = esmartdata_instructor.id
    WHERE title LIKE '%Ćwicze%'
''').fetchall()
for row in exercises:
    print(row)
#Left join and filter the courses where the title contains 'Python' and 'eng'
python_and_eng = cur.execute('''
    SELECT first_name,
           last_name,
           title,
           subcategory
    FROM esmartdata_course
    LEFT JOIN esmartdata_instructor ON esmartdata_course.instructor_id = esmartdata_instructor.id
    WHERE title LIKE '%Python%' AND language LIKE '%eng%'
''').fetchall()
for row in python_and_eng:
    print(row)

con.commit()
con.close()
