""
Robot Explorador
Universidad de los Andes
Copyleft (c) 2015 Marcelo A. Peña M (Marcelo.p@ula.ve)

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

  Written in Venezuela, Universidad de los Andes.
""

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
