import processing.net.*; 
Client myClient; 
int valor;
 
void setup() { 
  size(200, 200); 
 
  myClient = new Client(this, "192.168.1.120", 1976);
  
  valor = 0;
} 
 
void draw() { 
} 
 
void keyReleased() 
{
  if (key == CODED) 
  {
    if (keyCode == UP)
    {
      valor &= 0xFFFFFFFE; 
    }
    else if (keyCode == DOWN)
    {
      valor &= 0xFFFFFFFD;
    }
    else if (keyCode == LEFT)
    {
      valor &= 0xFFFFFFFB;      
    }
    else if (keyCode == RIGHT)
    {
      valor &= 0xFFFFFFF7;
    }
    myClient.write(valor + 0x30);
  }
}
 
void keyPressed()
{
  if (key == CODED) 
  {
    if (keyCode == UP)
    {
      valor |= 1; 
    }
    else if (keyCode == DOWN)
    {
      valor |= 2;
    }
    else if (keyCode == LEFT)
    {
      valor |= 4;      
    }
    else if (keyCode == RIGHT)
    {
      valor |= 8;      
    }
    myClient.write(valor + 0x30);
  }
}