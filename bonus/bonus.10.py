# Building a compres
# My github token: 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

import PySimpleGUI as PSG

label1 = PSG.Text('Select files to compress')
input1 = PSG.Input()
chooseButton1 = PSG.FileBrowse('Choose')

label2 = PSG.Text('Select destination folder')
input2 = PSG.Input()
chooseButton2 = PSG.FolderBrowse('Choose')

compressButton = PSG.Button('Compress')
# creating a window variable
window = PSG.Window('File Compressor', 
layout=[[label1, input1, chooseButton1], [label2, input2, chooseButton2],[compressButton]])

window.read()
window.close()