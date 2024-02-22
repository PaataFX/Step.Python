import random, json

# კამათლის კლასი
class Dice:
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        result = random.randint(1,self.sides)
        return result

d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)

# მონაცემების შესაბამისი მოდიფიკატორები.
class Stat:
    def __init__(self, name):
        self.name = name
        self.value = 1
    def __repr__(self):
        return self.name
    def asi(self, inc):
        self.value += inc
    def mod(self):
        if self.value == 1:
            return -5
        elif self.value >1 and self.value <4:
            return -4
        elif self.value >3 and self.value <6:
            return -3
        elif self.value >5 and self.value <8:
            return -2
        elif self.value >7 and self.value <10:
            return -1
        elif self.value >9 and self.value <12:
            return 0
        elif self.value >11 and self.value <14:
            return 1
        elif self.value >13 and self.value <16:
            return 2
        elif self.value >15 and self.value <18:
            return 3
        elif self.value >17 and self.value <20:
            return 4
        elif self.value == 20:
            return 5
        else:
            return "Error! Invalid ability score"

st = Stat("სიძლიერე")
dx = Stat("მოხერხებულობა")
cn = Stat("გამძლეობა")
nt = Stat("ინტელექტი")
wm = Stat("სიბრძნე")
ch = Stat("ქარიზმა")

# პერსონაჟის რასისა და კლასის დადგენა
character_race = ""
character_class = ""

def choose_human():
    character_race = "ადამიანი"
    st.asi(1)
    dx.asi(1)
    cn.asi(1)
    nt.asi(1)
    wm.asi(1)
    ch.asi(1)

def choose_dwarf():
    character_race = "ჯუჯა"
    cn.asi(2)
    nt.asi(1)

def choose_elf():
    character_race = "ელფი"
    dx.asi(2)
    wm.asi(1)


races = ["ადამიანი", "ჯუჯა", "ელფი"]

print("შეგიძლია აირჩიო ერთი რასა:")
print(races)
while True:
    chosen_race = input("რასა: ")
    if chosen_race in races:
        print("მაგარია!")
        break
    else:
        print("არასწორი რასა - სცადე თავიდან.")
character_race = chosen_race

if character_race == "ადამიანი":
    choose_human()
elif character_race == "ჯუჯა":
    choose_dwarf()
elif character_race == "ელფი":
    choose_elf()


def choose_fighter():
    character_class = "მებრძოლი"
    hit_die = Dice(10)

def choose_ranger():
    character_class = "რეინჯერი"
    hit_die = Dice(10)

def choose_wizard():
    character_class = "ჯადოქარი"
    hit_die = Dice(8)

classes = ["მებრძოლი", "რეინჯერი", "ჯადოქარი"]

print("არის რამდენიმე კლასი, აირჩიე: ")
print(classes)
while True:
    chosen_class = input("კლასი: ")
    if chosen_class in classes:
        print("მაგარია!")
        break
    else:
        print("არასწორი კლასი - სცადე თავიდან")
character_class = chosen_class

if character_class == "მებრძოლი":
    choose_fighter()
elif character_class == "რეინჯერი":
    choose_ranger()
elif character_class == "ჯადოქარი":
    choose_wizard()

# მონაცემების გაგორება და მოდიფიკატორების დადგენა
attributes = []
def roll_stat():
    rolls = []
    for i in range(0,4):
        rolls.append(d6.roll())
    rolls.sort()
    del(rolls[0])
    total = 0
    for num in rolls:
        total += num
    attributes.append(total)

for i in range(0, 6):
    roll_stat()

# ქულების განაწილება
print("აი 6 შემთხვევითობით გაგორებული კამათელი, გაანაწილე შენს მონაცემებზე")
print(attributes)
while True:
    strength_input = input("სიძლიერე: ")
    strength = int(strength_input)
    if strength in attributes:
        st.asi(strength-1)
        attributes.remove(strength)
        break
    else:
        print("Error, სცადე თავიდან.")
while True:
    dexterity_input = input("მოხერხებულობა: ")
    dexterity = int(dexterity_input)
    if dexterity in attributes:
        dx.asi(dexterity-1)
        attributes.remove(dexterity)
        break
    else:
        print("Error, სცადე თავიდან.")
while True:
    constitution_input = input("გამძლეობა: ")
    constitution = int(constitution_input)
    if constitution in attributes:
        cn.asi(constitution-1)
        attributes.remove(constitution)
        break
    else:
        print("Error, სცადე თავიდან.")
while True:
    intelligence_input = input("ინტელექტი: ")
    intelligence = int(intelligence_input)
    if intelligence in attributes:
        nt.asi(intelligence-1)
        attributes.remove(intelligence)
        break
    else:
        print("Error, სცადე თავიდან.")
while True:
    wisdom_input = input("სიბრძნე: ")
    wisdom = int(wisdom_input)
    if wisdom in attributes:
        wm.asi(wisdom-1)
        attributes.remove(wisdom)
        break
    else:
        print("Error, სცადე თავიდან.")
while True:
    charisma_input = input("ქარიზმა: ")
    charisma = int(charisma_input)
    if charisma in attributes:
        ch.asi(charisma-1)
        attributes.remove(charisma)
        break
    else:
        print("Error, სცადე თავიდან.")


stats = {st:st.value, dx:dx.value, cn:cn.value, nt:nt.value, wm:wm.value, ch:ch.value}

stats = {st:[st.value, st.mod()], dx:[dx.value, dx.mod()], cn:[cn.value, cn.mod()], nt:[nt.value, nt.mod()], wm:[wm.value, wm.mod()], ch:[ch.value, ch.mod()]}
armor_class = 10 + dx.mod()
max_hp = 10 + cn.mod()

print("ასეთია შენი პერსონაჟის ფურცელი: ")

print("მონაცემები:")
print("სიძლიერე: " + str(st.value) + " (" + str(st.mod()) + ")")
print("მოხერხებულობა: " + str(dx.value) + " (" + str(dx.mod()) + ")")
print("გამძლეობა: " + str(cn.value) + " (" + str(cn.mod()) + ")")
print("ინტელექტი: " + str(nt.value) + " (" + str(nt.mod()) + ")")
print("სიბრძნე: " + str(wm.value) + " (" + str(wm.mod()) + ")")
print("ქარიზმა: " + str(ch.value) + " (" + str(ch.mod()) + ")")

# საბოლოო მონაცემები და დეტალები
character_data = {
    "race": character_race,
    "class": character_class,
    "stats": {
        "strength": [st.value, st.mod()],
        "dexterity": [dx.value, dx.mod()],
        "constitution": [cn.value, cn.mod()],
        "intelligence": [nt.value, nt.mod()],
        "wisdom": [wm.value, wm.mod()],
        "charisma": [ch.value, ch.mod()]
    },
    "armor_class": armor_class,
    "max_hp": max_hp
}

# json-ში შენახვა
with open('character_data.json', 'w') as json_file:
    json.dump(character_data, json_file)

print("პერსონაჟი შენახულია Json-ში")