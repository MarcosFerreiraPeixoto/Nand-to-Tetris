
//Bootstrap code
@256
D=A
@SP
M=D
//function SimpleFunction.test 2
(SimpleFunction.test)
//push 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push local 0
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 1
@1
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
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
//not
@SP
A=M-1
M=!M
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
//push argument 1
@1
D=A
@ARG
A=M+D
D=M
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