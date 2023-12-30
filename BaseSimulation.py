import random
import string 
class SlotMachine:
    def __init__(self,reelNum, winDict):
        self.reels=[list(string.ascii_uppercase[:22])] *reelNum
        self.wins=winDict
    def spin(self):
        spinResult = ''
        for reel in self.reels:
            spinResult += str(random.choice(reel))
        return spinResult
    def simulation(self, spinCount, potAmt, betAmt):
        self.spinCount, self.potAmt, self.betAmt=spinCount, potAmt, betAmt
        jackpot=0
        startingpot=potAmt
        totalPaid=0
        winningSpins=0
        for i in range(self.spinCount):
            potAmt+= betAmt
            currSpin=self.spin()
            hits=[item for item in self.wins.keys() if item in currSpin]
            if hits:
                multiplier = self.wins[max(hits)]
                payout = (betAmt*multiplier)
                potAmt -= payout
                totalPaid += payout
                winningSpins += 1
                if multiplier == self.wins[max(self.wins.keys())]:
                    jackpot += 1
        returnToPlayer = float(f"{totalPaid / (betAmt * spinCount)}")
        profit = potAmt - startingpot

        if totalPaid == 0:
            profit = f"${float(profit):,.2f}"
            return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}. RTP: 0.0"
        if profit > 0:
            profit = f"${float(profit):,.2f}"
            return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}.  RTP: {returnToPlayer:.2f}"
        elif profit < 0:
            profit = f"${float(profit):,.2f}"
            profit = str(profit).replace("-", "-$")
            return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}. RTP: {returnToPlayer:.2f}"
        else:
            return f"{winningSpins} wins/{spinCount} spins.  Simulated profit: {profit}. RTP: {returnToPlayer:.2f}"
            
