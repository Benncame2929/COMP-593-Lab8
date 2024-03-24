import pandas
import os
import sqlite3
from create_relationships import db_path, script_dir






def main():
    married_couples = get_married_couples()
    csv_path = os.path.join(script_dir, 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)








def save_married_couples_csv(married_couples, csv_path):
    MarriedList = []
    for p1, p2, date in married_couples:
        MarriedList.append({'PERSON1': p1, 'PERSON2': p2, 'START_DATE': date})
    datafr = pandas.DataFrame(MarriedList)
    datafr.to_csv(csv_path, index=False)







def get_married_couples():
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    all_relationships_list = """
        SELECT person1.name, person2.name, start_date, type FROM relationships
        JOIN people person1 ON person1_id = person1.id
        JOIN people person2 ON person2_id = person2.id
        WHERE type = "spouse";
    """
    cur.execute(all_relationships_list)
    all_relationships = cur.fetchall()
    mariage_List = []
    for person1, person2, date, ship in all_relationships:
        mariage_List.append([person1, person2, date])
    return mariage_List















if __name__ == '__main__':
    main()
