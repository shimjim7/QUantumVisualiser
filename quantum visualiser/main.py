import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import tkinter as tk
from tkinter import RIGHT,NORMAL
from tkinter import END, DISABLED
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#defining the popup window
root = tk.Tk()
root.title("Quantum Visualiser")
root.geometry('399x427')
background = '#97ccf0'
buttons = '#486375'
sp_buttons ='#104263'
buttonFont = ('Arial', 18)
displayFont = ('Arial', 28)

#initialising the quantum circuit
def initialise_circuit():
    global circuit
    circuit = QuantumCircuit(1)
initialise_circuit()
theta = 0

#Defining Functions
def visualise_circuit(circuit, window):
    try:
        visualize_transition(circuit=circuit)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()

def display_gate(gate_input):
    display.insert(END, gate_input)
    input_gates = display.get()
    numGates = len(input_gates)
    searchWord = ["R", "D"]
    countDoubleValued_Gates = [input_gates.count(i) for i in searchWord]
    numGates -= sum(countDoubleValued_Gates)
    if numGates == 10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard]
        for gate in gates:
            gate.config(state=DISABLED)

def change_theta(num, window, circuit, key):
    global theta
    theta = num*np.pi

    if key == 'x':
        circuit.rx(theta,0)
        theta = 0
    elif key == 'y':
        circuit.ry(theta, 0)
        theta = 0
    else:
        circuit.rz(theta,0)
        theta = 0
    window.destroy()

def user_input(circuit, key):
    getInput = tk.Tk()
    getInput.title('Theta value')

    val1 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='pi/4', command= lambda:change_theta(0.25, getInput, circuit, key))
    val1.grid(row=0, column=0)

    val2 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='pi/2', command= lambda:change_theta(0.50, getInput, circuit, key))
    val2.grid(row=0, column=1)

    val3 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='pi', command= lambda:change_theta(1.0, getInput, circuit, key))
    val3.grid(row=0, column=2)

    val4 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='2*pi', command= lambda:change_theta(2.0, getInput, circuit, key))
    val4.grid(row=0, column=3)

    nval1 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='-pi/4', command= lambda:change_theta(-0.25, getInput, circuit, key))
    nval1.grid(row=1, column=0)

    nval2 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='-pi/2', command= lambda:change_theta(-0.50, getInput, circuit, key))
    nval2.grid(row=1, column=1)

    nval3 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='-pi', command= lambda:change_theta(-1.0, getInput, circuit, key))
    nval3.grid(row=1, column=2)

    nval4 = tk.Button(getInput, height=2, width=10, bg=buttons, font=("Arial",10), text='-2*pi', command= lambda:change_theta(-2.0, getInput, circuit, key))
    nval4.grid(row=1, column=3)

    text_obj = tk.Text(getInput, height=20, width=20, bg="Light cyan")
    note = """
    value ranges from -2pi to 2pi
    """
    text_obj.grid(sticky="WE", columnspan=4)
    text_obj.insert(END,note)

    getInput.mainloop()

def about():
    info = tk.Tk()
    info.title('About proj')
    text = tk.Text(info, height = 20, width = 20)

    label = tk.Label(info, text= 'About this project')
    label.config(font=("Arial",14))

    text_to_display = """
    Thsi project hlps visualise rotation results after
    different gates and their combinations are applied
    """

    label.pack()
    text.pack(fill = 'both', expand=True)

    text.insert(END, text_to_display)
    info.mainloop()

def clear(circuit):
    display.delete(0,END)
    initialise_circuit()
    if x_gate['state'] == DISABLED:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, hadamard]
        for gate in gates:
            gate.config(state=NORMAL)


#defining frames
displayFrame = tk.LabelFrame(root)
buttonFrame = tk.LabelFrame(root, bg='black')
displayFrame.pack()
buttonFrame.pack(fill ='both', expand =True)
#defining frame layout
display = tk.Entry(displayFrame, width=120, font=displayFont, bg=background, borderwidth=10, justify=RIGHT)
display.pack(padx=3, pady=4)

#defining first row of buttons
x_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='X', command=lambda:[display_gate('x'),circuit.x(0)])
y_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='Y', command=lambda:[display_gate('y'),circuit.y(0)])
z_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='Z', command=lambda:[display_gate('z'),circuit.z(0)])
x_gate.grid(row=0, column=0,ipadx=45,ipady=1)
y_gate.grid(row=0, column=1,ipadx=45,ipady=1)
z_gate.grid(row=0, column=2,ipadx=45,ipady=1,sticky='E')

#defining 2nd row of buttons
Rx_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='RX', command=lambda:[display_gate('Rx'),user_input(circuit,'x')])
Ry_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='RY', command=lambda:[display_gate('Ry'),user_input(circuit,'y')])
Rz_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='RZ', command=lambda:[display_gate('Rz'),user_input(circuit,'z')])
Rx_gate.grid(row=1, column=0,columnspan=1,pady=1,sticky='WE')
Ry_gate.grid(row=1, column=1,columnspan=1,pady=1,sticky='WE')
Rz_gate.grid(row=1, column=2,columnspan=1,pady=1,sticky='WE')

#defining 3rd row of buttons
s_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='S', command=lambda:[display_gate('s'),circuit.s(0)])
sd_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='SD', command=lambda:[display_gate('SD'),circuit.sdg(0)])
hadamard = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='H', command=lambda:[display_gate('H'),circuit.h(0)])
s_gate.grid(row=2, column=0,columnspan=1,pady=1, sticky='WE')
sd_gate.grid(row=2, column=1,sticky='WE',pady=1)
hadamard.grid(row=2, column=2,rowspan=2,pady=1,sticky='WENS')

#defining 4th row of buttons
t_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='T', command=lambda:[display_gate('t'),circuit.t(0)])
td_gate = tk.Button(buttonFrame, font=buttonFont, bg=buttons, text='TD', command=lambda:[display_gate('TD'),circuit.tdg(0)])
t_gate.grid(row=3, column=0,pady=1, sticky='WE')
td_gate.grid(row=3, column=1,sticky='WE',pady=1)

#defining quit and visual
quit = tk.Button(buttonFrame, font=buttonFont, bg=sp_buttons, text='Quit', command=root.destroy)
visualise = tk.Button(buttonFrame, font=buttonFont, bg=sp_buttons, text='Visualise', command=lambda:visualise_circuit(circuit,root))
quit.grid(row=4, column=0,columnspan=2, pady=1, sticky='WE',ipadx=5)
visualise.grid(row=4, column=2,columnspan=1,sticky='WE',pady=1,ipadx=8)

#defining quit and visual
clear_bt = tk.Button(buttonFrame, font=buttonFont, bg=sp_buttons, text='Clear', command=lambda:clear(circuit))
clear_bt.grid(row=5, column=0,columnspan=3, sticky='WE')
about_bt = tk.Button(buttonFrame, font=buttonFont, bg=sp_buttons, text='About', command=about)
about_bt.grid(row=6, column=2,columnspan=3,sticky='WE')

root.mainloop()