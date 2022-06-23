def columnHeader():
    print("Name                 Room Type          Cost       Cable   Hospitality Rm")
    print("-------------------------------------------------------------------------")

def prettyP(name, cost, room, costCable, hospRoom):
    print(format(name, '20s'), format(room, '17s'), format(cost, '>5s'), format(costCable, '11.2f'), format(hospRoom, '13.2f'))

def roomCost(num, typeRoom):

    if typeRoom == 'P':
        cost = num * 950
        typeRoom = 'Private'
    elif typeRoom == 'S':
        cost = num * 695
        typeRoom = 'Semi-Private'

    return cost, typeRoom

def cableCost(num):

    costCable = num * 24.50
    if costCable > 300:
        costCable = 300

    return costCable
 
def hospCost(num):

    hospRoom = num * 15
    if hospRoom < 300:
        hospRoom = hospRoom
    else:
        hospRoom = 300

    return hospRoom

def main():

    infile = open("hospital.py", 'r')

    name = infile.readline().strip()
    num = eval(infile.readline().strip())
    typeRoom = infile.readline().strip()
    cable = infile.readline().strip()
    used = infile.readline().strip()

    header = columnHeader()
    sumCost = 0
    sumCable = 0
    sumHosp = 0

    while name != 'END':

        costRoom = roomCost(num, typeRoom)
        room = costRoom[1]
        cost = str(costRoom[0])

        if cable == 'Y':
            costCable = cableCost(num)
        else:
            costCable = 0.00

        if typeRoom == 'S' or typeRoom == 'Semi-Private':
            if used == 'Y':
                hospRoom = hospCost(num)
            else:
                hospRoom = 0
        else:
            hospRoom = 0
        
                
        pretty = prettyP(name, cost, room, costCable, hospRoom)
        

        sumCost += int(cost)
        sumCable += costCable
        sumHosp += hospRoom

        name = infile.readline().strip()
        num = eval(infile.readline().strip())
        typeRoom = infile.readline().strip()
        cable = infile.readline().strip()
        used = infile.readline().strip() 

    print("-------------------------------------------------------------------------") 
    print(format("Totals", '20s'), format(sumCost, '23d'), format(sumCable, '11.2f'), format(sumHosp, '13.2f'))  
main() 
    