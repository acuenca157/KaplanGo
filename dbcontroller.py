from dis import Instruction
from operator import le
import sqlite3 as sql
from sqlite3 import Error


def createDB():
    conn = sql.connect("commands.db")
    conn.commit()
    conn.close()


def createTable():
    conn = sql.connect("commands.db")
    cursor = conn.cursor()

    cursor.execute(
        """DROP TABLE IF EXISTS commands"""
    )

    conn.commit()

    cursor.execute(
        """CREATE TABLE commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                command TEXT,
                script TEXT
        )"""
    )
    conn.commit()
    conn.close()

def createCommand(mycommand, myscript):
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO commands (command, script) VALUES ('{mycommand}', '{myscript}');"
    cursor.execute(instruction)
    conn.commit()
    conn.close

def readRows():
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM commands"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close
    return(data)

def getCommand(inputCommand):
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    query = "SELECT * FROM commands"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close
    for c in data:

        splitat = c[1].find(" {")

        if splitat > -1:
            clearCommand, slots = c[1][:splitat], c[1][splitat:]
        else:
            clearCommand = c[1]

        if clearCommand in inputCommand:
            return c
    
    return None


if __name__ == '__main__':
    # createDB()
    # createTable()
    # createCommand("reproduce {title}", "jukebox")
    # createCommand("reproduce una cancion", "jukebox")
    # createCommand("para la musica", "jukebox")
    # readRows()
    print(getCommand("reproduce can't stop the feeling"))