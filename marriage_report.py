
from create_relationships import db_path
import pandas as pd
import os
import sqlite3

"""
Description:
 Generates a CSV report of married couples in the Social Network database.

Usage:
 python generate_married_couples_report.py
"""

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    married_couples = get_married_couples()
    csv_path = os.path.join(script_dir, 'married_couples.csv') 
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Gets a list of all married couples"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    married_couples_query = """
    SELECT person1.name, person2.name, start_date FROM relationships
    JOIN people person1 ON person1_id = person1.id
    JOIN people person2 ON person2_id = person2.id
    WHERE type = 'spouse';
    """
    cur.execute(married_couples_query)
    married_couples = cur.fetchall()
    con.close()
    return married_couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    header_row = ['Person 1', 'Person 2', 'Anniversary']
    df = pd.DataFrame(married_couples, columns=header_row)
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    main()
