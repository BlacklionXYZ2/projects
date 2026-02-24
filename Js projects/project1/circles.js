let pos, end_pos, direction, speed, add_vec, start_pos, dir_change, colour;
const canvas_width = 1200;
const canvas_height = 600;
let start_velocity;
let acceleration = 0.1;

function orint(string) {
  console.log(string);
}

function setup() {
  velocity = createVector(4, 4);
  start_velocity = velocity.copy();
  createCanvas(canvas_width, canvas_height, WEBGL);
  start_pos = createVector(-(canvas_width / 2), -(canvas_height / 2));
  pos = start_pos.copy();
  end_pos = start_pos.copy().mult(-1);
  direction = end_pos.copy().sub(start_pos.copy()).normalize();
}

function draw() {
  dir_change = false;
  background(200);
  orbitControl();

  if (keyIsDown(87) === true) {
    colour = (0, 255, 0);
  } else {
    colour = (255, 0, 0);
  }
  fill(colour);

  circle(pos.x, pos.y, 25);
  pos.add(p5.Vector.mult(direction, velocity));

  if (pos.x > end_pos.x && velocity.x > 0) {
    start_velocity.x *= -1;
    velocity.x *= -1;
    dir_change = true;
  } else if (pos.x < start_pos.x && velocity.x < 0) {
    start_velocity.x *= -1;
    velocity.x *= -1;
    dir_change = true;
  }
  if (pos.y > end_pos.y && velocity.y > 0) {
    start_velocity.y *= -1;
    velocity.y *= -1;
    dir_change = true;
  } else if (pos.y < start_pos.y && velocity.y < 0) {
    start_velocity.x *= -1;
    velocity.y *= -1;
    dir_change = true;
  }

  if (dir_change) {
    let rand_dir = Math.random() * 2;
    if (Math.floor(rand_dir) === 0) {
      direction.x += rand_dir / 4;
      velocity = start_velocity.copy();
    } else if (Math.floor(rand_dir) === 1) {
      direction.y += rand_dir / 4;
      velocity = start_velocity.copy();
    }
    direction.normalize();
    orint(direction.toString());
  }

  if (velocity.x > 0) {
    velocity.x += acceleration;
  } else if (velocity.x < 0) {
    velocity.x -= acceleration;
  }
  if (velocity.y > 0) {
    velocity.y += acceleration;
  } else if (velocity.y < 0) {
    velocity.y -= acceleration;
  }
}
setup();
draw();
