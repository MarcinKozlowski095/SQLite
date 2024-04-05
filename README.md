# eSmartData Database

This project contains a SQLite database called `esmartdata.sqlite3`, which stores information about instructors and courses offered by eSmartData.

## Database Schema

The database schema consists of two tables:

1. `esmartdata_instructor`: Stores information about instructors, including their first name, last name, and description.
2. `esmartdata_course`: Stores information about courses, including title, subtitle, description, category, subcategory, language, length, rating, referral link, and the ID of the instructor who teaches the course.

## Queries

Here are some sample queries you can run on the database:

- Retrieve the titles of all courses.
- Get a sorted list of subcategories.
- Count the number of courses for each instructor.
- Calculate the average rating for each instructor.
- Filter courses containing the word "Ćwicze".
- Filter courses containing the word "Python" and with English language.
