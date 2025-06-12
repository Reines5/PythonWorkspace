from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(300, 300)

def get_Values():
    try:
        height_cm = float(heightE.get())
        kg = float(kgE.get())
        height_m = height_cm / 100
        bmi = kg / (height_m ** 2)
    except ValueError:
        result_label.config(text="Please enter a valid number.")
        return

    if bmi < 16:
        result_label.config(text=f"BMI: {bmi:.2f}, Severe Thinness")
    elif 16 <= bmi < 17:
        result_label.config(text=f"BMI: {bmi:.2f}, Moderate Thinness")
    elif 17 <= bmi < 18.5:
        result_label.config(text=f"BMI: {bmi:.2f}, Mild Thinness")
    elif 18.5 <= bmi < 25:
        result_label.config(text=f"BMI: {bmi:.2f}, Normal")
    elif 25 <= bmi < 30:
        result_label.config(text=f"BMI: {bmi:.2f}, Overweight")
    elif 30 <= bmi < 35:
        result_label.config(text=f"BMI: {bmi:.2f}, Obese Class I")
    elif 35 <= bmi < 40:
        result_label.config(text=f"BMI: {bmi:.2f}, Obese Class II")
    else:
        result_label.config(text=f"BMI: {bmi:.2f}, Obese Class III")

# Height
heightL = Label(text="Please entry your height (cm):")
heightE = Entry()
heightL.pack()
heightE.pack()

# Kilogram
kgL = Label(text="Please entry your weight (kg):")
kgE = Entry()
kgL.pack()
kgE.pack()

button = Button(text="Calculate", command=get_Values)
button.pack()

result_label = Label(text="")
result_label.pack()

window.mainloop()