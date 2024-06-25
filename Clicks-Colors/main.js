const CLICK_BUTTON = document.getElementById('click-button')

let score = 0;

CLICK_BUTTON.onclick = function() {
	// increase score
	score++
	CLICK_BUTTON.value = score
	CLICK_BUTTON.style.height = CLICK_BUTTON.offsetWidth + 'px'
	
	// get a random color
	let color = '#'+Math.floor(000000 + Math.random() * 999999)

	// change the background color
	document.body.style.background = color
	CLICK_BUTTON.style.color = color

	// achievement
	if (ACHIEVEMENTS[''+score]) {
		console.log(score+': '+ACHIEVEMENTS[''+score])
	}
}
