from tkinter import *
import sqlite3
import MySQLdb
import getmonogodbrecords


class Welcome():
    def __init__(self, master):
        self.master = master
        self.master.geometry('400x330+100+200')
        self.master.title('Welcome!')
        self.label1=Label(self.master,text='Test Database Main Menu',fg='red').grid(row=0,column=1)


        self.button1 = Button(self.master,text="Enter Data", height = 3, width = 12 , fg='green',command=self.gotodataentry).grid(row=1,column=1)
        self.button2 =Button(self.master,text="Data Records",fg='blue',height = 3, width = 12,command=self.gotorecords).grid(row=2,column=1)
        self.button6 = Button(self.master, height=3, width=12, text="Run amazon", fg="black", ).grid(row=3, column=1)
        self.button5 = Button(self.master, height=3, width=12, text="Getstatus", fg="orange",command=self.get_status_records).grid(row=4, column=1)
        self.button3 = Button(self.master,text="Exit",height = 3, width = 12,fg='red',command=self.exit).grid(row=5, column=1)

        # self.button6.configure(font=('Sans', '14', 'bold'), background='blue', foreground='#eeeeff')

    def exit(self):
        self.master.destroy()

    def gotodataentry(self):
        root2=Toplevel(self.master)
        myGUI=DataEntry(root2)

    def gotorecords(self):
        root2=Toplevel(self.master)
        mygui= records(root2,"ID","URL", "TOTAL REVIEWS COUNT")
        # mygui=Records(root2)

    def get_status_records(self):
        print("---------------------------------------------------------------in the get status record")
        root3 =Toplevel(self.master)
        myrecords  = records(root3,"ID","DATE", "MESSAGE")




class DataEntry():

    def __init__(self,master):
        self.master = master
        self.master.geometry('450x400+100+200')
        self.master.title('Data Entry')

        self.label2=Label(self.master,text='Welcome to the data entry menu', fg='red').grid(row=0,column=0)
        self.label3=Label(self.master,text='Please enter date"02/03/2018" text', fg='black').grid(row=3,column=0)
        self.label4=Label(self.master,text='Please enter some text', fg='black').grid(row=4,column=0)

        self.text1=StringVar()
        self.text_entry = Entry(self.master,textvariable=self.text1).grid(row=3,column=1)
        self.int1=StringVar()
        self.int_entry = Entry(self.master,textvariable=self.int1).grid(row=4,column=1)
        self.button4=Button(self.master,text="Save",fg='red',command=lambda: self.savedata(self.text1.get(), self.int1.get())).grid(row=7,column=0)
        self.button5=Button(self.master,text="Exit",fg='red',command=self.exit).grid(row=9,column=0)

    def exit(self):
        self.master.destroy()

    def savedata(self, text1, int1):
        con =  MySQLdb.connect("127.0.0.1", "root", "root", "mismatch")
        cur = con.cursor()
        print(text1,int1)
        insert ="""INSERT INTO dailystatus(date,message) VALUES ("%s","%s")"""
        cur.execute(insert%(text1,int1))
        con.commit()
        print('Record inserted in dailystatus')


class records:
    def __init__(self, master,col1_name ,col2_name,col3_name):
        print(col2_name)
        self.master = master
        self.master.geometry('850x600+100+200')
        self.master.title('Records')
        self.connection = MySQLdb.connect("127.0.0.1", "root", "root", "mismatch")
        self.cur = self.connection.cursor()
        self.textLabel = Label(self.master, text=col1_name, width=10)
        self.textLabel.grid(row=0, column=0)
        self.intLabel = Label(self.master, text=col2_name, width=10)
        self.intLabel.grid(row=0, column=1)
        self.intLabel = Label(self.master, text = col3_name, width=20)
        self.intLabel.grid(row=0, column=2)
        self.showallrecords(col2_name)

    def showallrecords(self,col2_name):
        if col2_name =="DATE":
            Data = self.readfromdatabase("dailystatus")
        else:
            Data = self.readfromdatabase("reviews_count")
        for index, dat in enumerate(Data):
            Label(self.master, text=dat[0]).grid(row=index+1, column=0)
            Label(self.master, text=dat[1]).grid(row=index+1, column=1)
            Label(self.master ,text =dat[2]).grid(row=index+1,column=2)

    def readfromdatabase(self,table):
        self.cur.execute("SELECT * FROM %s"%table)
        return self.cur.fetchall()

def main():
     root=Tk()
     myGUIWelcome=Welcome(root)
     root.mainloop()

if __name__ == '__main__':
     main()