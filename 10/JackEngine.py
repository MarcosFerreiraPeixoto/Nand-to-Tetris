import glob, os, re

class JackTokenizer:
    def __init__(self, file):
        with open(file) as f:
            '''Opens the input .jack file and gets ready to tokenize it.'''
            self.code = f.readlines()
            self.code = self.removeWhiteSpace(self.code)
            
            self.tokens = self.getTokens(self.code)
            self.counter = 0
            self.current_token = ''         

    def hasMoreTokens (self):
        '''Are there more commands in the input file?'''
        
        if self.counter < len(self.tokens):
            return True
        else:
            return False

    def advance (self):
        '''Reads the next token and makes it the current 
        token. Should be called only if hasMoreCommands()
        is true. Initially there is no current command.'''

        
        self.current_token = self.tokens[self.counter]
        self.counter += 1
    
    def tokenType (self):
        '''Returns the type of the current token, as a
        constant.'''
        
        key_words = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
        symbols = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~', '&lt;', '&gt;', '&amp;']

        if self.current_token in key_words:
            return 'keyword'
        elif self.current_token in symbols:
            return 'symbol'
        elif self.current_token[0] == '"' or self.current_token[0] == "'":
            return 'string_const'
        elif self.current_token.isnumeric():
            return 'int_const'
        else:
            return 'identifier'

    def keyWord (self):
       return f'<keyword> {self.current_token} </keyword>\n'
    
    def symbol (self):
        symbol = self.current_token

        if symbol == '<':
            symbol = '&lt;'
        elif symbol == '>':
            symbol = '&gt;'
        elif symbol == '&':
            symbol = '&amp;'

        return f'<symbol> {symbol} </symbol>\n'
    
    def identifier (self):
        return f'<identifier> {self.current_token} </identifier>\n'
    
    def intVal (self):
        return f'<integerConstant> {self.current_token} </integerConstant>\n'
    
    def stringVal (self):
        return "<stringConstant> " + self.current_token.replace('"','').strip() + " </stringConstant>\n"

    @staticmethod
    def removeWhiteSpace (code):
        
        code_without_white_space = []
        comment = False

        for line in code:
            if line[:2] == '/**':
                comment = True
            if line[-2:] == '*/':
                comment = False
            
            if comment == True:
                line = line.split('*',1)[0]
                line = line.split('\n', 1)[0]
                line = line.split('//', 1)[0]
                line = line.split('/**',1)[0]
                line = line.split('/*',1)[0]
                line = line.strip()
            else:
                line = line.split('\n', 1)[0]
                line = line.split('//', 1)[0]
                line = line.split('/**',1)[0]
                line = line.split('/*',1)[0]
                line = line.strip()
                code_without_white_space.append(line)
        
        code_without_white_space = list(filter(None, code_without_white_space))
        
        return code_without_white_space

    @staticmethod
    def getTokens (code_without_white_space):
        token_list = []

        #Creating a list with all tokens
        for code_line in code_without_white_space:
            code_line = re.split('(")', code_line) #Spliting the Strings
            j = 0
            while (j < len(code_line)):
                
                #Dealing with StringConstant Tokens
                if code_line[j] == '"':
                    token_list.append('"' + code_line[j+1] + '"')
                    j += 2
                
                #Dealing with all other tokens
                else:
                    tokens = re.split('(\W)', code_line[j])
                    for token in tokens:
                        token_list.append(token)
                
                j += 1
        
        token_list = [token for token in token_list if (token != '' and token != ' ')]

        return token_list

class JackEngine:
    def __init__(self, file, tokenizer):
        '''Opens the output file/stream and gets ready to write into it.'''
        self.file_out = open(file, "w")
        self.jmps = 0
        #self.tokenizer = JackTokenizer('test.jack()') ##MODIFICAR PAR self.tokenizer = tokenizer
        self.tokenizer = tokenizer
        
        self.type = ['int', 'char', 'boolean']
        self.statements = ['let', 'if', 'while', 'do', 'return']
        self.op = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
        
    def compileClass (self):
        '''Writes to the output file the assemply code that implements the
        givem arithmetic command.'''

        # 'class'
        self.file_out.write('<class>\n')
        self.compile()
        self.tokenizer.advance()
        
        # 'className'
        if self.tokenizer.tokenType() == 'identifier':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected an identifier" + f"instead found: '{self.tokenizer.current_token}'")

        # '{'
        if self.tokenizer.current_token == '{':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected '{' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # 'classVarDec'*
        if self.tokenizer.current_token in ['static', 'field']:
            while (self.tokenizer.current_token in ['static', 'field']):
                self.compileClassVarDec()
                self.tokenizer.advance()
          
        # 'subroutineDec'*
        if self.tokenizer.current_token in ['constructor', 'function', 'method']:          
            while (self.tokenizer.current_token in ['constructor', 'function', 'method']):
                self.compileSubroutine()
                self.tokenizer.advance()
      
        # '}'
        if self.tokenizer.current_token == '}':
            self.compile()
        else:
            raise Exception("Expected '}' " + f"instead found: '{self.tokenizer.current_token}'")
        
        self.file_out.write('</class>\n')


    def compileClassVarDec (self):
        
        self.file_out.write('<classVarDec>\n')

        # ('static' | 'field')
        self.compile()
        self.tokenizer.advance()

        # type | className
        if (self.tokenizer.current_token in self.type) or (self.tokenizer.tokenType() == 'identifier'):
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected 'int', 'char' or 'boolean' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # varName
        if self.tokenizer.tokenType() == 'identifier':
                self.compile()
                self.tokenizer.advance()
        else:
            raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")
            

        while (self.tokenizer.current_token == ','):
            
            self.compile()
            self.tokenizer.advance()           
            

            # varName
            if self.tokenizer.tokenType() == 'identifier':
                self.compile()
                self.tokenizer.advance()
            else:
                raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")

        if self.tokenizer.current_token == ';':
                self.compile()              
        else:
            raise Exception("Expected ';' " + f"instead found: '{self.tokenizer.current_token}'")

        self.file_out.write('</classVarDec>\n')
    
    def varDec(self):
        
        self.file_out.write('<varDec>\n')

        # ('var')
        self.compile()
        self.tokenizer.advance()

        # type
        if (self.tokenizer.current_token in self.type) or self.tokenizer.tokenType() == 'identifier':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected 'int', 'char' or 'boolean' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # varName
        if self.tokenizer.tokenType() == 'identifier':
                self.compile()
                self.tokenizer.advance()
        else:
            raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")
            

        while (self.tokenizer.current_token != ';'):
            
            # ','
            if self.tokenizer.current_token == ',':
                self.compile()     
                self.tokenizer.advance()         
            else:
                raise Exception("Expected ',' " + f"instead found: '{self.tokenizer.current_token}'")

            # varName
            if self.tokenizer.tokenType() == 'identifier':
                self.compile()
                self.tokenizer.advance()
            else:
                raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")

        if self.tokenizer.current_token == ';':
                self.compile()              
        else:
            raise Exception("Expected ';' " + f"instead found: '{self.tokenizer.current_token}'")
        
        self.file_out.write('</varDec>\n')

    def compile (self):
        token_type = self.tokenizer.tokenType()

        if token_type == 'keyword': 
            self.file_out.write(self.tokenizer.keyWord())

        elif token_type == 'symbol':
            self.file_out.write(self.tokenizer.symbol())

        elif token_type == 'int_const':
            self.file_out.write(self.tokenizer.intVal())

        elif token_type == 'string_const':
            self.file_out.write(self.tokenizer.stringVal())
        
        elif token_type == 'identifier':
            self.file_out.write(self.tokenizer.identifier())

    def compileTerm (self):
        self.file_out.write(f"<term>\n")
        
        # integerConstant | stringConstant | keywordConstant | varName | varName'[' expression ']' 
        # | '(' expression ')' | (unaryOp term) | subroutineCall
        token_type = self.tokenizer.tokenType()

        # integerConstant
        if token_type == 'int_const':
            self.compile()

        # stringConstant
        elif token_type == 'string_const':
            self.compile()
            
        # keywordConstant
        elif self.tokenizer.current_token in ['true', 'false', 'null', 'this']:
            #Não sei se é só <keyword>\n ou <keywordConstant>\n
            self.compile()
            #self.file_out.write(f"<keywordConstant>\n {self.tokenizer.current_token} </keywordConstant>\n")

        # varName | varName'[' expression ']' | subroutineName '(' expressionList ')' | 
        # (className | varName)'.'subroutineName'(' expressionList ')'
        elif token_type == 'identifier':
            self.tokenizer.advance()
                
            # varName '[' expression ']' 
            if self.tokenizer.current_token == '[':
                self.tokenizer.counter -= 1 #Retrocendo 1

                #varName 
                self.compile()
                self.tokenizer.advance()

                # '['
                self.compile()
                self.tokenizer.advance()
                    
                # expression
                self.compileExpression()
                self.tokenizer.advance()

                # ']'
                if self.tokenizer.current_token == ']':
                    self.compile()
                else:
                    raise Exception("Expected ']' " + f"instead found: '{self.tokenizer.current_token}'")
                
            #subroutineName '(' expressionList ')' 
            elif self.tokenizer.current_token == '(':
                self.tokenizer.counter -= 1 #Retrocendo 1

                #varName 
                self.compile()
                self.tokenizer.advance()

                # '('
                self.compile()
                self.tokenizer.advance()

                # expressionList
                self.compileExpressionList()
                self.tokenizer.advance()

                # ')'
                if self.tokenizer.current_token == ')':
                    self.compile()
                else:
                   raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")
                
            # (className | varName)'.'subroutineName'(' expressionList ')'
            elif self.tokenizer.current_token == '.':
                self.tokenizer.counter -= 1 #Retrocendo 1

                #varName 
                self.compile()
                self.tokenizer.advance()

                # '.'
                self.compile()
                self.tokenizer.advance()
                    
                # subroutineName
                if self.tokenizer.tokenType() == 'identifier':
                    self.compile()
                    self.tokenizer.advance()
                else:
                   raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")
                
                # '('
                if self.tokenizer.current_token == '(':
                    self.compile()
                    self.tokenizer.advance()
                else:
                   raise Exception("Expected '(' " + f"instead found: '{self.tokenizer.current_token}'")

                # expressionList
                self.compileExpressionList()
                self.tokenizer.advance()

                # ')'
                if self.tokenizer.current_token == ')':
                    self.compile()
                else:
                   raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")

            # varName
            else:
                self.tokenizer.counter -= 1 #Retrocendo 1
                #varName 
                self.compile()
            
        # '(' expression ')'
        elif self.tokenizer.current_token == '(':
               self.compile()
               self.tokenizer.advance()

               self.compileExpression()
               self.tokenizer.advance()

               if self.tokenizer.current_token == ')':
                   self.compile()
               else:
                   raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")
            
        # (unaryOp term)
        elif self.tokenizer.current_token in ['-', '~']:
            self.compile()
            self.tokenizer.advance()

            self.compileTerm()
            
        self.file_out.write(f"</term>\n")

    def compileSubroutine (self):

        self.file_out.write('<subroutineDec>\n')

        #('constructor' | 'function' | 'method')
        self.compile()
        self.tokenizer.advance()

        #('void' | 'type' | className)
        if self.tokenizer.current_token == 'void':
            self.compile()
            self.tokenizer.advance()
        elif (self.tokenizer.current_token in self.type) or (self.tokenizer.tokenType() == 'identifier'):
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected 'void', 'int', 'char' or 'boolean' " + f"instead found: '{self.tokenizer.current_token}'")
        
        
        #subroutineName
        if self.tokenizer.tokenType() == 'identifier':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected identifier " + f"instead found: '{self.tokenizer.current_token}'")
        
        #'('
        if self.tokenizer.current_token == '(':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected '('" + f"instead found: '{self.tokenizer.current_token}'")
        
        # parameterList
        self.compileParameterList() #Does not need tokenizer.advance() after.

        #')'
        if self.tokenizer.current_token == ')':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # subroutineBody
        if self.tokenizer.current_token == '{':
            self.compileSubroutineBody()
        else:
            raise Exception("Expected '{' " + f"instead found: '{self.tokenizer.current_token}'")
        
        self.file_out.write('</subroutineDec>\n')

        
    def compileSubroutineBody(self):
        
        self.file_out.write('<subroutineBody>\n')

        # '{'
        self.compile()
        self.tokenizer.advance()

        # varDec*
        while self.tokenizer.current_token == 'var':
            self.varDec()
            self.tokenizer.advance()

        # statements
        self.compileStatements()
        self.tokenizer.advance()

        # '}'
        if self.tokenizer.current_token == '}':
            self.compile()
        else:
            raise Exception("Expected '}' " + f"instead found: '{self.tokenizer.current_token}'")

        self.file_out.write('</subroutineBody>\n')

    def compileStatements(self):
        self.file_out.write('<statements>\n')

        while(self.tokenizer.current_token in self.statements):
            self.compileStatement()
            self.tokenizer.advance()
        
        self.tokenizer.counter -= 1

        self.file_out.write('</statements>\n')

    def compileStatement(self):

        if self.tokenizer.current_token == 'let':
            self.compileLet()
        elif self.tokenizer.current_token == 'if':
            self.compileIf()
        elif self.tokenizer.current_token == 'while':
            self.compileWhile()
        elif self.tokenizer.current_token == 'do':
            self.compileDo()
        elif self.tokenizer.current_token == 'return':
            self.compileReturn()

    def compileLet(self):
        # 'let' varName('[' expression ']')? '=' expression ';'
        self.file_out.write('<letStatement>\n')
        
        # 'let'
        self.compile()
        self.tokenizer.advance()

        # varName
        if self.tokenizer.tokenType() == 'identifier':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")
        
        
        # ('[' expression ']')?
        if self.tokenizer.current_token == '[':
            # '['
            self.compile()
            self.tokenizer.advance()
            
            # expression
            self.compileExpression()
            self.tokenizer.advance()

            # ']'
            if self.tokenizer.current_token == ']':
                self.compile()
                self.tokenizer.advance()
            else:
                raise Exception("Expected ']' " + f"instead found: '{self.tokenizer.current_token}'")
        
        if self.tokenizer.current_token == '=':
                self.compile()
                self.tokenizer.advance()
        else:
            raise Exception("Expected '=' " + f"instead found: '{self.tokenizer.current_token}'")
        
        
        # expression
        self.compileExpression()
        self.tokenizer.advance()

        # ';'
        if self.tokenizer.current_token == ';':
                self.compile()

        else:
            raise Exception("Expected ';' " + f"instead found: '{self.tokenizer.current_token}'")
        
        self.file_out.write('</letStatement>\n')
    
    def compileIf(self):
        # 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
        self.file_out.write('<ifStatement>\n')
        # 'if' '(' expression ')' '{' statements '}'
        # 'if'
        self.compile()
        self.tokenizer.advance()

        # '('
        if self.tokenizer.current_token == '(':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected '(' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # expression
        self.compileExpression()
        self.tokenizer.advance()

        #')'
        if self.tokenizer.current_token == ')':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # '{'
        if self.tokenizer.current_token == '{':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected '{' " + f"instead found: '{self.tokenizer.current_token}'")

        # statements
        self.compileStatements()
        self.tokenizer.advance()

        # '}'
        if self.tokenizer.current_token == '}':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected '}' " + f"instead found: '{self.tokenizer.current_token}'")
        

        # ('else' '{' statements '}')?
        if self.tokenizer.current_token == 'else':
            #else
            self.compile()
            self.tokenizer.advance()

            # '{'
            if self.tokenizer.current_token == '{':
                self.compile()
                self.tokenizer.advance()
            else:
                raise Exception("Expected '{' " + f"instead found: '{self.tokenizer.current_token}'")

            # statements
            self.compileStatements()
            self.tokenizer.advance()

            # '}'
            if self.tokenizer.current_token == '}':
                self.compile()
            else:
                raise Exception("Expected '}' " + f"instead found: '{self.tokenizer.current_token}'")
        
        #If there is no else statement
        else:
            self.tokenizer.counter -= 1

        self.file_out.write('</ifStatement>\n')
    
    def compileWhile(self):
        # 'while' '(' expression ')' '{' statements '}'
        self.file_out.write('<whileStatement>\n')

        # 'while'
        self.compile()
        self.tokenizer.advance()

        # '('
        if self.tokenizer.current_token == '(':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected '(' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # expression
        self.compileExpression()
        self.tokenizer.advance()

        #')'
        if self.tokenizer.current_token == ')':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")
        
        # '{'
        if self.tokenizer.current_token == '{':
            self.compile()
            self.tokenizer.advance()
        else:
            raise Exception("Expected '{' " + f"instead found: '{self.tokenizer.current_token}'")

        # statements
        self.compileStatements()
        self.tokenizer.advance()

        # '}'
        if self.tokenizer.current_token == '}':
            self.compile()
        else:
            raise Exception("Expected '}' " + f"instead found: '{self.tokenizer.current_token}'")

        self.file_out.write('</whileStatement>\n')
    
    def compileDo(self):
        # 'do' subroutineCall ';'
        self.file_out.write('<doStatement>\n')

        # 'do'
        self.compile()
        self.tokenizer.advance()

        # subroutineCall
        # subroutineName '(' expressionList ')' | 
        # (className | varName)'.'subroutineName'(' expressionList ')'
        if self.tokenizer.tokenType() == 'identifier':
                
            # subroutineName | (className | varName)
            self.compile()
            self.tokenizer.advance()
                
                    
            #subroutineName '(' expressionList ')' 
            if self.tokenizer.current_token == '(':
                # '('
                self.compile()
                self.tokenizer.advance()

                # expressionList
                self.compileExpressionList()
                self.tokenizer.advance()

                # ')'
                if self.tokenizer.current_token == ')':
                    self.compile()
                else:
                   raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")
                
            # (className | varName)'.'subroutineName'(' expressionList ')'
            elif self.tokenizer.current_token == '.':
                # '.'
                self.compile()
                self.tokenizer.advance()
                    
                # subroutineName
                if self.tokenizer.tokenType() == 'identifier':
                    self.compile()
                    self.tokenizer.advance()
                else:
                   raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")
                
                # '('
                if self.tokenizer.current_token == '(':
                    self.compile()
                    self.tokenizer.advance()
                else:
                   raise Exception("Expected '(' " + f"instead found: '{self.tokenizer.current_token}'")

                # expressionList
                self.compileExpressionList()
                self.tokenizer.advance()

                # ')'
                if self.tokenizer.current_token == ')':
                    self.compile()
                else:
                   raise Exception("Expected ')' " + f"instead found: '{self.tokenizer.current_token}'")

        self.tokenizer.advance()

        # ';'
        if self.tokenizer.current_token == ';':
            self.compile()
    
        else:
            raise Exception("Expected ';' " + f"instead found: '{self.tokenizer.current_token}'")

        self.file_out.write('</doStatement>\n')

    def compileReturn(self):
        self.file_out.write('<returnStatement>\n')

        # 'return'
        self.compile()
        self.tokenizer.advance()

        # expression
        if self.tokenizer.current_token != ';':
            self.compileExpression()
            self.tokenizer.advance()
        
        # ';'
        if self.tokenizer.current_token == ';':
            self.compile()
           
        else:
            raise Exception("Expected ';' " + f"instead found: '{self.tokenizer.current_token}'")    

        self.file_out.write('</returnStatement>\n')

    def compileExpressionList(self):
        #(expression(',' expression)*)?
        self.file_out.write('<expressionList>\n')

        #(expression(',' expression)*)?
        if self.tokenizer.tokenType() in ['int_const', 'string_const', 'identifier'] or self.tokenizer.current_token in ['true', 'false', 'null', 'this', '(']:
            # expression
            
            self.compileExpression()
            self.tokenizer.advance()

            # (',' expression)*
            while self.tokenizer.current_token == ',':
                # ','
                self.compile()
                self.tokenizer.advance()

                # expression
                self.compileExpression()
                self.tokenizer.advance()
            
            #Atrasando o contador em
        
        self.tokenizer.counter -= 1

        self.file_out.write('</expressionList>\n')

    def compileExpression(self):
        # term (op term)*
        self.file_out.write('<expression>\n')

        # term
        self.compileTerm()
        self.tokenizer.advance()

        # (op term)*
        while self.tokenizer.current_token in self.op:
            # op
            self.compile()
            self.tokenizer.advance()

            # term
            self.compileTerm()
            self.tokenizer.advance()

        #Andando com o contador para trás
        self.tokenizer.counter -= 1
        
        self.file_out.write('</expression>\n')

    def compileParameterList(self):
        self.file_out.write('<parameterList>\n')
        
        if self.tokenizer.current_token in self.type:
            # type
            self.compile()
            self.tokenizer.advance()

            # varName
            if self.tokenizer.tokenType() == 'identifier':
                self.compile()
                self.tokenizer.advance()
            else:
                raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")

            #(',' type varName)*
            while (self.tokenizer.current_token == ','):
                # ','
                self.compile()
                self.tokenizer.advance()
                
                # type
                if self.tokenizer.current_token in self.type:
                    self.compile()
                    self.tokenizer.advance()
                else: 
                    raise Exception("Expected 'void', 'int', 'char' or 'boolean' " + f"instead found: '{self.tokenizer.current_token}'")
        
                # varName
                if self.tokenizer.tokenType() == 'identifier':
                    self.compile()
                    self.tokenizer.advance()
                else:
                    raise Exception("Expected an identifier " + f"instead found: '{self.tokenizer.current_token}'")

        self.file_out.write('</parameterList>\n')

    def Close (self):
        '''Closes the output file.'''

        self.file_out.close()

def main ():
    file_dir = input('Please, insert the file name:')

    if file_dir[-1] == '/': #Verifying if the input is a file or a folder
        os.chdir(file_dir)
        files = glob.glob("*.jack")

    else:
        files = [file_dir]
   

    for file in files:
        tokenizer = JackTokenizer(file)
        code_writer = JackEngine(file.split('.')[-2] + '.xml', tokenizer)

        while (tokenizer.hasMoreTokens() == True):
            tokenizer.advance()
            current_token = tokenizer.current_token
            
            if current_token == 'class':  
                code_writer.compileClass()

        code_writer.Close()

if __name__ == "__main__":
    main()