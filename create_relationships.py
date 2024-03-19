import sqlite3
from random import randint, choice
from faker import Faker
"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    # SQL query that creates a table named 'relationships'.
    create_relationships_tbl_query = """
    CREATE TABLE IF NOT EXISTS relationships
    (
    id INTEGER PRIMARY KEY,
    person1_id INTEGER NOT NULL,
    person2_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    start_date DATE NOT NULL,
    FOREIGN KEY (person1_id) REFERENCES people (id),
    FOREIGN KEY (person2_id) REFERENCES people (id)
    );
    """
    # Execute the SQL query to create the 'relationships' table.
    cur.execute(create_relationships_tbl_query)
    con.commit()
    con.close()
   
    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    # SQL query that inserts a row of data in the relationships table.
    add_relationship_query = """
    INSERT INTO relationships
    (
    person1_id,
    person2_id,
    type,
    start_date
    )
    VALUES (?, ?, ?, ?);
    
    
    """

    person1_id_example = 1
    person2_id_example = 2
    type_example = 'friend'
    start_date_example = '2024-03-19'
    for _ in range(100):
    cur.execute(add_relationship_query, (person1_id_example, person2_id_example, type_example, start_date_example))



    con.commit()
    con.close()

    return 


if __name__ == '__main__':
   main()