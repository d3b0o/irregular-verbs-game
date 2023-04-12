import sqlite3 as sql
import os
import random
import time

def green():
    return "\033[92m"

def cyan():
	return "\033[96;1m"

def white():
	return "\x1b[1;37m"

def red():
	return "\033[91m"

def error():
	return "\x1b[1;31m"

def naranja():
	return "\x1b[1;33m"

def blue():
    return "\033[94m"

def purple():
    return "\033[38;5;209m"

def command():
    return "clear"
    #return "cls"



def main():
    puntos = 0
    racha = 0
    max_racha = 0
    while True:

        os.system(command())
        row = read_row()
        base_form = row[1]
        past_simple = row[2]
        past_participle = row[3]
        
        print(header(puntos, racha, max_racha))

        # Pregunta simple
        
        respuesta = input("\nWhat's the past {}simple{} form of '{}{}{}'?\n> ".format(purple(), white(), naranja(), base_form, white()))    
        if respuesta == past_simple:
            puntos += 1
            racha += 1
            if max_racha < racha:
                max_racha = racha
        else:
            racha = 0
            print("\n{}[!] The correct answer was {}'{}{}{}'".format(red(),white(), naranja(), past_simple, white()))
            input("Press enter to continue")
        
        os.system(command())

        print(header(puntos, racha, max_racha))

        # Pregunta participal
        
        respuesta = input("\nWhat's the past {}participle{} form of '{}{}{}'?\n> ".format(cyan(), white(), naranja(), base_form, white()))    
        if respuesta == past_participle:
            puntos += 1
            racha += 1
            if max_racha < racha:
                max_racha = racha
        else:
            racha = 0
            print("\n{}[!] The correct answer was '{}{}{}'".format(red(), naranja(), past_participle, white()))
            input("Press enter to continue")

def header(puntos, racha, max_racha):
    puntos_str = green() + str(puntos) + white()
    racha_str = green() + str(racha) + white()
    max_racha_str = green() + str(max_racha) + white()

    if puntos == 0:
        puntos_str = red() + str(puntos) + white()
    if racha == 0:
        racha_str = red() + str(racha) + white()
    if max_racha == 0:
        max_racha_str = red() + str(max_racha) + white()
    
    return "Total Points {} / Current Streak {} / Highest streak {}".format(puntos_str, racha_str, max_racha_str)

def read_row():
    conn = sql.connect("english.db")
    cursor = conn.cursor()
    instrucion = f"SELECT * FROM irregular_verbs"
    cursor.execute(instrucion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()

    row = random.randint(-1, (len(datos) - 1))
    return datos[row]

if __name__=="__main__":
    os.system(command())
    print("""{}
d888888b d8888b. d8888b. d88888b  d888b  db    db db       .d8b.  d8888b.    
  `88'   88  `8D 88  `8D 88'     88' Y8b 88    88 88      d8' `8b 88  `8D    
   88    88oobY' 88oobY' 88ooooo 88      88    88 88      88ooo88 88oobY'     
   88    88`8b   88`8b   88~~~~~ 88  ooo 88    88 88      88~~~88 88`8b      
  .88.   88 `88. 88 `88. 88.     88. ~8~ 88b  d88 88booo. 88   88 88 `88.     
Y888888P 88   YD 88   YD Y88888P  Y888P  ~Y8888P' Y88888P YP   YP 88   YD      


                db    db d88888b d8888b. d8888b. .d8888.
                88    88 88'     88  `8D 88  `8D 88'  YP                                                                                                                     
                Y8    8P 88ooooo 88oobY' 88oooY' `8bo.
                `8b  d8' 88~~~~~ 88`8b   88~~~b.   `Y8b.
                 `8bd8'  88.     88 `88. 88   8D db   8D 
                   YP    Y88888P 88   YD Y8888P' `8888Y'
{}
                        
                        Press enter to continue                                                                                                                    
    {}""".format(naranja(), blue(), white()))
    input()
    os.system(command())
    main()
