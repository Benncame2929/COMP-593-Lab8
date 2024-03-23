import pandas

"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path, script_dir

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    
    MarriedList = []

    for p1, p2, date in married_couples :
        MarriedList.append({'PERSON1' : p1, 'PERSON2' :p2, 'START_DATE' : date})

        datafr = pd.Dataframe(MarriedList)
        datafr.to_csv(csv_path, Index=False)

    return


def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """

    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    # Hint: See example code in lab instructions entitled "Get a List of Relationships"
 

    all_relationships_list = """
        SELECT person1.name, person2.name, start_date, type FROM relationships
        JOIN people person1 ON person1_id = person1.id
        JOIN people person2 ON person2_id = person2.id
        WHERE type = "spoue";
    """ 

    cur.execute(all_relationships_list)
    all_relationships = cur.fetchall()

    con.commit()
    con.close()

    mariage_List = []
    for person1, person2, date, ship in all_relationships:
        mariage_List.append([person1, person2, date])
    return mariage_List

    return



if __name__ == '__main__':
   main()