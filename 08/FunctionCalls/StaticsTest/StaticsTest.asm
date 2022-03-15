
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
//function Class1.set 0
(Class1.set)
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
//pop static 0
@SP
M=M-1
A=M
D=M
@Class1.vm.0
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
//pop static 1
@SP
M=M-1
A=M
D=M
@Class1.vm.1
M=D
//push constant 0
@0
D=A
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
//function Class1.get 0
(Class1.get)
//push static 0
@Class1.vm.0
D=M
@SP
A=M 
M=D
@SP
M=M+1
//push static 1
@Class1.vm.1
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
//function Class2.set 0
(Class2.set)
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
//pop static 0
@SP
M=M-1
A=M
D=M
@Class2.vm.0
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
//pop static 1
@SP
M=M-1
A=M
D=M
@Class2.vm.1
M=D
//push constant 0
@0
D=A
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
//function Class2.get 0
(Class2.get)
//push static 0
@Class2.vm.0
D=M
@SP
A=M 
M=D
@SP
M=M+1
//push static 1
@Class2.vm.1
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
//function Sys.init 0
(Sys.init)
//push constant 6
@6
D=A
@SP
A=M 
M=D
@SP
M=M+1
//push constant 8
@8
D=A
@SP
A=M 
M=D
@SP
M=M+1
//call Class1.set 2
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
@2
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class1.set
@Class1.set
0;JMP
//Declares a label for the return-address
(ret-addr1)
//pop temp 0
@SP
M=M-1
A=M
D=M
@5
M=D
//push constant 23
@23
D=A
@SP
A=M 
M=D
@SP
M=M+1
//push constant 15
@15
D=A
@SP
A=M 
M=D
@SP
M=M+1
//call Class2.set 2
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
@2
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class2.set
@Class2.set
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
//call Class1.get 0
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
@0
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class1.get
@Class1.get
0;JMP
//Declares a label for the return-address
(ret-addr3)
//call Class2.get 0
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
@0
D=D-A
@ARG
M=D
//LCL = SP
@SP
D=M
@LCL
M=D
//goto Class2.get
@Class2.get
0;JMP
//Declares a label for the return-address
(ret-addr4)
//label WHILE
(WHILE)
//goto WHILE
@WHILE
0;JMP