import pandas as pd
import os
import sqlite3
from create_relationships import db_path, script_dir






def main():
    married_couples = get_married_couples()
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples.csv') 
    save_married_couples_csv(married_couples, csv_path)
    







def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    married_couples = cur.fetchall()
    header_row = ('Person 1', 'Person 2', 'Anniversary')
    
    csv_path = pd.DataFrame(married_couples)
    csv_path.to_csv(f'married couples.csv', index=False, header=header_row)







def get_married_couples():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    all_relationships_list = """
        SELECT person1.name, person2.name, start_date, type FROM relationships
        JOIN people person1 ON person1_id = person1.id
        JOIN people person2 ON person2_id = person2.id
        WHERE person1.id = person1_id AND person2.id = person2_id;
    """
    cur.execute(all_relationships_list)
    all_relationships = cur.fetchall()
    con.close()
    for person1, person2, start_date, spouse in all_relationships:
        print(f'{person1} has been a {spouse} of {person2} since {start_date}.')
    return (person1, person2, start_date)



if __name__ == '__main__':
    main()
