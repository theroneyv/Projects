const Square = {}

Square.Game = class Game { 

	constructor(game) {

		this.canvas = game.canvas;
		this.canvas_render = this.canvas.getContext('2d');

		this.scene = game.scene;

		this._loop = ()=>{
			this.canvas_render.clearRect(0, 0, this.canvas.width, this.canvas.height);
			this._update();
			requestAnimationFrame(this._loop);
		}
	}

	load() {
		// ...
	}

	update() {
		// ...
	}

	iscollision(a, b) {
		a = a.transform;
		b = b.transform;

		return this.collisionRect(a, b);
	}

	collisionRect(a, b) {
		return (a.x + a.w >= b.x && a.x <= b.x + b.w &&
				a.y + a.h >= b.y && a.y <= b.y + b.h)
	}

	_load() {

		window.addEventListener('keydown', (e)=>{
			if (Square.Input.Keyboard[e.key]) {
				Square.Input.Keyboard[e.key].isdown = true;
			}
		})

		window.addEventListener('keypress', (e)=>{
			if (Square.Input.Keyboard[e.key]) {
				Square.Input.Keyboard[e.key].ispress = true;
				requestAnimationFrame(()=>{Square.Input.Keyboard[e.key].ispress = false;})
			}
		})

		window.addEventListener('keyup', (e)=>{
			if (Square.Input.Keyboard[e.key]) {
				Square.Input.Keyboard[e.key].isup = true;
				Square.Input.Keyboard[e.key].isdown = false;
				requestAnimationFrame(()=>{Square.Input.Keyboard[e.key].isup = false;})
			}
		})

		this.canvas.addEventListener('mousemove', (e)=>{
			let bcr = this.canvas.getBoundingClientRect();

			Square.Input.Mouse.x = Math.floor(e.clientX - bcr.y);
			Square.Input.Mouse.y = Math.floor(e.clientY - bcr.y);
		})

		this.canvas.oncontextmenu = function(e) { e.preventDefault(); e.stopPropagation(); }

		this.canvas.addEventListener('mousedown', (e)=>{
			let button = '';

			if (e.buttons == 1) {
				button = 'LeftButton';
			} 
			else if (e.buttons == 2) {
				button = 'RightButton';
			}

			Square.Input.Mouse[button].isup = true;
		})
	}

	_update() {
		this.update();
		this.scene._update(this);
	}

	_init() {
		this._load();
		this.load();
		this._loop();
	}
}

Square.Scene = class Scene { 

	constructor(scene) {

		this.elements = scene.elements || [];
		this.bakcground_color = scene.bakcground_color || 'lightgray'; 
	}

	instance(elmt) {
		if (elmt.length) {
			elmt.forEach((e)=>{
				this.elements.push(e);
			})
		}
		else {
			this.elements.push(elmt);
		}
	}

	_update(game) {
		game.canvas_render.fillStyle = this.bakcground_color;
		game.canvas_render.fillRect(0, 0, game.canvas.width, game.canvas.height);

		this.elements.forEach((elmt)=>{
			if (elmt) {
				elmt._update(game)
			}
		})
	}
}

Square.Element = class Element {

	constructor(elmt) {

		this.setTransform(0, 0, 0, 0);
		this.setVel(0, 0);
		this.rotate = 0;

		this.color = "black";
	}

	update() {
		// ...
	}
	
	setTransform(x, y, w, h) {
		this.transform = {
			x: x,
			y: y,
			w: w,
			h: h
		}
	}

	setVel(x, y) {
		this.vel = {
			x: x,
			y: y
		}
	}

	_update(game) {
		this._move();
		this._draw(game.canvas_render);
	}

	_move() {
		this.transform.x += this.vel.x;
		this.transform.y += this.vel.y;
	}

	_draw(canvas_render) {
		canvas_render.translate(this.transform.x, this.transform.y)
		canvas_render.rotate(this.rotate);

		canvas_render.fillStyle = this.color;
		
		canvas_render.fillRect(
			-this.transform.w / 2,
			-this.transform.h / 2,
			this.transform.w,
			this.transform.h
			)
		
		canvas_render.rotate(-this.rotate);		
		canvas_render.translate(-this.transform.x, -this.transform.y);
	}	
}

Square.Input = {
	Keyboard: {
		'ArrowUp': {'isdown':false, 'isup':false, 'ispress':false},
		'ArrowLeft': {'isdown':false, 'isup':false, 'ispress':false},
		'ArrowDown': {'isdown':false, 'isup':false, 'ispress':false},
		'ArrowRight': {'isdown':false, 'isup':false, 'ispress':false},
	},

	iskeydown: function(key) {
		if (Square.Input.Keyboard[key]) {
			return Square.Input.Keyboard[key].isdown;
		}
	},

	iskeyup: function(key) {
		if (Square.Input.Keyboard[key]) {
			return Square.Input.Keyboard[key].isup;
		}
	},

	iskeypress: function(key) {
		if (Square.Input.Keyboard[key]) {
			return Square.Input.Keyboard[key].ispress;
		}
	},

	Mouse: {
		'x': 0,
		'y': 0,
		'LeftButton': {'isdown':false, 'isup':false},
		'RightButton': {'isdown':false, 'isup':false},
	}
}

Square.createCanvas = function(width, height) {
	
	let canvas = document.createElement('canvas');
		canvas.width = width;
		canvas.height = height;
	
	return canvas;
}

Square.loadImage = function(src) {

	let img = new Image();
		img.src = src;

	return img;
}

Square.randint = function(min, max) {
	return Math.floor(min + Math.random() * max)
}