# Room information
rooms = {
    101: {
        "type": "Single",
        "price": 1000
    },
    102: {
        "type": "Double",
        "price": 1800
    }
}

# Ask the user
room_no = int(input("Enter Room Number: "))
days = int(input("Enter Number of Days: "))

# Check whether the room exists
if room_no in rooms:
    price_per_day = rooms[room_no]["price"]

    total_bill = price_per_day * days

    print("\n------ BILL ------")
    print("Room Number :", room_no)
    print("Room Type   :", rooms[room_no]["type"])
    print("Price/Day   :", price_per_day)
    print("Days Stayed :", days)
    print("Total Bill  :", total_bill)
else:
    print("Room not found!")