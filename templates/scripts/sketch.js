var x = 0;

function preload(){
  var url = 'http://localhost:8080/';
  httpGet(url, 'text', false, function(response){
    console.log(response);
    x = response;
  });
}

function setup() {
 createCanvas(600, 400);
}

function draw() {
  
  background(0);

  if(x == 1){
    strokeWeight(0);
    textSize(32);
    text("Conecte la Placa Arduino", 290 , 210);
  }else{
  stroke(255);
  strokeWeight(4);
  noFill();
  distance = map(x, 2, 25, width , 0);

  if(x < 10){
    stroke(0, 255, 0);
  }

  ellipse(distance, 200, 100, 100);
  strokeWeight(0);
  textSize(20);
  fill(255,0,0);
  text(String(x), distance-7, 210);
  preload();
 
  }
}