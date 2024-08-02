
import pandas as pd
import openpyxl
from datetime import date
'''
    University Decision Tool.py
    Author: Jie Wang
    First Version: 03/18/2024
    Usage: 
    1. Run it in the terminal, with 'python .\university_decision_tool.py' 
    2. Fill in the value you expected between 1~10
    3. The program will generate the excel output and the score ranking
'''

def create_decision_matrix():
    # modify it based on your own decision rule
    criteria = [
        "Curriculum Strength",
        "Research Opportunities",
        "Location & Climate",
        "Alumni Network & Job Placement Rates",
        "Financial Considerations",
        "Faculty Expertise",
        "Campus Facilities",
        "Internship & Job Opportunities Nearby"
    ]

    # Assign weights to each criterion 
    weights = [10, 9, 5, 8, 7, 9, 6, 8] # Modify it if necessary

    # Initialize a DataFrame to store the ratings for each university
    universities =  ['University1','Program1']# ["UCSD", "CMU","UIUC", "UMICH", "Gatech", "Northwestern","Northeastern" "DUKE"]
    data = {criterion: [0] * len(universities) for criterion in criteria}
    df = pd.DataFrame(data, index=universities)

    # Termianl input ratings for each program
    for university in universities:
        print(f"\nEnter ratings for {university} (scale 1-10):")
        for criterion in criteria:
            valid_input = False
            while not valid_input:
                try:
                    rating = int(input(f"{criterion}: "))
                    if rating < 1 or rating > 10:
                        print("Rating must be between 1 and 10. Please try again.")
                    else:
                        valid_input = True
                        df.loc[university, criterion] = rating
                except ValueError:
                    print("Invalid input. Please enter a number.")

    # weighted scores and ranking
    df['Total Score'] = df.dot(weights)
    print("\nFinal Rankings:")
    print(df.sort_values(by='Total Score', ascending=False))
    # store into excel
    today_str = date.today().strftime('%Y-%m-%d')
    df.to_excel(f'decision_sheet_{today_str}.xlsx', sheet_name=f'decision_sheet_{today_str}')

if __name__ == "__main__":
    create_decision_matrix()
