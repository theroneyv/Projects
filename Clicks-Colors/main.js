const button = document.getElementById('click-button')

let score = 0;

button.onclick = function() {
	score++
	button.value = score
	button.style.height = button.offsetWidth + 'px'

	let color = '#'+Math.floor(000000 + Math.random() * 999999)

	document.body.style.background = color
	button.style.color = color
}
