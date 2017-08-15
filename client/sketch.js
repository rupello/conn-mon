var packet_queue = new Array();

function preload() {
  // connect to our web socket on port 8008
  var ws = new WebSocket('ws://' + window.location.hostname + ':8008/')
  ws.onmessage = function(event) { 
    packet_queue.push(event.data); 
    // limit queue length..
    while(packet_queue.length>100) {
     packet_queue.shift();
    }
  };

}

function setup() {
  createCanvas(640, 480);
}

function draw() {
  background(200);
  while(packet_queue.length>0) {
    p = packet_queue.shift();
    var s = createSprite(width/2, height/2, 30, 30);
    s.draw = drawCreature ;
    s.tag = p;
    s.velocity.x = random(-5, 5);
    s.velocity.y = random(-5, 5);
  }
  drawSprites();
}

function mousePressed() {

}

function drawCreature() {
  beginShape();
  vertex(50, 120);
  vertex(100, 90);
  vertex(110, 60);
  vertex(80, 20);
  vertex(210, 60);
  vertex(160, 80);
  vertex(200, 90);
  vertex(140, 100);
  vertex(130, 120);
  endShape();
  fill(0);
  ellipse(155, 60, 8, 8)
  text(this.tag,100,50);
};