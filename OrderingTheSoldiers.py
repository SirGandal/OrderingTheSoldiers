sample = "2\n3\n0 1 0\n5\n0 1 2 0 1"

lines = sample.split('\n');
numberOfTestCases = int(lines[0])

for i in range(1, (numberOfTestCases * 2), 2):
    numberOfSoldiers = int(lines[i])

    #Initialize array of rankings from 1 to numberOfSoldiers
    soldierRanks = []
    for t in range(0, numberOfSoldiers, 1):
        soldierRanks.append(t+1)
    
    soldiersShifts = lines[i+1].split(' ')
    for j in range(0, numberOfSoldiers):
        shiftPositions = int(soldiersShifts[j])

        if shiftPositions > 0:
            for k in range(j-shiftPositions, j, 1):
                soldierRanks[k] = soldierRanks[k] + 1

            soldierRanks[j] = soldierRanks[j] - shiftPositions

    print ' '.join(str(rank) for rank in soldierRanks)
