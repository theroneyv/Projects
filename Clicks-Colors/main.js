const CLICK_BUTTON = document.getElementById('click-button')

const BLOP_SOUND = new Howl({
  src: ['blop.mp3'],
  volume: 0.25,
});

let score = 0;

CLICK_BUTTON.onclick = function() {
	// reproduce sound
	BLOP_SOUND.play();
    
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
