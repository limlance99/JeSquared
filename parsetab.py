
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightNOTleftANDORleftEQNEQLSSGTRLEQGEQleftPLUSMINUSleftMULTIPLYDIVIDEleftMODULOleftEXPAMP AND BREAK CLOSECURL CLOSEPAR COMMA COMMENT DIVIDE ELSE EOL EQ EQUALS EXP FLOAT FNAME GEQ GTR IF INPUT INT LEQ LSS MINUS MODULO MULTIPLY NAME NEQ NEWLINE NOT OPENCURL OPENPAR OR OUTPUT PERCENTFLOAT PERCENTINT PLUS QUOTEMARK RETURN TYPEFLOAT TYPEINT WHILE\n    begin : function\n    \n    function : function funcname OPENCURL code return EOL CLOSECURL\n             | empty\n    \n    funcname : datatype FNAME OPENPAR parameters CLOSEPAR \n    \n    parameters : vardeclare COMMA parameters\n                | vardeclare\n                | empty\n    \n    code : code vardeclare EOL \n        | code varassign EOL\n        | code io EOL\n        | code expression EOL\n        | code while \n        | code if\n        | code return EOL\n        | empty\n    \n    return : RETURN expression\n    \n    io : INPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA AMP NAME CLOSEPAR\n        | OUTPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA NAME CLOSEPAR\n    \n    percenttype : PERCENTFLOAT\n                | PERCENTINT\n    \n    datatype : TYPEFLOAT\n             | TYPEINT\n    \n    bool : expression boolop expression\n         | bool boolop bool\n         | expression boolop bool\n         | bool boolop expression\n         | NOT bool\n         | OPENPAR bool CLOSEPAR\n    \n    boolop : EQ\n           | NEQ\n           | LSS\n           | GTR\n           | LEQ\n           | GEQ\n           | AND\n           | OR\n    \n    if : IF OPENPAR bool CLOSEPAR block else\n       | IF OPENPAR bool CLOSEPAR block \n    \n    else : ELSE block\n    \n    while : WHILE OPENPAR bool CLOSEPAR block\n\n    \n    block : OPENCURL bcode CLOSECURL\n    \n    bcode : bcode io EOL\n        | bcode varassign EOL\n        | bcode while\n        | bcode if\n        | bcode expression EOL\n        | bcode BREAK EOL\n        | bcode return EOL\n        | empty\n    \n    expression :  expression oper expression\n               |  OPENPAR expression CLOSEPAR\n    \n    oper :  EXP\n        | MODULO\n         |  MULTIPLY\n         |  DIVIDE\n         |  PLUS\n         |  MINUS\n         |  EQUALS \n    \n    vardeclare : datatype NAME\n    \n    varassign : NAME EQUALS expression\n    \n    varname : NAME COMMA varname\n            | NAME\n            | empty\n    \n    expression  : INT\n                | FLOAT\n                | NAME\n    \n    expression : FNAME OPENPAR varname CLOSEPAR \n    \n    empty : \n    '
    
_lr_action_items = {'TYPEFLOAT':([0,2,3,8,10,11,12,18,19,34,35,36,37,38,58,59,99,106,112,116,124,],[-68,6,-3,-68,6,-15,6,-12,-13,-14,-8,-9,-10,-11,6,-2,-40,-38,-37,-41,-39,]),'TYPEINT':([0,2,3,8,10,11,12,18,19,34,35,36,37,38,58,59,99,106,112,116,124,],[-68,7,-3,-68,7,-15,7,-12,-13,-14,-8,-9,-10,-11,7,-2,-40,-38,-37,-41,-39,]),'$end':([0,1,2,3,59,],[-68,0,-1,-3,-2,]),'OPENCURL':([4,57,82,94,113,],[8,-4,100,100,100,]),'FNAME':([5,6,7,8,10,11,18,19,20,24,34,35,36,37,38,39,40,41,42,43,44,45,46,50,55,56,68,71,83,84,85,86,87,88,89,90,91,92,99,100,105,106,109,110,112,116,119,120,124,127,128,129,130,131,],[9,-21,-22,-68,28,-15,-12,-13,28,28,-14,-8,-9,-10,-11,28,-52,-53,-54,-55,-56,-57,-58,28,28,28,28,28,28,-29,-30,-31,-32,-33,-34,-35,-36,28,-40,-68,28,-38,28,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'NAME':([6,7,8,10,11,18,19,20,21,24,34,35,36,37,38,39,40,41,42,43,44,45,46,50,54,55,56,68,71,79,83,84,85,86,87,88,89,90,91,92,99,100,105,106,108,109,110,112,114,116,119,120,124,127,128,129,130,131,],[-21,-22,-68,22,-15,-12,-13,48,49,48,-14,-8,-9,-10,-11,48,-52,-53,-54,-55,-56,-57,-58,48,66,48,48,48,48,66,48,-29,-30,-31,-32,-33,-34,-35,-36,48,-40,-68,48,-38,115,22,-49,-37,125,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'RETURN':([8,10,11,18,19,34,35,36,37,38,99,100,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,20,-15,-12,-13,-14,-8,-9,-10,-11,-40,-68,-38,20,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'INPUT':([8,10,11,18,19,34,35,36,37,38,99,100,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,23,-15,-12,-13,-14,-8,-9,-10,-11,-40,-68,-38,23,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'OUTPUT':([8,10,11,18,19,34,35,36,37,38,99,100,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,25,-15,-12,-13,-14,-8,-9,-10,-11,-40,-68,-38,25,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'OPENPAR':([8,9,10,11,18,19,20,23,24,25,28,29,30,34,35,36,37,38,39,40,41,42,43,44,45,46,50,55,56,68,71,83,84,85,86,87,88,89,90,91,92,99,100,105,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,12,24,-15,-12,-13,24,51,24,53,54,55,56,-14,-8,-9,-10,-11,24,-52,-53,-54,-55,-56,-57,-58,24,68,68,68,68,68,-29,-30,-31,-32,-33,-34,-35,-36,105,-40,-68,105,-38,24,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'INT':([8,10,11,18,19,20,24,34,35,36,37,38,39,40,41,42,43,44,45,46,50,55,56,68,71,83,84,85,86,87,88,89,90,91,92,99,100,105,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,26,-15,-12,-13,26,26,-14,-8,-9,-10,-11,26,-52,-53,-54,-55,-56,-57,-58,26,26,26,26,26,26,-29,-30,-31,-32,-33,-34,-35,-36,26,-40,-68,26,-38,26,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'FLOAT':([8,10,11,18,19,20,24,34,35,36,37,38,39,40,41,42,43,44,45,46,50,55,56,68,71,83,84,85,86,87,88,89,90,91,92,99,100,105,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,27,-15,-12,-13,27,27,-14,-8,-9,-10,-11,27,-52,-53,-54,-55,-56,-57,-58,27,27,27,27,27,27,-29,-30,-31,-32,-33,-34,-35,-36,27,-40,-68,27,-38,27,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'WHILE':([8,10,11,18,19,34,35,36,37,38,99,100,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,29,-15,-12,-13,-14,-8,-9,-10,-11,-40,-68,-38,29,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'IF':([8,10,11,18,19,34,35,36,37,38,99,100,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-68,30,-15,-12,-13,-14,-8,-9,-10,-11,-40,-68,-38,30,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'CLOSEPAR':([12,26,27,31,32,33,48,49,52,54,58,60,63,65,66,67,69,72,73,78,79,80,81,93,97,98,101,102,103,104,111,115,125,],[-68,-64,-65,57,-6,-7,-66,-59,63,-68,-68,-50,-51,78,-62,-63,82,94,-5,-67,-68,98,63,-27,-61,-28,-24,-26,-23,-25,63,126,132,]),'EOL':([13,14,15,16,17,22,26,27,47,48,49,60,61,63,78,117,118,121,122,123,126,132,],[34,35,36,37,38,-66,-64,-65,-16,-66,-59,-50,-60,-51,-67,127,128,129,130,131,-18,-17,]),'EXP':([17,22,26,27,47,48,52,60,61,63,70,78,81,102,103,111,121,],[40,-66,-64,-65,40,-66,40,40,40,-51,40,-67,40,40,40,40,40,]),'MODULO':([17,22,26,27,47,48,52,60,61,63,70,78,81,102,103,111,121,],[41,-66,-64,-65,41,-66,41,41,41,-51,41,-67,41,41,41,41,41,]),'MULTIPLY':([17,22,26,27,47,48,52,60,61,63,70,78,81,102,103,111,121,],[42,-66,-64,-65,42,-66,42,42,42,-51,42,-67,42,42,42,42,42,]),'DIVIDE':([17,22,26,27,47,48,52,60,61,63,70,78,81,102,103,111,121,],[43,-66,-64,-65,43,-66,43,43,43,-51,43,-67,43,43,43,43,43,]),'PLUS':([17,22,26,27,47,48,52,60,61,63,70,78,81,102,103,111,121,],[44,-66,-64,-65,44,-66,44,44,44,-51,44,-67,44,44,44,44,44,]),'MINUS':([17,22,26,27,47,48,52,60,61,63,70,78,81,102,103,111,121,],[45,-66,-64,-65,45,-66,45,45,45,-51,45,-67,45,45,45,45,45,]),'EQUALS':([17,22,26,27,47,48,52,60,61,63,70,78,81,102,103,111,121,],[46,50,-64,-65,46,-66,46,46,46,-51,46,-67,46,46,46,46,46,]),'EQ':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,84,84,84,-67,84,84,84,-28,84,84,84,84,84,]),'NEQ':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,85,85,85,-67,85,85,85,-28,85,85,85,85,85,]),'LSS':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,86,86,86,-67,86,86,86,-28,86,86,86,86,86,]),'GTR':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,87,87,87,-67,87,87,87,-28,87,87,87,87,87,]),'LEQ':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,88,88,88,-67,88,88,88,-28,88,88,88,88,88,]),'GEQ':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,89,89,89,-67,89,89,89,-28,89,89,89,89,89,]),'AND':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,90,90,90,-67,90,90,90,-28,90,90,90,90,90,]),'OR':([26,27,48,60,63,69,70,72,78,80,81,93,98,101,102,103,104,111,],[-64,-65,-66,-50,-51,91,91,91,-67,91,91,91,-28,91,91,91,91,91,]),'COMMA':([32,49,66,95,96,],[58,-59,79,107,108,]),'CLOSECURL':([34,99,100,106,109,110,112,116,119,120,124,127,128,129,130,131,],[59,-40,-68,-38,116,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'QUOTEMARK':([51,53,74,75,76,77,],[62,64,95,-19,-20,96,]),'NOT':([55,56,68,71,83,84,85,86,87,88,89,90,91,92,105,],[71,71,71,71,71,-29,-30,-31,-32,-33,-34,-35,-36,71,71,]),'PERCENTFLOAT':([62,64,],[75,75,]),'PERCENTINT':([62,64,],[76,76,]),'BREAK':([99,100,106,109,110,112,116,119,120,124,127,128,129,130,131,],[-40,-68,-38,122,-49,-37,-41,-44,-45,-39,-42,-43,-46,-47,-48,]),'ELSE':([106,116,],[113,-41,]),'AMP':([107,],[114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'begin':([0,],[1,]),'function':([0,],[2,]),'empty':([0,8,12,54,58,79,100,],[3,11,33,67,33,67,110,]),'funcname':([2,],[4,]),'datatype':([2,10,12,58,],[5,21,21,21,]),'code':([8,],[10,]),'return':([10,109,],[13,123,]),'vardeclare':([10,12,58,],[14,32,32,]),'varassign':([10,109,],[15,118,]),'io':([10,109,],[16,117,]),'expression':([10,20,24,39,50,55,56,68,71,83,92,105,109,],[17,47,52,60,61,70,70,81,70,102,103,111,121,]),'while':([10,109,],[18,119,]),'if':([10,109,],[19,120,]),'parameters':([12,58,],[31,73,]),'oper':([17,47,52,60,61,70,81,102,103,111,121,],[39,39,39,39,39,39,39,39,39,39,39,]),'varname':([54,79,],[65,97,]),'bool':([55,56,68,71,83,92,105,],[69,72,80,93,101,104,80,]),'percenttype':([62,64,],[74,77,]),'boolop':([69,70,72,80,81,93,101,102,103,104,111,],[83,92,83,83,92,83,83,92,92,83,92,]),'block':([82,94,113,],[99,106,124,]),'bcode':([100,],[109,]),'else':([106,],[112,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> begin","S'",1,None,None,None),
  ('begin -> function','begin',1,'p_begin','parse.py',157),
  ('function -> function funcname OPENCURL code return EOL CLOSECURL','function',7,'p_function','parse.py',165),
  ('function -> empty','function',1,'p_function','parse.py',166),
  ('funcname -> datatype FNAME OPENPAR parameters CLOSEPAR','funcname',5,'p_funcname','parse.py',179),
  ('parameters -> vardeclare COMMA parameters','parameters',3,'p_parameters','parse.py',189),
  ('parameters -> vardeclare','parameters',1,'p_parameters','parse.py',190),
  ('parameters -> empty','parameters',1,'p_parameters','parse.py',191),
  ('code -> code vardeclare EOL','code',3,'p_code','parse.py',200),
  ('code -> code varassign EOL','code',3,'p_code','parse.py',201),
  ('code -> code io EOL','code',3,'p_code','parse.py',202),
  ('code -> code expression EOL','code',3,'p_code','parse.py',203),
  ('code -> code while','code',2,'p_code','parse.py',204),
  ('code -> code if','code',2,'p_code','parse.py',205),
  ('code -> code return EOL','code',3,'p_code','parse.py',206),
  ('code -> empty','code',1,'p_code','parse.py',207),
  ('return -> RETURN expression','return',2,'p_return','parse.py',215),
  ('io -> INPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA AMP NAME CLOSEPAR','io',9,'p_io','parse.py',221),
  ('io -> OUTPUT OPENPAR QUOTEMARK percenttype QUOTEMARK COMMA NAME CLOSEPAR','io',8,'p_io','parse.py',222),
  ('percenttype -> PERCENTFLOAT','percenttype',1,'p_percenttype','parse.py',234),
  ('percenttype -> PERCENTINT','percenttype',1,'p_percenttype','parse.py',235),
  ('datatype -> TYPEFLOAT','datatype',1,'p_datatype','parse.py',240),
  ('datatype -> TYPEINT','datatype',1,'p_datatype','parse.py',241),
  ('bool -> expression boolop expression','bool',3,'p_bool','parse.py',247),
  ('bool -> bool boolop bool','bool',3,'p_bool','parse.py',248),
  ('bool -> expression boolop bool','bool',3,'p_bool','parse.py',249),
  ('bool -> bool boolop expression','bool',3,'p_bool','parse.py',250),
  ('bool -> NOT bool','bool',2,'p_bool','parse.py',251),
  ('bool -> OPENPAR bool CLOSEPAR','bool',3,'p_bool','parse.py',252),
  ('boolop -> EQ','boolop',1,'p_boolop','parse.py',261),
  ('boolop -> NEQ','boolop',1,'p_boolop','parse.py',262),
  ('boolop -> LSS','boolop',1,'p_boolop','parse.py',263),
  ('boolop -> GTR','boolop',1,'p_boolop','parse.py',264),
  ('boolop -> LEQ','boolop',1,'p_boolop','parse.py',265),
  ('boolop -> GEQ','boolop',1,'p_boolop','parse.py',266),
  ('boolop -> AND','boolop',1,'p_boolop','parse.py',267),
  ('boolop -> OR','boolop',1,'p_boolop','parse.py',268),
  ('if -> IF OPENPAR bool CLOSEPAR block else','if',6,'p_if','parse.py',273),
  ('if -> IF OPENPAR bool CLOSEPAR block','if',5,'p_if','parse.py',274),
  ('else -> ELSE block','else',2,'p_else','parse.py',283),
  ('while -> WHILE OPENPAR bool CLOSEPAR block','while',5,'p_while','parse.py',289),
  ('block -> OPENCURL bcode CLOSECURL','block',3,'p_block','parse.py',296),
  ('bcode -> bcode io EOL','bcode',3,'p_bcode','parse.py',302),
  ('bcode -> bcode varassign EOL','bcode',3,'p_bcode','parse.py',303),
  ('bcode -> bcode while','bcode',2,'p_bcode','parse.py',304),
  ('bcode -> bcode if','bcode',2,'p_bcode','parse.py',305),
  ('bcode -> bcode expression EOL','bcode',3,'p_bcode','parse.py',306),
  ('bcode -> bcode BREAK EOL','bcode',3,'p_bcode','parse.py',307),
  ('bcode -> bcode return EOL','bcode',3,'p_bcode','parse.py',308),
  ('bcode -> empty','bcode',1,'p_bcode','parse.py',309),
  ('expression -> expression oper expression','expression',3,'p_expression_math','parse.py',319),
  ('expression -> OPENPAR expression CLOSEPAR','expression',3,'p_expression_math','parse.py',320),
  ('oper -> EXP','oper',1,'p_oper','parse.py',327),
  ('oper -> MODULO','oper',1,'p_oper','parse.py',328),
  ('oper -> MULTIPLY','oper',1,'p_oper','parse.py',329),
  ('oper -> DIVIDE','oper',1,'p_oper','parse.py',330),
  ('oper -> PLUS','oper',1,'p_oper','parse.py',331),
  ('oper -> MINUS','oper',1,'p_oper','parse.py',332),
  ('oper -> EQUALS','oper',1,'p_oper','parse.py',333),
  ('vardeclare -> datatype NAME','vardeclare',2,'p_vardeclare','parse.py',339),
  ('varassign -> NAME EQUALS expression','varassign',3,'p_varassign','parse.py',348),
  ('varname -> NAME COMMA varname','varname',3,'p_varname','parse.py',357),
  ('varname -> NAME','varname',1,'p_varname','parse.py',358),
  ('varname -> empty','varname',1,'p_varname','parse.py',359),
  ('expression -> INT','expression',1,'p_expression_int_float','parse.py',377),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','parse.py',378),
  ('expression -> NAME','expression',1,'p_expression_int_float','parse.py',379),
  ('expression -> FNAME OPENPAR varname CLOSEPAR','expression',4,'p_expression_function','parse.py',385),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',391),
]
