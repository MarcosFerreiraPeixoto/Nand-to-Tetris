import glob, os

class Parser:
    def __init__(self, file):
        '''Opens the input file and gets ready to parse it.'''
        
        with open(file) as f:
            code = f.readlines()

        self.code = self.remove_white_space(code)
        self.counter = 0
        self.current_command = ''

    def hasMoreCommands (self):
        '''Are there more commands in the input file?'''
        
        if self.counter < len(self.code):
            return True
        else:
            return False

    def advance (self):
        '''Reads the next command from the input and makes it the
        current command. Should be called only if hasMoreCommands()
        is true. Initially there is no current command.'''

        
        self.current_command = self.code[self.counter].split()
        self.counter += 1

    def commandType (self):
        '''Returns a constant representing the type of the current
        command. C_ARITHMETIC is returned for all the arithmetic/
        logical commands.'''
        
        arithmetic_commands = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        
        if self.current_command[0] in arithmetic_commands:
            return 'C_ARITHMETIC'
        elif self.current_command[0] == 'push':
            return 'C_PUSH'
        elif self.current_command[0] == 'pop':
            return 'C_POP'
        elif self.current_command[0] == 'label':
            return 'C_LABEL'
        elif self.current_command[0] == 'goto':
            return 'C_GOTO'
        elif self.current_command[0] == 'if-goto':
            return 'C_IF'
        elif self.current_command[0] == 'call':
            return 'C_CALL'
        elif self.current_command[0] == 'function':
            return 'C_FUNCTION'
        elif self.current_command[0] == 'return':
            return 'C_RETURN'
            
    def arg1 (self, command_type):
        '''Returns the first argument of the current command. In
        the case of C_ARITHMETIC, the command itself (add, sub, etc.)
        is returned. Should not be called if the current is C_RETURN.'''
        

        if command_type == 'C_ARITHMETIC':
            return self.current_command[0]
        elif command_type != 'C_RETURN':
            return self.current_command[1]

    def arg2 (self):
        '''Returns the second argument of the current command. Should
        be called only if the current command is C_PUSH, C_POP, C_FUNCTION
        or C_CALL.'''

        if self.commandType() in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            return self.current_command[2]

    @staticmethod
    def remove_white_space (code):
        
        code_without_white_space = []
        
        for line in code:
            line = line.split('\n', 1)[0]
            line = line.split('//', 1)[0]
            line = line.strip()
            code_without_white_space.append(line)
        
        code_without_white_space = list(filter(None, code_without_white_space))
        
        return code_without_white_space 

class CodeWriter:
    def __init__(self, file):
        '''Opens the output file/stream and gets ready to write into it.'''
        self.file_out = open(file, "w")
        self.jmps = 0

        self.file_out.write('\n//Bootstrap code\n@256\nD=A\n@SP\nM=D')
        
    def writeArithmetic (self, arg1):
        '''Writes to the output file the assemply code that implements the
        givem arithmetic command.'''
        if arg1 == 'add':
            self.file_out.write('\n//add\n@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=D+M\n@SP\nA=M-1\nM=D')
        elif arg1 == 'sub':
            self.file_out.write('\n//sub\n@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@SP\nA=M-1\nM=D')
        elif arg1 == 'neg':
            self.file_out.write('\n//neg\n@SP\nA=M-1\nM=-M')
        elif arg1 == 'eq':
            self.file_out.write(f"\n//eq\n@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nD=D-M\n@{'EQ' + str(self.jmps)}\nD;JEQ\n@0\nD=A\n@SP\nA=M-1\nM=D\n@{'END' + str(self.jmps)}\n0;JMP\n({'EQ' + str(self.jmps)})\nD=-1\n@SP\nA=M-1\nM=D\n({'END' + str(self.jmps)})")
            self.jmps += 1
        elif arg1 == 'gt':
            self.file_out.write(f"\n//gt\n@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nD=M-D\n@{'GT' + str(self.jmps)}\nD;JGT\n@0\nD=A\n@SP\nA=M-1\nM=D\n@{'END' + str(self.jmps)}\n0;JMP\n({'GT' + str(self.jmps)})\nD=-1\n@SP\nA=M-1\nM=D\n({'END' + str(self.jmps)})")
            self.jmps += 1
        elif arg1 == 'lt':
            self.file_out.write(f"\n//lt\n@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nD=M-D\n@{'LT' + str(self.jmps)}\nD;JLT\n@0\nD=A\n@SP\nA=M-1\nM=D\n@{'END' + str(self.jmps)}\n0;JMP\n({'LT' + str(self.jmps)})\nD=-1\n@SP\nA=M-1\nM=D\n({'END' + str(self.jmps)})")
            self.jmps += 1
        elif arg1 == 'and':
            self.file_out.write('\n//and\n@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nD=M&D\n@SP\nA=M-1\nM=D')
        elif arg1 == 'or':
            self.file_out.write('\n//or\n@SP\nM=M-1\nA=M\nD=M\n@SP\nA=M-1\nD=M|D\n@SP\nA=M-1\nM=D')
        elif arg1 == 'not':
            self.file_out.write('\n//not\n@SP\nA=M-1\nM=!M')

    def writePushPop (self, command_type, arg1, arg2, file_name):
        '''Writes to the output file the assembly codetha implements
        the given command, where command is either C_PUSH or C_POP.'''
        
        if command_type == 'C_PUSH':
            if arg1 == 'constant':
                self.file_out.write(f'\n//push constant {arg2}\n@{arg2}\nD=A\n@SP\nA=M \nM=D\n@SP\nM=M+1')
            elif arg1 == 'local':
                self.file_out.write(f'\n//push local {arg2}\n@{arg2}\nD=A\n@LCL\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg1 == 'argument':
                self.file_out.write(f'\n//push argument {arg2}\n@{arg2}\nD=A\n@ARG\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg1 == 'this':
                self.file_out.write(f'\n//push this {arg2}\n@{arg2}\nD=A\n@THIS\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg1 == 'that':
                self.file_out.write(f'\n//push that {arg2}\n@{arg2}\nD=A\n@THAT\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg1 == 'static':
                self.file_out.write(f'\n//push static {arg2}\n@{file_name}.{arg2}\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
            elif arg1 == 'temp':
                self.file_out.write(f'\n//push temp {arg2}\n@{5 + int(arg2)}\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
            elif arg1 == 'pointer':
                if arg2 == '0':
                    self.file_out.write(f'\n//push pointer 0\n@THIS\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
                elif arg2 == '1':
                    self.file_out.write(f'\n//push pointer 1\n@THAT\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
        
        if command_type == 'C_POP':
            if arg1 == 'local':
                self.file_out.write(f'\n//pop local {arg2}\n@{arg2}\nD=A\n@LCL\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg1 == 'argument':
                self.file_out.write(f'\n//pop argument {arg2}\n@{arg2}\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg1 == 'this':
                self.file_out.write(f'\n//pop this {arg2}\n@{arg2}\nD=A\n@THIS\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg1 == 'that':
                self.file_out.write(f'\n//pop that {arg2}\n@{arg2}\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg1 == 'static':
                self.file_out.write(f'\n//pop static {arg2}\n@SP\nM=M-1\nA=M\nD=M\n@{file_name}.{arg2}\nM=D')
            elif arg1 == 'temp':
                self.file_out.write(f'\n//pop temp {arg2}\n@SP\nM=M-1\nA=M\nD=M\n@{5 + int(arg2)}\nM=D')
            elif arg1 == 'pointer':
                if arg2 == '0':
                    self.file_out.write(f'\n//pop pointer 0\n@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D')
                elif arg2 == '1':
                    self.file_out.write(f'\n//pop pointer 1\n@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D')
                    
    def writeLabel (self, arg1):
        self.file_out.write(f'\n//label {arg1}\n({arg1})')

    def writeGoto (self, arg1):
        self.file_out.write(f'\n//goto {arg1}\n@{arg1}\n0;JMP')

    def writeIf (self, arg1):
        self.file_out.write(f'\n//if-goto {arg1}\n@SP\nAM=M-1\nD=M\n@{arg1}\nD;JNE')
    
    def writeCall (self, arg1, arg2):
        self.file_out.write(f'\n//call {arg1} {arg2}\n//push ret-addr\n@ret-addr{self.jmps}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push LCL\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push ARG\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push THIS\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//push THAT\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n//ARG = SP - 5 - nArgs\n@SP\nD=M\n@5\nD=D-A\n@{arg2}\nD=D-A\n@ARG\nM=D\n//LCL = SP\n@SP\nD=M\n@LCL\nM=D\n//goto {arg1}\n@{arg1}\n0;JMP\n//Declares a label for the return-address\n(ret-addr{self.jmps})')
        self.jmps += 1
    
    def writeFunction (self, arg1, arg2):
        text =f'\n//function {arg1} {arg2}\n({arg1})'
        for i in range(int(arg2)):
            text += '\n//push 0\n@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1'
        self.file_out.write(text)
    
    def writeReturn (self):
        self.file_out.write('\n//endFrame = LCL\n@LCL\nD=M\n@endFrame\nM=D\n//retAddr = *(endFrame -5)\n@endFrame\nD=M\n@5\nA=D-A\nD=M\n@retAddr\nM=D\n//*ARG = pop()\n@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\n//SP = ARG + 1\n@ARG\nD=M+1\n@SP\nM=D\n//THAT = *(endFrame - 1)\n@endFrame\nD=M\n@1\nA=D-A\nD=M\n@THAT\nM=D\n//THIS = *(endFrame - 2)\n@endFrame\nD=M\n@2\nA=D-A\nD=M\n@THIS\nM=D\n//ARG = *(endFrame - 3)\n@endFrame\nD=M\n@3\nA=D-A\nD=M\n@ARG\nM=D\n//LCL = *(endFrame - 4)\n@endFrame\nD=M\n@4\nA=D-A\nD=M\n@LCL\nM=D\n//goto retAddr\n@retAddr\nA=M\n0;JMP')

    def Close (self):
        '''Closes the output file.'''

        self.file_out.close()

def main ():
    file_dir = input('Please, insert the file name:')

    if file_dir[-1] == '/':
        os.chdir(file_dir)
        files = glob.glob("*.vm")
        dir_name = file_dir.split('/')[-2]
        code_writer = CodeWriter(dir_name + '.asm')
        
        if 'Sys.vm' in files:
            code_writer.writeCall (arg1='Sys.init', arg2='0')
    else:
        files = [file_dir]
        code_writer = CodeWriter(files[0] + '.asm')

    

    for file in files:

        arg1 = ''
        arg2 = ''

        parser = Parser(file)

        while (parser.hasMoreCommands() == True):
            parser.advance()
            command_type = parser.commandType()
            arg1 = parser.arg1(command_type)
            
            if command_type in ['C_PUSH', 'C_POP'] :
                arg2 = parser.arg2()
                code_writer.writePushPop(command_type, arg1, arg2, file)

            elif command_type == 'C_ARITHMETIC':
                code_writer.writeArithmetic(arg1)

            elif command_type == 'C_LABEL':
                code_writer.writeLabel(arg1)

            elif command_type == 'C_GOTO':
                code_writer.writeGoto(arg1)

            elif command_type == 'C_IF':
                code_writer.writeIf(arg1)

            elif command_type == 'C_CALL':
                arg2 = parser.arg2()
                code_writer.writeCall(arg1, arg2)

            elif command_type == 'C_FUNCTION':
                arg2 = parser.arg2()
                code_writer.writeFunction(arg1, arg2)

            elif command_type == 'C_RETURN':
                code_writer.writeReturn()

    code_writer.Close()

if __name__ == "__main__":
    main()