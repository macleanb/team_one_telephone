""" To run:
    1. Create a database called "school" ($ dropdb school then $ createdb school)
    2. Create the schema by using command line 'psql school'
            Then in psql run \i '<absolute_file_path_to_sql_file>/<create_schema.sql>'
    3. Start the Flask server by typing 'python app.py'
    4. Send http requests to http://localhost:5000/api/v1/students/ or other
       endpoints below.  You can post fake student data by calling
       POST to the /students/ endpoint.

    Design Notes:
     - Basic table relationships developed from guidance here:
       https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html
"""

# External Imports
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import psycopg2

#########################################
###   Declare Constants & Variables   ###
#########################################

# Constants
OLD_STUDENT_AGE_THRESHOLD = 21

# Create the app
app = Flask(__name__)

# Set CORS policy to allow requests from localhost
CORS(app)

# Configuration for the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://W:password@localhost/school'

# Make sure the jsonify command doesn't re-sort the keys
app.json.sort_keys = False

# Initialize the SQLAlchemy extension
db = SQLAlchemy(app)

#############################
###   Class Definitions   ###
#############################

class Subject(db.Model):
    """ Create Subject model """
    __tablename__ = "subjects" # was creating problems

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50))

    # Create many-to-one relationship with Student class
    # backref creates a property called "subject_taking" on Student
    # because the property "subject" was already declared in the
    # Student class as a foreign key
    students = db.relationship('Student', backref="subject_taking")
    # set uselist=False for one-to-one relationship
    teacher = db.relationship('Teacher', uselist=False, backref="subject_teaching")

    def __str__(self):
        """ Returns a string for Subject instance """
        return f'Subject(ID: {self.id}, subject: {self.subject})'

    def serialize(self):
        """ Converts instance to a dict """
        students_list = [student.full_name() for student in self.students]

        return {
           #'id'          : self.id,
            'subject'     : self.subject,
            'teacher'     : self.teacher.full_name(),
            'students'    : students_list
        }

class Student(db.Model):
    """ Create Student model """
    __tablename__ = "students" # was creating problems

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)

    # Create field referencing Subject class
    # Foreign Key references <table_name>.<table_column_name>
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

    def serialize(self):
        """ Converts instance to a dict """

        teacher_full_name = (
            self.subject_taking.teacher.first_name +
            ' ' +
            self.subject_taking.teacher.last_name
            )

        return {
            'id'          : self.id,
            'first_name'  : self.first_name,
            'last_name'   : self.last_name,
            'age'         : self.age,
            'class'       : {
                'subject' : self.subject_taking.subject,
                'teacher' : teacher_full_name
            }
        }

    def full_name(self):
        """ Returns a full-name string """
        return self.first_name + ' ' + self.last_name

    def serialize_names_only(self):
        """ Converts instance to a dict """
        return {
            'first_name': self.first_name,
            'last_name' : self.last_name
        }

    def serialize_names_and_ages(self):
        """ Converts instance to a dict """
        return {
            'student_name': self.first_name + ' ' + self.last_name,
            'age'         : self.age
        }

class Teacher(db.Model):
    """ Create Teacher model """
    __tablename__ = "teachers" # was creating problems

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

    # Create field referencing Subject class
    # Foreign Key references <table_name>.<table_column_name>
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))

    def full_name(self):
        """ Returns a full-name string """
        return self.first_name + ' ' + self.last_name

    def serialize(self):
        """ Converts instance to a dict """
        students_list = [student.full_name() for student in self.subject_teaching.students]

        subject_dict = {
            'subject'  : self.subject_teaching.subject,
            'students' : students_list
        }

        return {
           #'id'          : self.id,
            'first_name'  : self.first_name,
            'last_name'   : self.last_name,
            'age'         : self.age,
            'subject'     : subject_dict
        }

    def serialize_names_only(self):
        """ Converts instance to a dict """
        return {
            'first_name': self.first_name,
            'last_name' : self.last_name
        }

    def serialize_names_and_ages(self):
        """ Converts instance to a dict """
        return {
            'student_name': self.first_name + ' ' + self.last_name,
            'age'         : self.age
        }


##################
###   Routes   ###
##################

### Student Routes ###

@app.route('/api/v1/students/', methods=['GET', 'POST'])
def get_students():
    """ Returns a JSON list of student data from school db/students table """
    output = []
    if request.method == 'GET':
        query_result = Student.query.all()
        output = [student.serialize() for student in query_result]

    if request.method == 'POST':
        # Add a student for demo purposes
        max_existing_id = db.session.query(func.max(Student.id)).scalar()

        form_data = None
        try:
            form_data = request.get_json()
        except Exception as e:
            print(f'Exception in app.py get_students: {e}')

        new_student = Student(
            id           = max_existing_id + 1,
            first_name   = form_data['first_name'],
            last_name    = form_data['last_name'],
            age          = int(form_data['age']),
            subject      = int(form_data['subject'])
            )

        db.session.add(new_student)
        db.session.commit()

        return jsonify(new_student.serialize())
    return jsonify(output)

@app.route('/api/v1/old_students/', methods=['GET'])
def get_old_students():
    """ Respond to GET requests with student data for old students """
    query_result = db.session.query(Student).filter(Student.age >= OLD_STUDENT_AGE_THRESHOLD)
    output = [student.serialize() for student in query_result]
    return jsonify(output)

@app.route('/api/v1/young_students/', methods=['GET'])
def get_young_students():
    """ Respond to GET requests with student data for young students """
    query_result = db.session.query(Student).filter(Student.age < OLD_STUDENT_AGE_THRESHOLD)
    output = [student.serialize() for student in query_result]
    return jsonify(output)

@app.route('/api/v1/advance_students/', methods=['GET'])
def get_advance_students():
    """ Respond to GET requests with student data for advanced students """
    query_result = db.session.query(Student).filter(
        Student.grade == 'A',
        Student.age < OLD_STUDENT_AGE_THRESHOLD
        )
    output = [student.serialize() for student in query_result]
    return jsonify(output)

@app.route('/api/v1/student_names/', methods=['GET'])
def get_student_names():
    """ Respond to GET requests with student name data only """
    query_result = Student.query.all()
    output = [student.serialize_names_only() for student in query_result]
    return jsonify(output)

@app.route('/api/v1/student_ages/', methods=['GET'])
def get_student_ages():
    """ Respond to GET requests with student age data only """
    query_result = Student.query.all()
    output = [student.serialize_names_and_ages() for student in query_result]
    return jsonify(output)

### Teacher Routes ###

@app.route('/api/v1/teachers/', methods=['GET'])
def get_teachers():
    """ Returns a JSON list of teacher data from school db/teachers table """
    output = []
    if request.method == 'GET':
        query_result = Teacher.query.all()
        output = [teacher.serialize() for teacher in query_result]
    return jsonify(output)

### Subject Routes ###

@app.route('/api/v1/subjects/', methods=['GET'])
def get_subjects():
    """ Returns a JSON list of subject data from school db/subjects table """
    output = []
    if request.method == 'GET':
        query_result = Subject.query.all()
        output = [subject.serialize() for subject in query_result]
    return jsonify(output)


################
###   Main   ###
################

if __name__ == '__main__':
    app.run(debug=True)
