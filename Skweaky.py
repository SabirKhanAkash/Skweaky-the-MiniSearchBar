import wolframalpha
client = wolframalpha.Client("3UR8GP-8XXK9AYYH5")
global flag

import PySimpleGUI as gui 
gui.theme('DarkAmber')
layout = [
	[gui.Text('           HELLO! WELCOME TO Skweaky...! ')],
	[gui.Text('')],
	[gui.Text('')],
	[gui.Text('ENTER YOUR QUERY: ')], 
	[gui.InputText()], 
	[gui.Text('                         '), gui.Button('Ok'), gui.Button('Cancel')]	
]
window = gui.Window('Skweaky',layout, finalize=True, use_ttk_buttons=True)

while True:
	event, values = window.read()
	if event in (None, 'Cancel'):
		break
	for i in range(25000):
		gui.PopupAnimated(gui.DEFAULT_BASE64_LOADING_GIF, background_color='#2c2825', time_between_frames=100)

	gui.PopupAnimated(None)
	res = client.query(values[0])
	gui.Popup('     '+next(res.results).text+'       ')

window.close()
