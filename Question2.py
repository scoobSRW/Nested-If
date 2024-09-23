attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print("Venue selected:", venue)

if attendees > 100:
    print("You may also need an audio system and a projector.")
else:
    print("A projector may be helpful.")

vegetarian = input("Do you want vegetarian food? (yes/no) ").lower()
if vegetarian == "yes":
    print("Recommended: Veggie Delight Caterers")
else:
    print("Recommended: Gourmet Meals Caterers")