"""finds-starter-template/
│
├── README.md
├── find_s.py
└── sample_output.txt"""

import csv

def find_s_algo(filename):
    with open(filename, 'r') as file:
        csvreader = csv.reader(file)
        
        hypothesis = None
        
        for row in csvreader: 
            attribute = row[:-1]
            target = row[-1]
            
            if target == 'yes':
                if hypothesis is None:
                    hypothesis = attribute.copy()
                else:
                    for i in range(len(hypothesis)):
                        if hypothesis[i] != attribute[i]:
                            hypothesis[i] = '?'
        return hypothesis
    
final_hypothesis = find_s_algo("enjoysport.csv")
print("Final Hypothesis:", final_hypothesis)
