from tkinter import *
import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS store (ID INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Year INTEGER, ISBN INTEGER)")
        self.conn.commit()

    def insert(self,Title, Author, Year, ISBN):
        self.cur.execute("INSERT INTO store VALUES (NULL,?,?,?,?)",(Title, Author, Year, ISBN))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM store")
        rows=self.cur.fetchall()
        return rows

    def search(self,Title="", Author="", Year="", ISBN=""):
        self.cur.execute("SELECT * FROM store WHERE Title=? OR Author=? OR Year=? OR ISBN=? ",(Title, Author, Year, ISBN))
        searched=self.cur.fetchall()
        self.conn.commit()
        return searched

    def update(self,id, Title, Author, Year, ISBN):
        self.cur.execute("UPDATE store SET Title=?, Author=?, Year=?, ISBN=? WHERE ID=?", (Title, Author, Year, ISBN, id))
        self.conn.commit()

    def deleteit(self,id):
        self.cur.execute("DELETE FROM store WHERE ID=?",(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close
