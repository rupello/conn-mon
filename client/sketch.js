var packet_queue = new Array();

function preload() {
  // connect to our web socket
  var hn = window.location.hostname;
  var ws = new WebSocket('ws://' + hn + ':8008/')
  ws.onmessage = function(event) { packet_queue.push(event.data); };
}

function setup() {
  createCanvas(640, 480);
}

function draw() {
  background(200);
  while(packet_queue.length>0) {
    console.info(packet_queue.shift());
    var s = createSprite(mouseX, mouseY, 30, 30);
    s.velocity.x = random(-5, 5);
    s.velocity.y = random(-5, 5);
  }
  drawSprites();
}

function mousePressed() {
  
  //create a sprite at the mouse position and store it in a temporary variable
  var s = createSprite(mouseX, mouseY, 30, 30);
  //if no image or animation is associated it will be a rectancle of the specified size
  //and a random color
  
  //now you can use the variable to set properties
  //e.g. a random velocity on the x and y coordinates
  s.velocity.x = random(-5, 5);
  s.velocity.y = random(-5, 5);
}