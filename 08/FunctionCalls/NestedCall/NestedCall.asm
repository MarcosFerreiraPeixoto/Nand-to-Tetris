
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
//function Sys.init 0
(Sys.init)
//push constant 4000
@4000
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D
//push constant 5000
@5000
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
//call Sys.main 0
//push ret-addr
@ret-addr1
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
//goto Sys.main
@Sys.main
0;JMP
//Declares a label for the return-address
(ret-addr1)
//pop temp 1
@SP
M=M-1
A=M
D=M
@6
M=D
//label LOOP
(LOOP)
//goto LOOP
@LOOP
0;JMP
//function Sys.main 5
(Sys.main)
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
//push 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 4001
@4001
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D
//push constant 5001
@5001
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
//push constant 200
@200
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop local 1
@1
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
//push constant 40
@40
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop local 2
@2
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
//push constant 6
@6
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop local 3
@3
D=A
@LCL
D=D+M
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
//push constant 123
@123
D=A
@SP
A=M 
M=D
@SP
M=M+1
//call Sys.add12 1
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
//goto Sys.add12
@Sys.add12
0;JMP
//Declares a label for the return-address
(ret-addr2)
//pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D
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
//push local 2
@2
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 3
@3
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 4
@4
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
//function Sys.add12 0
(Sys.add12)
//push constant 4002
@4002
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop pointer 0
@SP
M=M-1
A=M
D=M
@THIS
M=D
//push constant 5002
@5002
D=A
@SP
A=M 
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
A=M
D=M
@THAT
M=D
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
//push constant 12
@12
D=A
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