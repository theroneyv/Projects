colors = {	
	'black': '30',
	'red': '31',
	'green': '32',
	'yellow': '33',
	'blue': '34',
	'purple': '35',
	'cyan': '36',
	'white': '37',
}

styles = {	
	'normal': '0',
	'bold': '1',
	'dim': '2',
}

def style(text, style, color):
	return f'\033[{style};{color}m{text}\033[0m'