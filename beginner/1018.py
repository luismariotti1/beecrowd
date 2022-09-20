value = int(input())
saveValue = value
notes = [100, 50, 20, 10, 5, 2, 1]

distribuition = []
numberOfNotes = 0
note = 0

while note < len(notes):
    if value >= notes[note]:
        value -= notes[note]
        numberOfNotes += 1
    else:
        distribuition.append(numberOfNotes)
        numberOfNotes = 0
        note += 1

print(saveValue)
for i in range (0,len(notes)):
    print("{} nota(s) de R$ {},00".format(distribuition[i],notes[i]))