# Building a Flask + PostgreSQL API for School Data

## Introduction

In this assignment, you will be tasked with building a Flask + PostgreSQL API that handles school-related data. You will work with student, teacher, and subject data, and your API will provide endpoints to retrieve information about students, teachers, and subjects as specified in the requirements.

## Data Description

You will be provided with the following data in CSV format:

### students.csv

This file contains information about students, including their first name, last name, age, and the subject they are studying.

### teachers.csv

This file contains information about teachers, including their first name, last name, age, and the subject they teach.

### subjects.csv

This file contains a mapping of subject IDs to subject names.

## Requirements

To complete this assignment, you need to perform the following tasks:

### 1. Database Schema (school.sql)

Create a SQL script (school.sql) that defines the database schema. You should create tables to store the provided data from the CSV files. Ensure that the tables are properly structured and relationships are established where necessary.

### 2. Flask Application (app.py)

Create a Flask application (app.py) that does the following:

- Connects to a PostgreSQL database using SQLAlchemy.
- Defines SQLAlchemy models for the following entities:
  - Students
  - Teachers
  - Subjects

### 3. Endpoints

Implement the following endpoints in your Flask application to retrieve information as specified:

#### /students

- Returns a list of students along with their class names and the teacher of their class.
- The response should be in JSON format, following the structure:

```json
[
  {
    "id": 1,
    "first_name": "Sophia",
    "last_name": "Wright",
    "age": 30,
    "class": {
      "subject": "Mathematics",
      "teacher": "David Miller"
    }
  },
  {
    // Next student data
  }
]
```

#### /teachers

- Returns an array of teachers, the subjects they teach, and the students within each subject.
- The response should be in JSON format, following the structure:

```json
[
  {
    "first_name": "David",
    "last_name": "Miller",
    "age": 32,
    "subject": {
      "subject": "Mathematics",
      "students": [
        "Sophia Wright",
        "Anna Robinson",
        // ... List of students in this subject
      ]
    }
  },
  {
    // Next teacher data
  }
]
```

#### /subjects

- Returns a list of subject dictionaries with the students enrolled in each class and the teacher who teaches each subject.
- Please provide an example of the response structure for this endpoint.

**Note:** This assignment is designed to assess your ability to structure a Flask application, create a PostgreSQL database, and define endpoints to serve data from that database. Please ensure that your code is well-documented, organized, and follows best practices.
