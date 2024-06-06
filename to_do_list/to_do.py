# Initialize the To-Do List with sample tasks
ToDoList = {
    1: 'Sample Task 1',
    2: 'Sample Task 2',
    3: 'Sample Task 3',
    4: 'Sample Task 4',
    5: 'Sample Task 5',
    6: 'Sample Task 6',
    7: 'Sample Task 7',
    8: 'Sample Task 8',
    9: 'Sample Task 9',
    10: 'Sample Task 10',
}

# Function to display available functionalities
def functionalityListing():
    print("What do you wish to do?")
    print(" 1. View List (v/V)")
    print(" 2. Add Item to the List (a/A)")
    print(" 3. Remove Item from the List (r/R)")
    print(" 4. Quit the program (q/Q)")

# Function to perform actions based on user choice
def DoTheFunction(UserChoice):
    match UserChoice.lower():
        case 'r':
            RemoveItemFromTheList()
        case 'v':
            ViewListItems()
        case 'a':
            AddItemToTheList()
        case 'q':
            quit()
        case _:
            print("Wrong Input!! Choose from a/A/v/V/r/R Next Time!!")

# Function to remove an item from the list
def RemoveItemFromTheList():
    print("Here is your TO DO LIST")
    ViewListItems()
    ItemToBeDeleted = int(input("Give S. No. of Item you wish to delete: "))
    if ItemToBeDeleted not in ToDoList.keys():
        print("Here is your TO DO LIST:")
        ViewListItems()
        print("Nothing deleted, because you gave wrong serial No!")
    else:
        ToDoList.pop(ItemToBeDeleted)
        ItemDeletedSerialNumber = ItemToBeDeleted
        ResetListAfterDeletion(ItemDeletedSerialNumber)
        print("Here is your TO DO LIST after deletion:")
        ViewListItems()

# Function to reset the list after an item is deleted
def ResetListAfterDeletion(ItemDeletedSerialNumber):
    new_dict = {}
    for key, value in ToDoList.items():
        if key < ItemDeletedSerialNumber:
            print(key, True)
            new_dict[int(key)] = value
        else:
            print(key, False)
            new_dict[int(key - 1)] = value
    ToDoList.clear()
    for key, value in new_dict.items():
        ToDoList[int(key)] = value

# Function to view list items
def ViewListItems():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("S. No.     Task Name")
    if NoOFItemsCalculator() == 0:
        print("Nothing to show here!! Add Items")
    for item in ToDoList:
        print(item, "    ", ToDoList[item])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Function to calculate the number of items in the list
def NoOFItemsCalculator():
    NoOfItemsInTheList = 0
    for item in ToDoList:
        NoOfItemsInTheList += 1
    return NoOfItemsInTheList

# Function to add an item to the list
def AddItemToTheList():
    lastNumber = NoOFItemsCalculator()
    UserGivenNameForNewTask = str(input("Give Description For the new To Do List Item: "))
    ToDoList.update({lastNumber + 1: str(UserGivenNameForNewTask)})
    print("Here is your Updated To Do List:")
    ViewListItems()

# Main function to run the program
def main():
    print("---------- Welcome to To Do List ----------")
    while True:
        functionalityListing()
        UserChoice = str(input())
        DoTheFunction(UserChoice)

# Run the main function
if __name__ == '__main__':
    main()
