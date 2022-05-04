class SymbolTable ():
    def __init__(self):
        self.classTable = {'name': [], 'type': [], 'kind': [], '#': []}
        self.subroutineTable = {'name': [], 'type': [], 'kind': [], '#': []}
        self.current_scope = 'class'
        
    def startSubroutine (self):
        self.subroutineTable = {'name': [], 'type': [], 'kind': [], '#': []}
        
    def define (self, name, tipo, kind):
        '''Defines a new identifier of the given name, type, and kind and assigns 
        it a running index, STATIC and FIELD identifiers have a class scope, 
        while ARG nad VAR identifiers have subroutine scope'''

        if kind in ['STATIC', 'FIELD']:
            self.current_scope = 'class'

            self.classTable['name'].append(name)
            self.classTable['type'].append(tipo)
            self.classTable['kind'].append(kind)
            self.classTable['#'].append(self.varCount(kind))
  
        else:
            self.current_scope = 'subroutine'

            self.subroutineTable['name'].append(name)
            self.subroutineTable['type'].append(tipo)
            self.subroutineTable['kind'].append(kind)
            self.subroutineTable['#'].append(self.varCount(kind))
          
    def varCount (self, kind):
        '''Returns the number of variables of the given kind already defined in 
        the current scope.'''

        if self.current_scope == 'class':
            return self.classTable['kind'].count(kind) - 1
        else:
            return self.subroutineTable['kind'].count(kind) - 1

    def kindOf (self, identifier_name):
        '''Returns the kind of the named identifier in the current scope. If the 
        identifier is unknown in the current scope, returns NONE'''
        if self.current_scope == 'class':
            try:
                i = self.classTable['name'].index(identifier_name)
                return self.classTable['kind'][i]
            except:
                return 'NONE'
        else:
            i = self.subroutineTable['name'].index(identifier_name)
            return self.subroutineTable['kind'][i]

    def typeOf (self, identifier_name):
        '''Returns the type of the named identifier in the current scope'''
        if self.current_scope == 'class':
            i = self.classTable['name'].index(identifier_name)
            return self.classTable['type'][i]
        else:
            i = self.subroutineTable['name'].index(identifier_name)
            return self.subroutineTable['type'][i]

    def indexOf (self, identifier_name):
        '''Returns the index assigned to the named identifier'''
        if self.current_scope == 'class':
            i = self.classTable['name'].index(identifier_name)
            return self.classTable['#'][i]
        else:
            i = self.subroutineTable['name'].index(identifier_name)
            return self.subroutineTable['#'][i]