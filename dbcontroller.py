from dis import Instruction
from operator import le, truediv
import sqlite3 as sql
from sqlite3 import Error
import intent as Intent
import random
import string

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
        """DROP TABLE IF EXISTS services"""
    )

    conn.commit()

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS commands (
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

def removeCommand(id):
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    instruction = f"DELETE FROM commands WHERE id = {id}"
    cursor.execute(instruction)
    conn.commit()
    conn.close


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
        ("??", "a"),
        ("??", "e"),
        ("??", "i"),
        ("??", "o"),
        ("??", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s.lower()

def addSkillRecord(intent):
    id = getKey()
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    instruction = f"INSERT INTO services VALUES ('{id}', '{intent.scriptName}')"
    cursor.execute(instruction)
    conn.commit()
    conn.close
    return(id)

def removeSkillRecord(id):
    pass

def getSkillFromName(name):
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM services WHERE name = '{name}'"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close
    return(data[0])

def checkSkillRecord(name):
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM services WHERE name = '{name}'"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close
    if len(data) > 0:
        return True
    else:
        return False

def keyExists(key):
    conn = sql.connect("commands.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM services WHERE id = '{key}'"
    cursor.execute(instruction)
    data = cursor.fetchall()
    conn.commit()
    conn.close
    if len(data) > 0:
        return True
    else:
        return False

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    
def getKey():
    key = get_random_string(5)
    while keyExists(key):
        key = get_random_string(5)
    return key

if __name__ == '__main__':
    # createDB()
    createTable()
    createCommand("quien fue {search}", "wikipedia")
    createCommand("quien es {search}", "wikipedia")
    createCommand("dame informacion sobre {search}", "wikipedia")
    createCommand("dame informacion de {search}", "wikipedia")
    createCommand("hablame de {search}", "wikipedia")
    createCommand("dime quien es {search}", "wikipedia")
    createCommand("que es {search}", "wikipedia")
    createCommand("que tiempo hace hoy en {city}", "weather")
    createCommand("que tiempo hace en {city}", "weather")
    createCommand("que tiempo hace aqui en {city}", "weather")
    createCommand("cual es el tiempo en {city}", "weather")
    createCommand("reproduce {song}", "youtube")
    createCommand("reproduce la cancion {song}", "youtube")
    createCommand("pon {song}", "youtube")
    createCommand("pon la cancion {song}", "youtube")
    createCommand("dime noticias de {news}", "news")
    createCommand("dime una broma", "jokes")
    createCommand("cuentame un chiste", "jokes")
    createCommand("cuentame una broma", "jokes")
    createCommand("dime un chiste", "jokes")
    # readRows()
    # removeCommand(4)
    # intent = getCommand("reproduce can't stop the feeling")
    # print(f"{intent.scriptName}, {intent.placeHolders}")
    # pass