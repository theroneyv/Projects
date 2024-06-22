class Box extends Square.Element {

	constructor(x, y, w, h, color = 'black') {
		super();

		this.setTransform(x, y, w, h);
		this.color = color;
	}
}

food = new Box(320, 200, 20, 20);
player = new Box(320, 240, 20, 20, 'lightgray');

Game.scene.instance([food, player]);

SCORE_TEXT = document.getElementById('score-text');

score = 0;

Game.update = function() {	
	// cambiar color
	let color = Square.randint(100000, 999999);
	food.color = '#' + color;

	// rotar
	food.rotate += 0.1;

	// movimiento
	speed = 6;

	if (Input.iskeydown('ArrowLeft')) {
		player.vel.x = -speed;
		player.vel.y = 0;
	}
	else if (Input.iskeydown('ArrowRight')) {
		player.vel.x = speed;
		player.vel.y = 0;
	}
	else if (Input.iskeydown('ArrowUp')) {
		player.vel.y = -speed;
		player.vel.x = 0;
	}
	else if (Input.iskeydown('ArrowDown')) {
		player.vel.y = speed;
		player.vel.x = 0;
	}

	// comida (puntaje)
	if (Game.iscollision(player, food)) {
		// aumentar mostrar puntaje
		score += 1;
		SCORE_TEXT.innerText = score;

		// cambiar la posicion 
		food.transform.x = Square.randint(40, 560);
		food.transform.y = Square.randint(40, 400);
	}
}