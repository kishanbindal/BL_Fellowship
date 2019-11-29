def userInput():
    while True:
        try:
            cash = int(input("Please Enter Amount :\n"))
        except ValueError:
            print("Please enter only Integer Values")
        else:
            return cash


def vendingMachine(cash):
    available_notes = [1000,500,100,50,10,5,2,1]
    result = {}
    total_notes = 0
    print(f"Amount = {cash}")
    for note in available_notes:
        number_of_notes = 0
        if cash>=note:
            number_of_notes = cash//note
            result[note] = number_of_notes
            total_notes += number_of_notes
            cash = cash - note*number_of_notes
    print(f"Total Number of Notes to be given : {total_notes}")
    for key,value in result.items():
        print(f"Number of {key} notes = {value}")
    return result
