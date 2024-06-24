const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let isdrawn = false;

let size = 2;

function draw(x,y) {
    ctx.beginPath();
        ctx.moveTo(0, 0);
        ctx.lineTo(x, y);
        ctx.stroke();
}

canvas.addEventListener('mousedown', (e)=>{
	isdrawn = true;
})

window.addEventListener('mouseup', (e)=>{
	isdrawn = false;
})

canvas.addEventListener('mousemove', (e)=>{
	if (isdrawn) draw(e.clientX, e.clientY);
})