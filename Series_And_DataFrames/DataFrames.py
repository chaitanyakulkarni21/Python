import pandas as pd
import numpy as np

marksheet = pd.DataFrame({'Physics': [23,45,94,28,10],
                          'Chemistry': [16,98,45,19,49],
                          'Maths': [16,45,20,25,27],
                          'English': [15,12,45,89,16]},
                          index =['Student A', 'Student B', 'Student C', 'Student D', 'Student E'])
print(marksheet)          
marksheet['Average'] = (marksheet['Physics'] + marksheet['Chemistry'] + marksheet['Maths'] + marksheet['English']) /4
print(' ')
print(marksheet)

# marksheet.loc[marksheet['Average'] < 40, 'Result'] = 'FAIL'
# marksheet.loc[marksheet['Average'] > 40, 'Result'] = 'PASS'
print(' ')
# print(marksheet)

# Above result can be achieved using lambda function 

marksheet['Result'] = marksheet['Average'].apply(lambda Average : 'FAIL' if Average < 40 else 'PASS')
print(marksheet)
print(' ')
print(marksheet['Result'])

