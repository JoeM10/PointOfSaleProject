class item:
    def __init__(
        self,
        itemName: str,
        itemCost: float,
        itemQuantity: int
    ):
        self.itemName = itemName
        self.itemCost = itemCost
        self.itemQuantity = itemQuantity

    #Setters
    def setItemName(self, data):
        self.itemName = data
    
    def setItemCost(self, data):
        self.itemCost = data
    
    def setItemQuantity(self, data):
        self.itemQuantity = data
    
    #Getters
    def getItemName(self):
        return self.itemName
    
    def getItemCost(self):
        return self.itemCost
    
    def getItemQuantity(self):
        return self.itemQuantity