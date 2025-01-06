from enum import Enum
from typing import List

class ASTNode:
    def __init__(self): pass
    def __str__(self): pass
    def __repr__(self): return self.__str__()

class VariableAccess(ASTNode):
    def __init__(self, name: str):
        self.name = name
        
    def __str__(self):
        return f"VariableAccess({self.name})"
    
class FunctionApplication(ASTNode):
    def __init__(self, called: ASTNode, parameter: str):
        self.called = called
        self.parameter = parameter
        
    def __str__(self):
        return f"FunctionApplication({self.called}, {self.parameter})"
    
class Number(ASTNode):
    def __init__(self, value: float):
        self.value = float(value)
        
    def __str__(self):
        return str(self.value)
    
class String(ASTNode):
    def __init__(self, value: str):
        self.value = value
        
    def __str__(self):
        return self.value
    
class Boolean(ASTNode):
    def __init__(self, value: bool):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
class Unit(ASTNode):
    def __init__(self):
        pass
    
    def __str__(self):
        return "Unit"
    
class Block(ASTNode):
    def __init__(self, body: List[ASTNode]):
        self.body = body
        
    def __str__(self):
        return f"Block({self.body})"
    
class VariableDeclaration(ASTNode):
    def __init__(self, name: str, value: ASTNode, lifetime: str = "inf", public: bool = False):
        self.name = name
        self.value = value
        self.lifetime = lifetime
        self.public = public
        
    def __str__(self):
        return f"VariableDeclaration({self.name}, value={self.value}, lifetime={self.lifetime}, public={self.public})"
    
class FunctionDeclaration(ASTNode):
    def __init__(self, parameters: List[str], body: ASTNode, impure: bool = False):
        self.parameters = parameters
        self.body = body
        self.impure = impure
        
    def __str__(self):
        return f"FunctionDeclaration({self.parameters}, body={self.body}, impure={self.impure})"
    
class MatchCase(ASTNode):
    def __init__(self, condition: ASTNode, expr: ASTNode):
        self.condition = condition
        self.expr = expr
        
    def __str__(self):
        return f"MatchCase({self.condition}, {self.expr})"
    
class Match(ASTNode):
    def __init__(self, expr: ASTNode, cases: List[MatchCase], otherwise: ASTNode):
        self.expr = expr
        self.cases = cases
        self.otherwise = otherwise
        
    def __str__(self):
        return f"Match({self.expr}, cases={self.cases}, otherwise={self.otherwise})"
    
class ClassDefinition(ASTNode):
    def __init__(self, fields: List[ASTNode], inherit: str|None = None):
        self.members = fields
        self.inherit = inherit
        
    def __str__(self):
        return f"ClassDefinition({self.members}, inherit={self.inherit})"
    
class MemberAccess(ASTNode):
    def __init__(self, obj: str, member: str):
        self.obj = obj
        self.member = member
        
    def __str__(self):
        return f"MemberAccess({self.obj}, {self.member})"
    
class ClassInstancing(ASTNode):
    def __init__(self, name: str):
        self.name = name
        
    def __str__(self):
        return f"ClassInstance({self.name})"