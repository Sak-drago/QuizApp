import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


mydb = mysql.connector.connect(
    host= os.getenv("DB_HOST"),
    user= os.getenv("DB_USER"),
    password= os.getenv("DB_PASSWORD"),
    database= os.getenv("DB_NAME")
)

# test if connection was successful
print(mydb)
mycursor = mydb.cursor()


# if table already exists, drop it first
mycursor.execute("DROP TABLE IF EXISTS tokens;")
mycursor.execute("DROP TABLE IF EXISTS responses;")
mycursor.execute("DROP TABLE IF EXISTS options;")
mycursor.execute("DROP TABLE IF EXISTS questions;")
mycursor.execute("DROP TABLE IF EXISTS quizzes;")
mycursor.execute("DROP TABLE IF EXISTS users;")


#create table with (user_id : int primary key, username : varchar(255), password : sha256, token : varchar(255))
mycursor.execute("CREATE TABLE users (uid INT NOT NULL AUTO_INCREMENT , username VARCHAR(255), password VARCHAR(255), PRIMARY KEY (uid));")

# make a token table with (token_id : int primary key not null, token : varchar(255), user_id : int foreign key, expires_at : datetime)
mycursor.execute("CREATE TABLE tokens (token_id INT NOT NULL AUTO_INCREMENT , token VARCHAR(255), uid INT NOT NULL, expires_at DATETIME, PRIMARY KEY(token_id), FOREIGN KEY (uid) REFERENCES users(uid));")

# make a quizzes table with (quiz_id : int primary key, quiz_name : varchar(255))
mycursor.execute("CREATE TABLE quizzes (quiz_id INT NOT NULL AUTO_INCREMENT , quiz_name VARCHAR(255), PRIMARY KEY(quiz_id));")

# make a questions table with (question_id : int primary key, question : varchar(255)
mycursor.execute("CREATE TABLE questions (question_id INT NOT NULL AUTO_INCREMENT , question VARCHAR(1500) NOT NULL, PRIMARY KEY(question_id));")

# make a options table with (option_id : int primary key, question_id : int foreign key, option_ans : varchar(255), is_correct : boolean)
mycursor.execute("CREATE TABLE options (option_id INT NOT NULL AUTO_INCREMENT , question_id INT NOT NULL, option_ans VARCHAR(255), is_correct boolean, PRIMARY KEY(option_id), FOREIGN KEY (question_id) REFERENCES questions(question_id));")

# make a responses table with (response_id : int primary key, user_id : int foreign key, quiz_id : int foreign key, question_id : int foreign key, response : foreign key to options)
mycursor.execute("CREATE TABLE responses (response_id INT NOT NULL AUTO_INCREMENT , uid INT NOT NULL, quiz_id INT NOT NULL, question_id INT NOT NULL, option_id INT, PRIMARY KEY(response_id), FOREIGN KEY (uid) REFERENCES users(uid), FOREIGN KEY (quiz_id) REFERENCES quizzes(quiz_id), FOREIGN KEY (question_id) REFERENCES questions(question_id), FOREIGN KEY (option_id) REFERENCES options(option_id));")
