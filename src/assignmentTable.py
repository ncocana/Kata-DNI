class AssignmentTable:

    def __init__(self):
        
        self.table = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    
    def getLenghtTable(self):

        return len(self.table)
    
    def getPositionLetter(self, position):

        try:
            return self.table[position]
        except:
            return "This letter is not in use."

    def calculateLetter(self, numbersDni):

        positionLetter = int(numbersDni) % self.getLenghtTable()
        return self.getPositionLetter(positionLetter)

    def getTableContent(self):

        return self.table
