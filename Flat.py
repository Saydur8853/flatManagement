class Flat:
    def __init__(self, flatId, flatType, flatSize, Address, Description):
        self.flatId = flatId
        self.flatType = flatType
        self.flatSize = flatSize
        self.Address = Address
        self.Description = Description
        
f1 = Flat("2B", "Family", "2300 Sqr/ft", "Banani 11", "New condition , full tiles")    

print("Flat: ", f1.flatId, f1.flatType, f1.flatSize, f1.Address, f1.Description)


class Rooms:
    def __init__(self, roomQuantity, roomType, roomSize,Description):
        self.roomQuantity = roomQuantity
        self.roomType = roomType
        self.roomSize = roomSize
        self.Description = Description
        
r1 = Rooms("2", "Bed Room", "230 Sqr/ft", "attached bath")    
r2 = Rooms("1", "Dyning Room", "120 Sqr/ft", " good condition")   
print("Rooms: ", r1.roomQuantity,r1.roomType,r1.roomSize,r1.Description)
print("Rooms: ", r2.roomQuantity,r2.roomType,r2.roomSize,r2.Description)


class Owner:
    def __init__(self, name, phoneNumber, nationalID, comment):
        self.name = name
        self.phoneNumber = phoneNumber
        self.nationalID = nationalID
        self.comment = comment
        
o1 = Owner("Noor", "01700000", "7847484674", "Welcome to my flat")    

print("Owner: ", o1.name, o1.phoneNumber, o1.nationalID, o1.comment)



class Facility:
    def __init__(self, facilityType, Description):
        self.facilityType = facilityType
        self.Description = Description
        
facility1 = Facility("Parking", "2 Cars can hold")    

print("Facility: ", facility1.facilityType, facility1.Description)

class Bills:
    def __init__(self, billsType, billAmount, vat, billDate, comment):
        self.billsType = billsType
        self.billAmount = billAmount
        self.vat = vat
        self.billDate = billDate
        self.comment = comment
        
bills = Bills("Electricity", "900 taka", "30 taka", "24/10/2021", "Please pay this bill witnin 1 week")    

print("Bill: ", bills.billsType, bills.billAmount, bills.vat, bills.billDate, bills.comment)

