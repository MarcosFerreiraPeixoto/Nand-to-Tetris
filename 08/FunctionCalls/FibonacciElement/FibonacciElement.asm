
//Bootstrap code
@256
D=A
@SP
M=D
//call Sys.init 0
//push ret-addr
@ret-addr0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP - 5 - nArgs
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Sys.init
@Sys.init
0;JMP
//Declares a label for the return-address
(ret-addr0)
//function Main.fibonacci 0
(Main.fibonacci)
//push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M 
M=D
@SP
M=M+1
//lt
@SP
M=M-1
A=M
D=M
@SP
A=M-1
D=M-D
@LT1
D;JLT
@0
D=A
@SP
A=M-1
M=D
@END1
0;JMP
(LT1)
D=-1
@SP
A=M-1
M=D
(END1)
//if-goto IF_TRUE
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE
//goto IF_FALSE
@IF_FALSE
0;JMP
//label IF_TRUE
(IF_TRUE)
//push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//endFrame = LCL
@LCL
D=M
@endFrame
M=D
//retAddr = *(endFrame -5)
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
//*ARG = pop()
@SP
AM=M-1
D=M
@ARG
A=M
M=D
//SP = ARG + 1
@ARG
D=M+1
@SP
M=D
//THAT = *(endFrame - 1)
@endFrame
D=M
@1
A=D-A
D=M
@THAT
M=D
//THIS = *(endFrame - 2)
@endFrame
D=M
@2
A=D-A
D=M
@THIS
M=D
//ARG = *(endFrame - 3)
@endFrame
D=M
@3
A=D-A
D=M
@ARG
M=D
//LCL = *(endFrame - 4)
@endFrame
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto retAddr
@retAddr
A=M
0;JMP
//label IF_FALSE
(IF_FALSE)
//push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M 
M=D
@SP
M=M+1
//sub
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
A=M-1
M=D
//call Main.fibonacci 1
//push ret-addr
@ret-addr2
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP - 5 - nArgs
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Main.fibonacci
@Main.fibonacci
0;JMP
//Declares a label for the return-address
(ret-addr2)
//push argument 0
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M 
M=D
@SP
M=M+1
//sub
@SP
M=M-1
A=M
D=M
A=A-1
D=M-D
@SP
A=M-1
M=D
//call Main.fibonacci 1
//push ret-addr
@ret-addr3
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP - 5 - nArgs
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Main.fibonacci
@Main.fibonacci
0;JMP
//Declares a label for the return-address
(ret-addr3)
//add
@SP
M=M-1
A=M
D=M
A=A-1
D=D+M
@SP
A=M-1
M=D
//endFrame = LCL
@LCL
D=M
@endFrame
M=D
//retAddr = *(endFrame -5)
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
//*ARG = pop()
@SP
AM=M-1
D=M
@ARG
A=M
M=D
//SP = ARG + 1
@ARG
D=M+1
@SP
M=D
//THAT = *(endFrame - 1)
@endFrame
D=M
@1
A=D-A
D=M
@THAT
M=D
//THIS = *(endFrame - 2)
@endFrame
D=M
@2
A=D-A
D=M
@THIS
M=D
//ARG = *(endFrame - 3)
@endFrame
D=M
@3
A=D-A
D=M
@ARG
M=D
//LCL = *(endFrame - 4)
@endFrame
D=M
@4
A=D-A
D=M
@LCL
M=D
//goto retAddr
@retAddr
A=M
0;JMP
//function Sys.init 0
(Sys.init)
//push constant 4
@4
D=A
@SP
A=M 
M=D
@SP
M=M+1
//call Main.fibonacci 1
//push ret-addr
@ret-addr4
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//ARG = SP - 5 - nArgs
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Main.fibonacci
@Main.fibonacci
0;JMP
//Declares a label for the return-address
(ret-addr4)
//label WHILE
(WHILE)
//goto WHILE
@WHILE
0;JMP