GAME_CANVAS = document.getElementById('game-canvas');

Game = new Square.Game({
	canvas: GAME_CANVAS,
	scene: new Square.Scene({
		elements: [],
		bakcground_color: 'black',
	})
})

Input = Square.Input;

document.body.appendChild(Game.canvas);
Game._init()