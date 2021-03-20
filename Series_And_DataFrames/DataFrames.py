import pandas as pd
import numpy as np

marksheet = pd.DataFrame({'Physics': [23,45,94,28,90],
                          'Chemistry': [56,98,45,19,89],
                          'Maths': [16,95,90,25,97],
                          'English': [95,90,75,89,96]},
                          index =['Student A', 'Student B', 'Student C', 'Student D', 'Student E'])
print(marksheet)          
marksheet['Avg'] = (marksheet['Physics'] + marksheet['Chemistry'] + marksheet['Maths'] + marksheet['English']) /4
print(' ')
print(marksheet)

# marksheet.loc[marksheet['Avg'] < 40, 'Result'] = 'FAIL'
# marksheet.loc[marksheet['Avg'] > 40, 'Result'] = 'PASS'
print(' ')
# print(marksheet)

# Above result can be achieved using lambda function 

marksheet['Result'] = marksheet['Avg'].apply(lambda Avg : 'FAIL' if Avg < 40 else 'PASS')
print(marksheet)