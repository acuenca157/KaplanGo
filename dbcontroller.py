from dis import Instruction
from operator import le
import sqlite3 as sql
from sqlite3 import Error
import intent as Intent

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


def createIntent(scriptName, onlySlots, userSlots):
    intent = Intent.Intent(scriptName, onlySlots, userSlots)
    return intent


def getIntent(inputCommand):
    inputCommand = normalize(inputCommand)
    print(inputCommand)
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
            clearedUserCommand, userSlots =  inputCommand[:splitat], inputCommand[splitat:]
        else:
            clearCommand = c[1]
            userSlots = None

        if clearCommand in inputCommand:
            intent = createIntent(c[2], slots, userSlots)
            return intent
    
    return None

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s.lower()

if __name__ == '__main__':
    # createDB()
    # createTable()
    # createCommand("quien fue {search}", "wikipedia")
    # createCommand("quien es {search}", "wikipedia")
    # createCommand("dame informacion sobre {search}", "wikipedia")
    # createCommand("dame informacion de {search}", "wikipedia")
    # createCommand("hablame de {search}", "wikipedia")
    # createCommand("hablame sobre {search}", "wikipedia")
    # readRows()
    # intent = getCommand("reproduce can't stop the feeling")
    # print(f"{intent.scriptName}, {intent.placeHolders}")
    pass