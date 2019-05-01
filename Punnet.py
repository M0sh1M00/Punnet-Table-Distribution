import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
random.seed(2)
### CHANGE THESE 2 VARIABLES FOR DIFFERENRT RESULTS ###

OGAmountOfPeople=200
AmountOfPeople=OGAmountOfPeople
TotalGenerations=9

### BBRR BBRr BBrr BbRR BbRr Bbrr bbRR bbRr bbrr ###
Total = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Traits = ["bb","BB","Bb","Bb"]
Traits2Num = {"bb":0,"Bb":1,"BB":2}
Freckles = {
    "bb":"Has Freckles",
    "Bb":"No Freckles",
    "BB":"No Freckles",
    }
EyeColor = {
    "bb":"Has Blue Eyes",
    "Bb":"Has Brown Eyes",
    "BB":"Has Brown Eyes",
    }
CurlyHair = {
    "bb":"Has Curly Hair",
    "Bb":"No Curly Hair",
    "BB":"No Curly Hair",
    }
EarLobes = {
    "bb":"Has Hanging Earlobes",
    "Bb":"Has Attached Earlobes",
    "BB":"Has Attached Earlobes",
    }

People = []
NewPeople = []
def CreatePerson():
    #### datapack = [freckles,eyecolor,curlyhair,earlobes] ###
    datapack = [random.choice(Traits),random.choice(Traits),random.choice(Traits)]
    return datapack
    
def Breed(TraitA,TraitB):
    ### Creating Children ###
    Child = TraitA[random.randint(0,1)]
    Child += TraitB[random.randint(0,1)]
    if Child[0]=="b":
        if Child[1]=="B":
            Child="Bb"
    return Child

def NewGeneration(People):
    ### Breeding All Humans ###
    for Couple in range(int(AmountOfPeople/2)):        
        for Children in range(4):
            Child = []
            for Trait in range(3):
                Child.append(Breed(People[Couple][Trait],People[(AmountOfPeople-1)-Couple][Trait]))
            NewPeople.append(Child)
    random.shuffle(NewPeople)
    return NewPeople

### Creating Starter Humans ###
for Person in range(AmountOfPeople):
    People.append(CreatePerson())
#print(People)
### Breeding A Generation ###
for i in range(TotalGenerations):
    #print(AmountOfPeople)
    NewPeople = NewGeneration(People)
    AmountOfPeople=len(NewPeople)
    
    ### Resetting People Variable ###
    People = []
    for Person in NewPeople:
        People.append(Person)
    NewPeople=[]
#print(len(People))

### Creating Lists For Traits:  UNUSED ###
FrecklesAr = []
EyeColorAr = []
CurlyHairAr = []
EarLobesAr = []

### BBRR BBRr BBrr BbRR BbRr Bbrr bbRR bbRr bbrr ###
for Person in People:
    if Person[0] == "BB" and Person[1] == "BB" and Person[2] == "BB":
        Total[0]+=1
    if Person[0] == "BB" and Person[1] == "Bb" and Person[2] == "BB":
        Total[1]+=1
    if Person[0] == "BB" and Person[1] == "bb" and Person[2] == "BB":
        Total[2]+=1
    if Person[0] == "Bb" and Person[1] == "BB" and Person[2] == "BB":
        Total[3]+=1
    if Person[0] == "Bb" and Person[1] == "Bb" and Person[2] == "BB":
        Total[4]+=1
    if Person[0] == "Bb" and Person[1] == "bb" and Person[2] == "BB":
        Total[5]+=1
    if Person[0] == "bb" and Person[1] == "BB" and Person[2] == "BB":
        Total[6]+=1
    if Person[0] == "bb" and Person[1] == "Bb" and Person[2] == "BB":
        Total[7]+=1
    if Person[0] == "bb" and Person[1] == "bb" and Person[2] == "BB":
        Total[8]+=1

    if Person[0] == "BB" and Person[1] == "BB" and Person[2] == "Bb":
        Total[9]+=1
    if Person[0] == "BB" and Person[1] == "Bb" and Person[2] == "Bb":
        Total[10]+=1
    if Person[0] == "BB" and Person[1] == "bb" and Person[2] == "Bb":
        Total[11]+=1
    if Person[0] == "Bb" and Person[1] == "BB" and Person[2] == "Bb":
        Total[12]+=1
    if Person[0] == "Bb" and Person[1] == "Bb" and Person[2] == "Bb":
        Total[13]+=1
    if Person[0] == "Bb" and Person[1] == "bb" and Person[2] == "Bb":
        Total[14]+=1
    if Person[0] == "bb" and Person[1] == "BB" and Person[2] == "Bb":
        Total[15]+=1
    if Person[0] == "bb" and Person[1] == "Bb" and Person[2] == "Bb":
        Total[16]+=1
    if Person[0] == "bb" and Person[1] == "bb" and Person[2] == "Bb":
        Total[17]+=1

    if Person[0] == "BB" and Person[1] == "BB" and Person[2] == "bb":
        Total[18]+=1
    if Person[0] == "BB" and Person[1] == "Bb" and Person[2] == "bb":
        Total[19]+=1
    if Person[0] == "BB" and Person[1] == "bb" and Person[2] == "bb":
        Total[20]+=1
    if Person[0] == "Bb" and Person[1] == "BB" and Person[2] == "bb":
        Total[21]+=1
    if Person[0] == "Bb" and Person[1] == "Bb" and Person[2] == "bb":
        Total[22]+=1
    if Person[0] == "Bb" and Person[1] == "bb" and Person[2] == "bb":
        Total[23]+=1
    if Person[0] == "bb" and Person[1] == "BB" and Person[2] == "bb":
        Total[24]+=1
    if Person[0] == "bb" and Person[1] == "Bb" and Person[2] == "bb":
        Total[25]+=1
    if Person[0] == "bb" and Person[1] == "bb" and Person[2] == "bb":
        Total[26]+=1
#print(Total)

    
if 1==2:
    for Person in range(len(NewPeople)):
        print("Person Number: "+str(Person+1))
        print("Freckles: "+Freckles[NewPeople[Person][0]])
        print("Eye Color: "+EyeColor[NewPeople[Person][1]])
        #print("Curly Hair: "+CurlyHair[NewPeople[Person][2]])
        #print("Earlobes: "+EarLobes[NewPeople[Person][3]])
        print("\n\n")

ind = np.arange(27)
barlist=plt.bar(ind,Total)


barlist[0].set_color('r')
barlist[1].set_color('b')
barlist[2].set_color('r')
barlist[3].set_color('b')
barlist[4].set_color('g')
barlist[5].set_color('b')
barlist[6].set_color('r')
barlist[7].set_color('b')
barlist[8].set_color('r')
barlist[9].set_color('b')
barlist[10].set_color('g')
barlist[11].set_color('b')
barlist[12].set_color('g')
barlist[13].set_color('purple')
barlist[14].set_color('g')
barlist[15].set_color('b')
barlist[16].set_color('g')
barlist[17].set_color('b')
barlist[18].set_color('r')
barlist[19].set_color('b')
barlist[20].set_color('r')
barlist[21].set_color('b')
barlist[22].set_color('g')
barlist[23].set_color('b')
barlist[24].set_color('r')
barlist[25].set_color('b')
barlist[26].set_color('r')

plt.suptitle('Distribution In A Punnet Table Over '+str(TotalGenerations)+ " Generations Starting With "+str(OGAmountOfPeople)+" People")

legend = plt.legend((barlist[0], barlist[1], barlist[4],barlist[13]), ('1', '2', '3','4'), title="Frequency In Average Distribution (Ratio)", fancybox = True)

plt.xlabel('Which Type Of Gene?')
plt.ylabel('Population')

Types =         ['BBRRKK', 'BBRrKK', 'BBrrKK', 'BbRRKK', 'BbRrKK',
                 'BbrrKK', 'bbRRKK', 'bbRrKK', 'bbrrKK','BBRRKk',
                 'BBRrKk', 'BBrrKk', 'BbRRKk', 'BbRrKk', 'BbrrKk',
                 'bbRRKk', 'bbRrKk', 'bbrrKk','BBRRkk', 'BBRrkk',
                 'BBrrkk', 'BbRRkk', 'BbRrkk', 'Bbrrkk', 'bbRRkk',
                 'bbRrkk', 'bbrrkk'
                 ]
for i in range(len(Types)):

    plt.text(i, Total[i]+0.1, Types[i], fontsize=6.5, horizontalalignment='center')
    
plt.xticks(ind, ('1', '2', '3', '4', '5',
                 '6', '7', '8', '9','10',
                 '11', '12', '13', '14', '15',
                 '16', '17', '18','19', '20',
                 '21', '22', '23', '24', '25',
                 '26', '27'), fontsize=7)
plt.show()

### Coordinates, Size, Color, Shape


