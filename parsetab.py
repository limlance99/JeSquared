
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightNOTleftANDORleftEQNEQLSSGTRLEQGEQleftPLUSMINUSleftMULTIPLYDIVIDEleftEXPAND CLOSECURL CLOSEPAR COMMA DIVIDE ELSE EOL EQ EQUALS EXP FLOAT FOR GEQ GTR IF INPUT INT LEQ LSS MAINCOMMENT MINUS MULTIPLY NAME NEQ NOT OPENCURL OPENPAR OR OUTPUT PERCENTFLOAT PERCENTINT PLUS QUOTEMARK RETURN STRING THEN TO TYPEFLOAT TYPEINT TYPESTRING WHILE\n    code : vardeclare EOL \n        | io EOL\n        | expression EOL\n        | while \n        | if\n        | empty\n    \n    io : inputoutput OPENPAR iodata CLOSEPAR\n    io : inputoutput error \n    inputoutput : INPUT\n                | OUTPUT\n    \n    iodata : QUOTEMARK percenttype QUOTEMARK COMMA AND NAME\n    \n    percenttype : PERCENTFLOAT\n                | PERCENTINT\n    \n    datatype : TYPEFLOAT\n             | TYPEINT\n    \n    bool : expression boolop expression\n         | bool boolop bool\n         | expression boolop bool\n         | bool boolop expression\n    \n    boolop : EQ\n           | NEQ\n           | LSS\n           | GTR\n           | LEQ\n           | GEQ\n           | AND\n           | OR\n    \n    if : IF OPENPAR bool CLOSEPAR block else\n       | IF OPENPAR bool CLOSEPAR block \n    \n    else : ELSE block\n    \n    while : WHILE OPENPAR bool CLOSEPAR block\n\n    \n    block : OPENCURL while CLOSECURL\n        |   OPENCURL if CLOSECURL\n        |   OPENCURL bcode CLOSECURL\n    \n    bcode : io EOL\n        | expression EOL\n        | empty\n    \n    expression :  expression EXP expression\n               |  expression  MULTIPLY expression\n               |  expression DIVIDE expression\n               |  expression PLUS expression\n               |  expression MINUS expression\n               |  OPENPAR expression CLOSEPAR\n    \n    oper :  EXP\n         |  MULTIPLY\n         |  DIVIDE\n         |  PLUS\n         |  MINUS\n         |  EQUALS \n    \n    vardeclare : datatype NAME\n    \n    expression : NAME EQUALS expression\n               | NAME EQUALS NAME\n    \n    expression  : INT\n                | FLOAT\n    \n    empty : \n    '
    
_lr_action_items = {'OPENPAR':([0,10,11,14,15,18,19,23,24,25,26,27,29,33,34,53,54,55,56,57,58,59,60,61,62,66,],[11,30,11,33,34,-9,-10,11,11,11,11,11,11,11,11,11,-20,-21,-22,-23,-24,-25,-26,-27,11,11,]),'NAME':([0,8,11,16,17,23,24,25,26,27,29,33,34,53,54,55,56,57,58,59,60,61,62,66,81,],[9,28,9,-14,-15,9,9,9,9,9,40,9,9,9,-20,-21,-22,-23,-24,-25,-26,-27,9,9,88,]),'INT':([0,11,23,24,25,26,27,29,33,34,53,54,55,56,57,58,59,60,61,62,66,],[12,12,12,12,12,12,12,12,12,12,12,-20,-21,-22,-23,-24,-25,-26,-27,12,12,]),'FLOAT':([0,11,23,24,25,26,27,29,33,34,53,54,55,56,57,58,59,60,61,62,66,],[13,13,13,13,13,13,13,13,13,13,13,-20,-21,-22,-23,-24,-25,-26,-27,13,13,]),'WHILE':([0,66,],[14,14,]),'IF':([0,66,],[15,15,]),'$end':([0,1,5,6,7,20,21,22,65,71,79,82,83,84,87,],[-55,0,-4,-5,-6,-1,-2,-3,-31,-29,-28,-32,-33,-34,-30,]),'TYPEFLOAT':([0,],[16,]),'TYPEINT':([0,],[17,]),'INPUT':([0,66,],[18,18,]),'OUTPUT':([0,66,],[19,19,]),'EOL':([2,3,4,12,13,28,31,35,36,37,38,39,40,41,44,48,76,77,],[20,21,22,-53,-54,-50,-8,-38,-39,-40,-41,-42,-52,-51,-43,-7,85,86,]),'EXP':([4,12,13,32,35,36,37,38,39,40,41,44,46,68,69,77,],[23,-53,-54,23,-38,23,23,23,23,-52,23,-43,23,23,23,23,]),'MULTIPLY':([4,12,13,32,35,36,37,38,39,40,41,44,46,68,69,77,],[24,-53,-54,24,-38,-39,-40,24,24,-52,24,-43,24,24,24,24,]),'DIVIDE':([4,12,13,32,35,36,37,38,39,40,41,44,46,68,69,77,],[25,-53,-54,25,-38,-39,-40,25,25,-52,25,-43,25,25,25,25,]),'PLUS':([4,12,13,32,35,36,37,38,39,40,41,44,46,68,69,77,],[26,-53,-54,26,-38,-39,-40,-41,-42,-52,26,-43,26,26,26,26,]),'MINUS':([4,12,13,32,35,36,37,38,39,40,41,44,46,68,69,77,],[27,-53,-54,27,-38,-39,-40,-41,-42,-52,27,-43,27,27,27,27,]),'EQUALS':([9,40,],[29,29,]),'error':([10,18,19,],[31,-9,-10,]),'CLOSEPAR':([12,13,32,35,36,37,38,39,40,41,42,44,45,47,67,68,69,70,88,],[-53,-54,44,-38,-39,-40,-41,-42,-52,-51,48,-43,52,63,-17,-19,-16,-18,-11,]),'EQ':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,54,54,54,54,54,54,54,]),'NEQ':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,55,55,55,55,55,55,55,]),'LSS':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,56,56,56,56,56,56,56,]),'GTR':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,57,57,57,57,57,57,57,]),'LEQ':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,58,58,58,58,58,58,58,]),'GEQ':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,59,59,59,59,59,59,59,]),'AND':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,72,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,60,60,60,60,60,60,60,81,]),'OR':([12,13,35,36,37,38,39,40,41,44,45,46,47,67,68,69,70,],[-53,-54,-38,-39,-40,-41,-42,-52,-51,-43,61,61,61,61,61,61,61,]),'QUOTEMARK':([30,49,50,51,],[43,64,-12,-13,]),'PERCENTFLOAT':([43,],[50,]),'PERCENTINT':([43,],[51,]),'OPENCURL':([52,63,80,],[66,66,66,]),'COMMA':([64,],[72,]),'CLOSECURL':([65,66,71,73,74,75,78,79,82,83,84,85,86,87,],[-31,-55,-29,82,83,84,-37,-28,-32,-33,-34,-35,-36,-30,]),'ELSE':([71,82,83,84,],[80,-32,-33,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,],[1,]),'vardeclare':([0,],[2,]),'io':([0,66,],[3,76,]),'expression':([0,11,23,24,25,26,27,29,33,34,53,62,66,],[4,32,35,36,37,38,39,41,46,46,68,69,77,]),'while':([0,66,],[5,73,]),'if':([0,66,],[6,74,]),'empty':([0,66,],[7,78,]),'datatype':([0,],[8,]),'inputoutput':([0,66,],[10,10,]),'iodata':([30,],[42,]),'bool':([33,34,53,62,],[45,47,67,70,]),'percenttype':([43,],[49,]),'boolop':([45,46,47,67,68,69,70,],[53,62,53,53,62,62,53,]),'block':([52,63,80,],[65,71,87,]),'bcode':([66,],[75,]),'else':([71,],[79,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> vardeclare EOL','code',2,'p_code','parse.py',160),
  ('code -> io EOL','code',2,'p_code','parse.py',161),
  ('code -> expression EOL','code',2,'p_code','parse.py',162),
  ('code -> while','code',1,'p_code','parse.py',163),
  ('code -> if','code',1,'p_code','parse.py',164),
  ('code -> empty','code',1,'p_code','parse.py',165),
  ('io -> inputoutput OPENPAR iodata CLOSEPAR','io',4,'p_io','parse.py',172),
  ('io -> inputoutput error','io',2,'p_io_error','parse.py',176),
  ('inputoutput -> INPUT','inputoutput',1,'p_inputoutput','parse.py',180),
  ('inputoutput -> OUTPUT','inputoutput',1,'p_inputoutput','parse.py',181),
  ('iodata -> QUOTEMARK percenttype QUOTEMARK COMMA AND NAME','iodata',6,'p_iodata','parse.py',186),
  ('percenttype -> PERCENTFLOAT','percenttype',1,'p_percenttype','parse.py',191),
  ('percenttype -> PERCENTINT','percenttype',1,'p_percenttype','parse.py',192),
  ('datatype -> TYPEFLOAT','datatype',1,'p_datatype','parse.py',197),
  ('datatype -> TYPEINT','datatype',1,'p_datatype','parse.py',198),
  ('bool -> expression boolop expression','bool',3,'p_bool','parse.py',204),
  ('bool -> bool boolop bool','bool',3,'p_bool','parse.py',205),
  ('bool -> expression boolop bool','bool',3,'p_bool','parse.py',206),
  ('bool -> bool boolop expression','bool',3,'p_bool','parse.py',207),
  ('boolop -> EQ','boolop',1,'p_boolop','parse.py',213),
  ('boolop -> NEQ','boolop',1,'p_boolop','parse.py',214),
  ('boolop -> LSS','boolop',1,'p_boolop','parse.py',215),
  ('boolop -> GTR','boolop',1,'p_boolop','parse.py',216),
  ('boolop -> LEQ','boolop',1,'p_boolop','parse.py',217),
  ('boolop -> GEQ','boolop',1,'p_boolop','parse.py',218),
  ('boolop -> AND','boolop',1,'p_boolop','parse.py',219),
  ('boolop -> OR','boolop',1,'p_boolop','parse.py',220),
  ('if -> IF OPENPAR bool CLOSEPAR block else','if',6,'p_if','parse.py',225),
  ('if -> IF OPENPAR bool CLOSEPAR block','if',5,'p_if','parse.py',226),
  ('else -> ELSE block','else',2,'p_else','parse.py',235),
  ('while -> WHILE OPENPAR bool CLOSEPAR block','while',5,'p_while','parse.py',241),
  ('block -> OPENCURL while CLOSECURL','block',3,'p_block','parse.py',248),
  ('block -> OPENCURL if CLOSECURL','block',3,'p_block','parse.py',249),
  ('block -> OPENCURL bcode CLOSECURL','block',3,'p_block','parse.py',250),
  ('bcode -> io EOL','bcode',2,'p_bcode','parse.py',256),
  ('bcode -> expression EOL','bcode',2,'p_bcode','parse.py',257),
  ('bcode -> empty','bcode',1,'p_bcode','parse.py',258),
  ('expression -> expression EXP expression','expression',3,'p_expression_math','parse.py',266),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_math','parse.py',267),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_math','parse.py',268),
  ('expression -> expression PLUS expression','expression',3,'p_expression_math','parse.py',269),
  ('expression -> expression MINUS expression','expression',3,'p_expression_math','parse.py',270),
  ('expression -> OPENPAR expression CLOSEPAR','expression',3,'p_expression_math','parse.py',271),
  ('oper -> EXP','oper',1,'p_oper','parse.py',277),
  ('oper -> MULTIPLY','oper',1,'p_oper','parse.py',278),
  ('oper -> DIVIDE','oper',1,'p_oper','parse.py',279),
  ('oper -> PLUS','oper',1,'p_oper','parse.py',280),
  ('oper -> MINUS','oper',1,'p_oper','parse.py',281),
  ('oper -> EQUALS','oper',1,'p_oper','parse.py',282),
  ('vardeclare -> datatype NAME','vardeclare',2,'p_vardeclare','parse.py',287),
  ('expression -> NAME EQUALS expression','expression',3,'p_expression_var_assign','parse.py',294),
  ('expression -> NAME EQUALS NAME','expression',3,'p_expression_var_assign','parse.py',295),
  ('expression -> INT','expression',1,'p_expression_int_float','parse.py',312),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','parse.py',313),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',318),
]
