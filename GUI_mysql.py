from Tkinter import *
import MySQLdb

root = Tk()
root.title("PyCall")
myContainer = Frame(root)
myContainer.pack(side=TOP, expand=YES, fill=BOTH)

db = MySQLdb.connect("1.234.91.201",port=3306, user="root", passwd="########", db="BOARD" )
cursor = db.cursor()

cursor.execute("SELECT * FROM tb_bbs")
db.commit()

numrows = int(cursor.rowcount)

for i in range(0,numrows):
    
    row = cursor.fetchone()
    print row[3]
    

listbox = Listbox(root)
listbox.pack()
listbox.insert(END, row[6])

root.mainloop()
db.close()
