int cols, rows;
int scl = 20;
int w = 3000;
int h = 2000;

import processing.sound.*;

AudioIn in;
FFT fft;
Amplitude amp;
int bands = 512;
float[] spectrum = new float[bands];




float[][] terrain; 
float flying = 0;

void setup () {
  size(900, 600, P3D);
  cols = w/scl;
  rows = h/scl;
  terrain = new float [cols][rows];
  
  fft = new FFT(this,bands);
  amp = new Amplitude(this);
  in = new AudioIn(this,0);
  
  fft.input(in);
  in.start();
  amp.input(in);
  
}

void draw () {
  float vol = amp.analyze()*20;
  int specVal = int(random(bands));
  println("SpecVal: " + specVal);
  float freq = spectrum[specVal]*10000000;
  println("Freq: " + freq);
  float c = map(freq, 0, 2, 0,1);
  
  
  flying-=vol;
  float yoff = flying;
  for (int y = 0; y<rows; y++){
    float xoff = 0;
    for (int x = 0; x < cols; x++) { 
      terrain[x][y] = map(noise(xoff,yoff),0,1,-120,120);
      xoff+=0.15;   
    }
    yoff+=0.15;
  }
  background(255);
    
  translate(width/2,height/3);
  rotateX(PI/3);
  translate(-w/3,-h/2);
  noFill();
  fft.analyze(spectrum);
    for (int y = 0; y<rows-1; y++) {
      stroke(map(y,rows,0,0,255));
      beginShape(TRIANGLE_STRIP);
      for (int x = 0; x < cols; x++) { 
        vertex(x*scl,y*scl, terrain[x][y]);
        vertex(x*scl,(y+1)*scl, terrain[x][y+1]);
      }
      endShape();
    }
}
