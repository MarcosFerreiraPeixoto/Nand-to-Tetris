// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


//BLACKEN OR CLEAR THE SCREEN
(START)	
	@24576
	D = M
	
	@UNPRESSED
	D;JEQ
(PRESSED)
	@i
	M = 0
		
	(PAINTBLACK)
	@i
	D = M
	
	@16384
	D = A + D
	A = D
	M = -1
	
	@i
	M = M + 1
	D = M
	
	@8191
	D = A - D
	@PAINTBLACK
	D;JGT
	
	// Voltando para o início do programa
	@START
	0;JMP
(UNPRESSED)
	@i
	M = 0
	
	(PAINTWHITE)
	@i
	D = M
	
	@16384
	D = A + D
	A = D
	M = 0
	
	@i
	M = M + 1
	D = M
	
	@8191
	D = A - D
	@PAINTWHITE
	D;JGT
	
	
	// Voltando para o início do programa
	@START
	0;JMP
