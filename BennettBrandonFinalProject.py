'''
Major to Minor Conversion Program
Brandon Bennett
SDEV140

This program will take the name of a major scale as an input and then the user will use the GUI 
to output the corresponding relative minor scaleas well as the corresponding dominant fifth chord in the scale.
The user will use the exit button to exit the program when finished.

'''
#This imports the GUI and PhotoImage libraries.
from breezypythongui import EasyFrame
from tkinter import PhotoImage

#MajorMinor is the main class of this program which contains the GUI.
class MajorMinor(EasyFrame):
    #Creates the GUI
    def __init__ (self):
        EasyFrame.__init__(self, title = "Major to Minor")
        
        #Image and label for title image. 
        ImageLabel1 = self.addLabel(text = "", row = 0, column = 0, columnspan = 3, sticky = "NSEW")
        self.Image1 = PhotoImage(file = "MajorMinor.png")
        ImageLabel1["image"] = self.Image1
        
        #Input field and label
        self.InputText = self.addTextField(text = "" , row = 1, column = 1)   
        self.addLabel(text = "Enter a Major Scale name. (Ex. 'A' or 'B Flat')", row = 1, column = 0)
        
        #Minor scale conversion button, label, and output field.
        self.addButton(text = "Minor", row = 2, column = 1, command = self.Minor)
        self.addLabel(text = "Press to return the Relative Minor Scale.", row = 2, column = 0)
        self.MinorOutput = self.addTextField(text = "", row = 2, column = 2, state = "readonly")
        
        #Dominant Fifth conversion button, label, and output field.
        self.addButton(text = "Fifth", row = 3, column = 1, command = self.Fifth)
        self.addLabel(text = "Press to the return the Dominant Fifth of the scale.", row = 3, column = 0)
        self.FifthOutput = self.addTextField(text = "", row = 3, column = 2, state = "readonly")
        
        #Circle of Fifth's image placeholder
        ImageLabel2 = self.addLabel(text = "", row = 5, column = 0, sticky = "NSEW")
        self.Image2 = PhotoImage(file = "blank.png")
        ImageLabel2["image"] = self.Image2
        
        #Button and Label used to exit the program.
        self.addLabel(text = "Press to Exit the program.", row = 4, column = 0)
        self.addButton(text = "Exit", row = 4, column = 1, command = self.EndProgram)
        
        
        
        
    #Function for minor scale conversion
    def Minor(self):
        '''Converts Major scale to Relative Minor Scale'''
        
        #Dictionary containing scale letters and corresonding numbers.
        dictionary = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"A", 9:"B", 10:"C", 11:"D", 12:"E", 13:"F", 14:"G"}
        #Placeholder List for loop
        NumList =[]
        #Pulls input from user.
        MajorInput = self.InputText.getText()
        
        #Pulls key from dictionary values and also verifies input.
        if MajorInput == "A" or MajorInput == "A Flat":
            minor = {i for i in dictionary if dictionary[i] == "A"}
        elif MajorInput == "B" or MajorInput == "B Flat":  
            minor = {i for i in dictionary if dictionary[i] == "B"}
        elif MajorInput == "C" or MajorInput == "C Sharp":
            minor = {i for i in dictionary if dictionary[i] == "C"}
        elif MajorInput == "D" or MajorInput == "D Flat":
            minor = {i for i in dictionary if dictionary[i] == "D"}
        elif MajorInput == "E" or MajorInput == "E Flat":
            minor = {i for i in dictionary if dictionary[i] == "E"}
        elif MajorInput == "F" or MajorInput == "F Sharp":
            minor = {i for i in dictionary if dictionary[i] == "F"}
        elif MajorInput == "G" or MajorInput == "G Flat":
            minor = {i for i in dictionary if dictionary[i] == "G"}
        else:
            self.messageBox(title = "Error", message = "Invalid input. please input a capitalized common scale name of type 'string'.")
            
         
        #For loop to convert major (input) to minor(output).
        for Num in minor:
            NumList.append(Num)
        minor = NumList[0] -2
        NewKey = dictionary.get(minor)
        
        #Verifies proper output based on sharps and flats
        NaturalList = ["C", "D", "F", "G", "A Flat", "B Flat", "E Flat"]
        SharpList = ["A", "E", "B", "F Sharp"]
        FlatList = ["D Flat", "G Flat"]
        for key in NaturalList:
            if MajorInput == key:
               FinalKey = NewKey
            else:
                continue
        for key in SharpList:
            if MajorInput == key:
                FinalKey = NewKey + " Sharp"
            elif MajorInput == "C Sharp":
                FinalKey = "B Flat"
            else:
                continue
        for key in FlatList:
            if MajorInput == key:
                FinalKey = NewKey + " Flat"
            elif MajorInput == "C Flat":
                FinalKey = "G sharp"
            else:
                break
        #Final Output
        self.MinorOutput.setText(str(FinalKey))
        
            
        
                
                
        
    #Function for Dominant Fifth Chord conversion
    def Fifth(self):
        '''Converts Major Scale to the Dominant Fifth Chord.'''
        #Dictionary containing scale letters and corresonding numbers.
        dictionary = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"A", 9:"B", 10:"C", 11:"D", 12:"E", 13:"F", 14:"G"}
        #Placeholder list for loop
        NumList =[]
        #Pulls input from user.
        MajorInput = self.InputText.getText()
        
        #Pulls key from dictionary values and also verifies input.
        if MajorInput == "A" or MajorInput == "A Flat":
            five = {i for i in dictionary if dictionary[i] == "A"}
        elif MajorInput == "B" or MajorInput == "B Flat":  
            five = {i for i in dictionary if dictionary[i] == "B"}
        elif MajorInput == "C" or MajorInput == "C Sharp":
            five = {i for i in dictionary if dictionary[i] == "C"}
        elif MajorInput == "D" or MajorInput == "D Flat":
            five = {i for i in dictionary if dictionary[i] == "D"}
        elif MajorInput == "E" or MajorInput == "E Flat":
            five = {i for i in dictionary if dictionary[i] == "E"}
        elif MajorInput == "F" or MajorInput == "F Sharp":
            five = {i for i in dictionary if dictionary[i] == "F"}
        elif MajorInput == "G" or MajorInput == "G Flat":
            five = {i for i in dictionary if dictionary[i] == "G"}
        else:
            self.messageBox(title = "Error", message = "Invalid input. please input a capitalized scale name of type 'string'.")
        
        #For loop to convert major (input) to dominant fifth (output).
        for Num in five:
            NumList.append(Num)
        Five = NumList[1] + 4
        NewKey = dictionary.get(Five)
        #If-Else used to produce proper output based on sharps and flats.
        if "Flat" in MajorInput != True and MajorInput != "B Flat":
            FinalKey = NewKey + " Flat"
        elif MajorInput == "B":
            FinalKey = "F Sharp"
        elif "Sharp" in MajorInput != True and MajorInput != "F Sharp":
            FinalKey = NewKey + " Sharp"
        elif MajorInput == "F Sharp":
            FinalKey = "D Flat"
        else:
            FinalKey = NewKey
        #Final Output
        self.FifthOutput.setText(FinalKey)
        
        #Circle of Fifth's Image
        ImageLabel2 = self.addLabel(text = "", row = 5, column = 0, sticky = "NSEW")
        self.Image2 = PhotoImage(file = "circle.png")
        ImageLabel2["image"] = self.Image2
    
    #Function for exiting the program
    def EndProgram(self):
        '''Exits the program'''
        exit()
    
#Main function loop used for EasyFrame
def main():
    MajorMinor().mainloop()
if __name__ == "__main__":
    main()
