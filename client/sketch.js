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
  }
}