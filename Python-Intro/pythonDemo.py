import random
import sys

def rechnen():
    print("-----------------------------------")
    print("Rechner. Geben sie ein Rechenzeichen ein: (+;-;*;/):")

    rechenzeichen = input("Eingabe: ")

    #Zahleneingabe
    if(rechenzeichen=="+" or rechenzeichen=="-" or rechenzeichen=="*" or rechenzeichen=="/"):
        print("Geben sie beliebig viele Zahlen ein. Wenn sie fertig sind geben sie \"F\" ein.")
        zahl=0
        zahlen=[]
        while True:
            try:
                zahl= input("Eingabe: ")
                if zahl =="F":
                    break

                if(rechenzeichen=="/" and int(zahl)==0):
                    raise Exception("No division by 0!")

                zahlen.append(int(zahl))
                
            except:
                print("EXCEPTION: ")
                print("Bitte eine richtige Zahl oder \"F\" eingeben.")
        
        #Eingabe berechnen
        ergebnis = zahlen[0]
        for i in range(len(zahlen)):
            if i !=0:
                if rechenzeichen=="+":
                    ergebnis = ergebnis+zahlen[i]
                elif rechenzeichen=="-":
                    ergebnis = ergebnis-zahlen[i]
                elif rechenzeichen=="*":
                    ergebnis = ergebnis*zahlen[i]
                elif rechenzeichen=="/":
                    ergebnis = ergebnis/zahlen[i]
        
        print("Ergebnis: ",ergebnis)
    else:
        print("Bitte ein richtiges Rechenzeichen eingeben.")
        #lässige Rekursion
        rechnen()




def randomZahlen():
    print("----------------------------------------")
    print("Ranom zahlen. Bitte gib die anzahl der zu generierenden Zahlen ein.")

    anzahl = input("Eingabe: ")
    min = input("Untergrenze eingeben: ")
    max = input("Obergrenze eingeben: ")

    #generate Numbers
    randomNumbers =[]

    for i in range(int(anzahl)):
        randomNumbers.append(random.randint(int(min),int(max)))
    
    print("Random Numbers: ")
    for i in randomNumbers:
        #Damit alle in einer Zeile geprinted werden
        sys.stdout.write(str(i))
        sys.stdout.write(", ")
    
    #Sort numbers
    randomNumbers=sorted(randomNumbers)
    print("")
    print("Sorted random Numbers: ")
    for i in randomNumbers:
        sys.stdout.write(str(i))
        sys.stdout.write(", ")
    
    #berechne summe
    print("")
    print("Summe: ",sum(randomNumbers))





class customer: 
    def __init__(self,id, firstname,lastname,gender,email): 
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email


def insertCustomer():
    print("Kunden hinzufügen.")
    id = input("Geben sie eine ID ein: ")
    firstname = input("Geben sie den Vornamen ein: ")
    lastname = input("geben sie den Nachnamen ein: ")
    gender = input("Geben sie das Geschlecht ein: ")
    email = input("Geben sie die email ein: ")
    return customer(id,firstname,lastname,gender,email)


def kundenliste():
    eing=0
    customers =[]
    while eing !="5":
        print("")
        print("---------------------------")
        print("")
        print("Kundenliste. Was möchten sie tun?")
        print("1) Kunden anlegen")
        print("2) Kunden löschen")
        print("3) Kundendaten ändern")
        print("4) Kundenliste anzeigen")  
        print("5) Zurück zum Hauptmenü")

        eing = input("Eingabe: ")
        if eing  == "1":
            customers.append(insertCustomer())

        elif eing == "2":
            remId = input("geben sie die ID vom Kunden ein, den sie löschen möchten: ")
            for cust in customers:
                if cust.id == remId:
                    customers.remove(cust)
                    break

        elif eing=="3":
            chanId = input("geben sie die ID vom Kunden ein, von dem sie etwas verändern möchten: ")
            attr = input("geben sie das Attribut ein das sie verändern wollen(id,firstname,lastname,gender,email): ")
            for cust in customers:
                if cust.id == chanId:
                    if attr=="id":
                        newId = input("Geben sie die neue ID ein: ")
                        cust.id=newId
                    elif attr=="firstname":
                        newFirstname = input("Geben sie den neuen Vornamen ein: ")
                        cust.firstname = newFirstname
                    elif attr == "lastname":
                        newLastname = input("Geben sie den neuen Nachnamen ein: ")
                        cust.lastname = newLastname
                    elif attr =="gender":
                        newGender = input("Geben sie das neue Geschlecht ein: ")
                        cust.gender = newGender
                    elif attr=="email":
                        newEmail = input("Geben sie die neue Email ein: ")
                        cust.email = newEmail
                    break

        elif eing=="4":
            for obj in customers:
                print("Kunde: {", "ID: ",obj.id, "; Vorname: ",obj.firstname,"; Nachname: ",obj.lastname,"; Geschlecht: ",obj.gender,"; Email: ",obj.email,"}", sep ='' )

#main menü
if __name__ =="__main__":
    eingabe = 0

    while eingabe!="4":
        print("")
        print("")
        print("------------------------")
        print("")
        print("Was möchten sie tun?")
        print("1) Rechnen")
        print("2) Random Zahlen")
        print("3) Kundenliste")
        print("4) Beenden")

        eingabe = input("Eingabe: ")

        if eingabe  == "1":
            rechnen()
        elif eingabe == "2":
            randomZahlen()
        elif eingabe=="3":
            kundenliste()