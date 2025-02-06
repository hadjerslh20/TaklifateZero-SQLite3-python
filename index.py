# TASK 02
import sqlite3
DB = sqlite3.connect('elzero.db')
# for unique data must use '' UNIQUE ''
DB.execute('CREATE TABLE if not exists users ( id INTEGER PRIMARY KEY, name TEXT UNIQUE , birthDate TEXT UNIQUE , email TEXT  ) ')
# TASK 03
# TO AVOID ERRORS BECAUSE OF UNIQUE WE ADD  ''  OR IGNORE''
cursor1= DB.cursor()
cursor1.execute('INSERT OR IGNORE INTO users VALUES (1,"Ahmed","20/10/1980","a@elzero.org")')
cursor1.execute('INSERT OR IGNORE INTO users VALUES (3,"Gamal","05/10/1991","g@elzero.org")')
cursor1.execute('INSERT OR IGNORE INTO users VALUES (4,"Mahmoud","09/10/1987","m@elzero.org")')
cursor1.execute('INSERT OR IGNORE INTO users VALUES (5,"Sameh","08/11/2000","s@elzero.org")')
# TASK 04  
cursor1.execute('INSERT OR REPLACE INTO users VALUES (2,"Sayed","20/10/1990","s@elzero.org")')
cursor1.execute('INSERT OR IGNORE INTO users VALUES (5,"Sameh","08/11/2000","s_s@elzero.org")')
# TASK 05
userId = int(input('Enter user ID :'))
Result = cursor1.execute("SELECT id FROM users ")
listi= []
for row in Result:
    listi.append(row[0])
if userId in listi:
    cursor1.execute(f'DELETE  FROM users WHERE id = {userId}')
    print('User Deleted.')
else:
    print("User Not Found. ")
DB.commit()
DB.close()