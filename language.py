class Token:


    digits = "0123456789"

    Int = "INT"
    Float = "FLOAT"
    plus = "PLUS"
    minus = "MINUS"
    mul = "MUL"
    div = "DIV"
    lbracket = "LBRACKET"
    rbracket= "RBRACKET"


    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type_}:{self.value}'
        return f'{self.type}'



class Lexer:

     def __init__(self,text):
         self.text = text
         self.position = -1
         self.currentCharacter = None
         self.moveForward()


     def moveForward(self):
         self.pos += 1

         if self.position< len(self.text):

            self.currentCharacter = self.text[self.position]
         else:
             self.currentCharacter = None


     def makeTokens(self):
         tokenList =[]

         while self.currentCharacter!=None:
             if self.currentCharacter in " \t":
                 self.moveForward()
             elif self.currentCharacter in self.digits:
                 newToken = Token(self.makeNumber())
                 tokenList.append(newToken)
             elif self.currentCharacter == "+":
                 newToken = Token(self.plus)
                 tokenList.append(newToken)
                 self.moveForward()
             elif self.currentCharacter == "-":
                 newToken = Token(self.minus)
                 tokenList.append(newToken)
                 self.moveForward()
             elif self.currentCharacter == "*":
                 newToken = Token(self.mul)
                 tokenList.append(newToken)
                 self.moveForward()
             elif self.currentCharacter == "/":
                 newToken = Token(self.div)
                 tokenList.append(newToken)
                 self.moveForward()
             elif self.currentCharacter == "(":
                 newToken = Token(self.lbracket)
                 tokenList.append(newToken)
                 self.moveForward()
             elif self.currentCharacter == ")":
                 newToken = Token(self.rbracket)
                 tokenList.append(newToken)
                 self.moveForward()
         return tokenList


     def makeNumber(self):
         numberString=""
         dotCounter =0

         while self.currentCharacter != None and self.currentCharacter in self.digits or ".":
             if self.currentCharacter == ".":
                 if dotCounter==1: break
                 dotCounter += 1
                 numberString +="."
             else:
                 numberString += self.currentCharacter

         if dotCounter ==0:
             return Token(self.Int,int(numberString))
         else:
             return Token(self.Float,float(numberString))



class Error:

    def __init__(self,errorName, details):
        self.errorName = errorName
        self.details = details