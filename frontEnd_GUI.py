from cProfile import label
import PySimpleGUI as PSG

inputLabel = PSG.Text('List of to do')
inputText = PSG.InputText(tooltip='Enter your to do phrase')
inputButton = PSG.Button('Add')
window = PSG.Window('My to do App', layout=[[inputLabel], [inputText, inputButton]])

window.read()
window.close()
