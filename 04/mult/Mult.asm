// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
	@R2
	M=0
	@i
	M=0
// Checking if the R0 is equal to 0, if so jump to END
	@R0
	D=M
	@END
	D;JEQ

(LOOP)
// Getting the multiplier value
	@R1 
	D=M
// Acummulating the sum
	@R2 
	M=D+M
// Adding 1 to i
	@i
	M=M+1
// Checking if the loop is over
	D=M
	@R0
	D=M-D
	@LOOP
	D;JGT
(END)
	@END
	0;JMP
	
