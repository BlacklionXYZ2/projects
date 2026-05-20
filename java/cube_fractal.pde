float a = 0;
Box b;
ArrayList<Box> fract;
void setup(){
  size(400, 400, P3D);
  fract = new ArrayList<Box>();
  Box b = new Box(0, 0, 0, 200);
  fract.add(b);
}
void mousePressed(){
  ArrayList<Box> next = new ArrayList<Box>();
  for (Box b: fract){
    ArrayList<Box> newBoxes = b.generate();
    next.addAll(newBoxes);
  }
  fract = next;
}
void draw(){
  background(0);
  stroke(255);
  noFill();

  translate(width / 2, height / 2);
  rotateX(a);
  for (Box b: fract){
    b.show();
  }
  
  a += 0.01;
}
