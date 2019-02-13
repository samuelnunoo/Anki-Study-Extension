
#Import The Modules
import genanki
import sys
import os 
import random
import sqlite3
import datetime as time



TEST_MODEL = genanki.Model(
      1145059532, 'foomodel',
      fields=[
        {
          'name': 'AField',
        },
        {
          'name': 'BField',
        },
      ],
      templates=[
        {
          'name': 'card1',
          'qfmt': '{{AField}}',
          'afmt': 
                  '<hr id="answer">'
                  '{{BField}}',
        }
      ],
    )

my_deck=genanki.Deck(
        130036233123332166,
        'Python Data Science')

#Iterate Through the Flashcards folder Right

def Cards(deck,model):
    print('ran')
    current=os.getcwd()
    export=current+"/Export/"
    flashcards=current+"/Flashcards"
    media=[]

    length=len(os.listdir(flashcards))
    if length%2!=0:
        raise FileExistsError('Missing')

    total=Card_Database()
    print(total)
    start=total-(int(length/2))
    total+=1
    start+=1
    print(start,total)

    os.chdir(flashcards)
    try:
        
        for number in range(start,total):
            index=str(number)

            front=index+"Front.png"
            back=index+"Back.png"

            print(front,back)

            note=genanki.Note(model,['<img src="{}">'.format(front),' <img src="{}">'.format(back)])
            deck.add_note(note)

            media.append(front)
            media.append(back)
    except:
        raise FileExistsError('Missing')

      
     
    genanki.Package(deck,media_files=media).write_to_file(
                export+str(len(os.listdir(export))+1)+'.apkg'
                )


    os.chdir(current)



    Backup=current+"/Backup/"


    #Move Old Files to Backup Folder

    try:
        dir=Backup+str(len(os.listdir(Backup))+1)
        os.mkdir(dir)
    except:
        print('failed')

    for items in os.listdir(flashcards):
        os.rename(flashcards+"/"+items,dir+"/"+items)
        

def New_Deck(name,id):
    
    print('running new deck',type(id),id)
    with sqlite3.connect("Decks.db") as con:
        c=con.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Decks
        				(name text, id real)''')
        
        c.execute("SELECT * FROM Decks WHERE name=?",(name,))
        entry=c.fetchone()
        if entry is None:
            c.execute("INSERT INTO Decks VALUES (?,?)",(name,id))
        else:
            return 'Deck Already Exists'
        

        for rows in c.execute("SELECT * FROM Decks"):
        	print(type(rows),rows)
        con.commit()

def Search_Decks():
    with sqlite3.connect("Decks.db") as con:
        c=con.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Decks
        				(name text, id real)''')
        
        c.execute('SELECT * FROM Decks')
        items=c.fetchall()
        return items

def Select_Deck(name):
    with sqlite3.connect("Decks.db") as con:
        c=con.cursor()
        c.execute('SELECT * FROM Decks WHERE name=?',(name,))
        item=c.fetchone()
        if item:
            return genanki.Deck(int(item[1]),item[0])

def Card_Database():
    with sqlite3.connect("Cards.db") as con:
        c=con.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Cards (name integer, date blob) ")
        amount=c.execute("SELECT COUNT(*) FROM Cards")
        return amount.fetchone()[0]

def Insert_Card():
    with sqlite3.connect("Cards.db") as con:
        c=con.cursor()
        amount=c.execute("SELECT COUNT(*) FROM Cards")
        amount=amount.fetchone()[0]

        t=time.datetime.now()
        date="{}-{}-{} at {}:{}:{}".format(t.year,t.month,t.day,t.hour,t.minute,t.second)
        print(date)
        c.execute("INSERT INTO Cards VALUES (?,?)",(amount,date))
     


