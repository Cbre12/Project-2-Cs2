from tkinter import *
from tkinter import messagebox
import csv

class Gui:
    def __init__(self, window):
        """this def function initializes the GUI.

        :param window: The Tkinter window.
        :type window: object
        :rtype: None
        :return: None
        """
        # this code initializes the window. 
        self.window = window

        # this is the frame for the dog name input.
        self.frame_one = Frame(self.window)
        self.frame_one.pack(anchor= W)
        self.label_Name = Label(self.frame_one, text='Dog Name:')
        self.label_Name.pack(side='left', padx=10)
        self.input_Name = Entry(self.frame_one, width=10)
        self.input_Name.pack(padx=21, pady=10)

        # this frame is for the weight input for the dog.
        self.frame_two = Frame(self.window)
        self.frame_two.pack(anchor=W)
        self.label_LBS = Label(self.frame_two, text='Weight (LBS):')
        self.label_LBS.pack(side='left', padx=10)
        self.input_LBS = Entry(self.frame_two, width=10)
        self.input_LBS.pack(padx=10, pady=13)

        # this frame is for the diet selection radio buttons.
        self.frame_three = Frame(self.window)
        self.radio_Status = Label(self.frame_three, text='Diet:')
        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_Student = Radiobutton(self.frame_three, text='Beef', variable=self.radio_answer, value=1)
        self.radio_staff = Radiobutton(self.frame_three, text='Fish', variable=self.radio_answer, value=2)
        self.radio_both = Radiobutton(self.frame_three, text='Beef and Fish', variable=self.radio_answer, value=3)
        self.radio_Status.pack(side='left')
        self.radio_Student.pack(side='left')
        self.radio_staff.pack(side='left')
        self.radio_both.pack(side='left')
        self.frame_three.pack(pady=10)

        # this is the frame for first submit button.
        self.frame_four = Frame(self.window)
        self.frame_four.pack()
        self.button_save = Button(self.frame_four, text='Find Food Amount', command=self.submit)
        self.button_save.pack(pady=10)

        # this is frame for output label.
        self.output_frame = Frame(self.window)
        self.output_label = Label(self.output_frame, text=' Enter a dog name and a dog weight \nto get the daily food amount in (LBS)')
        self.output_label.pack(pady=10)
        self.output_frame.pack()

    def submit(self):
        """Handle the submission of input and display the output.
        This def function retrieves the dog's name, weight, and diet selection from the GUI.
        It validates the input and calculates the daily food amount based on the selected diet.
        The output is displayed in the GUI and is also outputed to a CSV file named 'Diet.csv'.
        :param self: the submit button function.
        :type self: object
        :rtype: Error window object.
        :return: Error messages.  
        """
        # This clears previous output so there will not be multiple outputs on the GUI.
        for widget in self.output_frame.winfo_children():
            widget.destroy()

        # This will retrieve input values from the entries and set them equal to variable to be used in the equations.
        name = self.input_Name.get().strip()
        LBS = self.input_LBS.get().strip()
        status = self.radio_answer.get()

        # This checks if each input is numeric for dog name or a char or a zero for lbs and sends an error if the user is not giving the correct response.
        if not name.isalpha():
            messagebox.showerror("Error", "Dog name should contain only alphabetic characters.")
            return
        if not LBS.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Weight should contain only numeric characters.")
            return
        if float(LBS) <= 0:
            messagebox.showerror("Error", "Weight should be larger than zero.")
            return
        LBS = float(LBS)

        # This calculates food amount based on diet selection from the radio buttons.
        if status == 1:
            Beef_Amount = LBS * 0.008
            output_text = f'Dog: {name}\nweight: {LBS}\nYou selected Beef.\nFood amount per day: {Beef_Amount:.2f} (LBS)'
        elif status == 2:
            Fish_Amount = LBS * 0.003
            output_text = f'Dog: {name}\nweight: {LBS}\nYou selected Fish.\nFood amount per day: {Fish_Amount:.2f} (LBS)'
        elif status == 3:
            Both_Amount = LBS * 0.005
            output_text = f'Dog: {name}\nweight: {LBS}\nYou selected Beef and Fish.\nFood amount per day: {Both_Amount:.2f} (LBS)'
        else:
            output_text = f'Dog: {name}\nweight: {LBS}\nYou selected nothing. Please make a selection.'

        # This displays the final output.
        self.output_label = Label(self.output_frame, text=output_text)
        self.output_label.pack(pady=10)
        self.output_frame.pack()

        # This will output the response of the code to the CSV file.
        with open('Diet.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([output_text])






