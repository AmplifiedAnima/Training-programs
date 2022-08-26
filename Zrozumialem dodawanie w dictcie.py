import csv

wtr={'blasphemous': 'bluźnierczy',
 'grace': 'wdzięk', 
'gluttony':'obżarstwo',
'transesophageal': 'przezprzełykowy',
'stent' :'stent,proteza rozszerzająca naczynie',
'drain':'sączkowanie',
'dilated renal tubule' : 'rozszerzony kanalik nerkowy',
'blister': 'listek tabletek',
'krwotok':'haemorrhage',
'healthcare proxy': 'pełnomocnik w sprawie decyzji medycznych',
'diverticular disease':'choroba uchyłkowa',
'focal segmental glomerulosclerosis':'ogniskowe segmentalne szkliwienie kłębuszków',
'labyrinth': 'błędnik',
'ear,nose and throat doctor,otolaryngologist' : 'otolaryngolog',
'roof tile': 'dachówka',
'fallopian tube' : 'jajowód',
'mrsa bacteria' : 'bakteria gronkowca złocistego',
'carotid aneurysm': 'tętniak tętnicy szyjnej',
'herpes': 'opryszczka',
'shingles': "półpasiec",
'Hemosiderin':'Hemosyderyna'
}
sort_values = sorted(wtr.items())
def odpowiedzi():
    print("1. Pokaż słownik")
    print("2. Dodaj słowo")
    print("3. Usuń słowo")
    print("4. Zapisz do pliku")

halfoflist = sorted(
    wtr.items())[len(wtr)//2:]

    
def wydrukujhalf():
    for ang,pol in halfoflist:

        print(ang+ " - "+ pol)



def saveit():
    v = open("wtr.txt", "w")
    v.write(str(wtr))
    v.close()

def saveitcsv():
    w = csv.writer(open("plik excel wtr","w"))
    for a,b in wtr.items():
        w.writerow([a,b])


def wydrukuj():
    for a,b in sorted(wtr.items()):              
        print(a+ " - "+ b)




odpowiedzi()
z=1 
while z==1:
    user_choice = int(input("którą opcje pragniesz wybrać ? "))


    if user_choice==1:
        wydrukuj()

        odpowiedzi()

    if user_choice ==2:
        x=1
        while x ==1:
                a = input(str("które słówko Angielskie chcesz dodać?"))
                b = input(str("które słówko Polskie chcesz dodać?"))
                wtr[a]=b
                
                for a,b in sorted(wtr.items()):
                        print (a + '-'+ b)
                aa = input(str("czy chcesz kontyunować tak/nie?"))
                if aa =="tak":
                        continue
                if aa == "nie":
                    odpowiedzi()
                    break
 
    if user_choice ==3:
        x=1      
        while x == 1:
            a = input(str("które słówko Angielskie chcesz usunąć?")) 
            wtr.pop(a)
            for a,b in sorted(wtr.items()):
                        print (a + '-'+ b)
            
            print("wartości zostały usunięte!")


            aa = input(str("czy chcesz kontyunować tak/nie?"))
            if aa =="tak":
                continue
            if aa == "nie":
                    odpowiedzi()
                    break  
    
    if user_choice ==4:
        saveitcsv()
        saveit()
    continue




