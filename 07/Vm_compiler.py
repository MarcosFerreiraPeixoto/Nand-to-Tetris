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
    
            
    def arg1 (self):
        '''Returns the first argument of the current command. In
        the case of C_ARITHMETIC, the command itself (add, sub, etc.)
        is returned. Should not be called if the current is C_RETURN.'''

        if self.commandType() != 'C_RETURN':
            return self.current_command[0]

    def arg2 (self):
        '''Returns the second argument of the current command. Should
        be called only if the current command is C_PUSH, C_POP, C_FUNCTION
        or C_CALL.'''

        if self.commandType() in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            return self.current_command[1:]

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

    def writePushPop (self, arg1, arg2):
        '''Writes to the output file the assembly codetha implements
        the given command, where command is either C_PUSH or C_POP.'''
        
        if arg1 == 'push':
            if arg2[0] == 'constant':
                self.file_out.write(f'\n//push constant {arg2[1]}\n@{arg2[1]}\nD=A\n@SP\nA=M \nM=D\n@SP\nM=M+1')
            elif arg2[0] == 'local':
                self.file_out.write(f'\n//push local {arg2[1]}\n@{arg2[1]}\nD=A\n@LCL\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg2[0] == 'argument':
                self.file_out.write(f'\n//push argument {arg2[1]}\n@{arg2[1]}\nD=A\n@ARG\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg2[0] == 'this':
                self.file_out.write(f'\n//push this {arg2[1]}\n@{arg2[1]}\nD=A\n@THIS\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg2[0] == 'that':
                self.file_out.write(f'\n//push that {arg2[1]}\n@{arg2[1]}\nD=A\n@THAT\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1')
            elif arg2[0] == 'static':
                self.file_out.write(f'\n//push static {arg2[1]}\n@Foo.{arg2[1]}\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
            elif arg2[0] == 'temp':
                self.file_out.write(f'\n//push temp {arg2[1]}\n@{5 + int(arg2[1])}\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
            elif arg2[0] == 'pointer':
                if arg2[1] == '0':
                    self.file_out.write(f'\n//push pointer 0\n@THIS\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
                elif arg2[1] == '1':
                    self.file_out.write(f'\n//push pointer 1\n@THAT\nD=M\n@SP\nA=M \nM=D\n@SP\nM=M+1')
        
        if arg1 == 'pop':
            if arg2[0] == 'local':
                self.file_out.write(f'\n//pop local {arg2[1]}\n@{arg2[1]}\nD=A\n@LCL\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg2[0] == 'argument':
                self.file_out.write(f'\n//pop argument {arg2[1]}\n@{arg2[1]}\nD=A\n@ARG\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg2[0] == 'this':
                self.file_out.write(f'\n//pop this {arg2[1]}\n@{arg2[1]}\nD=A\n@THIS\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg2[0] == 'that':
                self.file_out.write(f'\n//pop that {arg2[1]}\n@{arg2[1]}\nD=A\n@THAT\nD=D+M\n@R13\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@R13\nA=M\nM=D')
            elif arg2[0] == 'static':
                self.file_out.write(f'\n//pop static {arg2[1]}\n@SP\nM=M-1\nA=M\nD=M\n@Foo.{arg2[1]}\nM=D')
            elif arg2[0] == 'temp':
                self.file_out.write(f'\n//pop temp {arg2[1]}\n@SP\nM=M-1\nA=M\nD=M\n@{5 + int(arg2[1])}\nM=D')
            elif arg2[0] == 'pointer':
                if arg2[1] == '0':
                    self.file_out.write(f'\n//pop pointer 0\n@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D')
                elif arg2[1] == '1':
                    self.file_out.write(f'\n//pop pointer 1\n@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D')

    def Close (self):
        '''Closes the output file.'''

        self.file_out.close()

def main ():
    file = input('Please, insert the file name:')
    arg1 = ''
    arg2 = ''
    file_out = file[:-3] + '.asm'

    parser = Parser(file)
    code_writer = CodeWriter(file_out)

    while (parser.hasMoreCommands() == True):
        
        parser.advance()
        arg1 = parser.arg1()
        
        if parser.commandType() in ['C_PUSH', 'C_POP'] :
            arg2 = parser.arg2()
            code_writer.writePushPop(arg1, arg2)

        elif parser.commandType() == 'C_ARITHMETIC':
            code_writer.writeArithmetic(arg1)

    code_writer.Close()

if __name__ == "__main__":
    main()