
(% atoms %)
print aaa,
print aa'bb,
print 712,
print 2024-03-08,
print Function_call(),
print PROCEDURE_CALL(),
print ( ( aa ) ),

(% terms %)
print 7 * 9,
print 9 / 2,
print 7 * 1 * 0 * 10 * 12 * 9,
print 999 / 1 / 2 / 3 / 44,
print 7 * 99 / 10 * 12 / 3 / 0,
print ( 7 * 3 ) / ( 1 * 11 ),

(% simple_expr %)
print 7 + 9,
print 9 - 2,
print 7 + 1 + 0 + 10 + 12 + 9,
print 999 - 1 - 2 - 3 - 44,
print 7 + 99 - 10 + 12 - 3 - 0,
print ( 7 + 3 ) - ( 1 + 11 ),

(% combined %)
print 7 * 2 + 7 / 2 - 1 * 2,
print 7 * (2 + 7) / (2 - 1) * 2,

(% expression %)
print 7 = 7,
print 7 = 8,
print 7 < 10,
print 7 < 7,
print 7 * 9 = 9 / 7,
print 7 + 3 = 13 - 3,
print 7 * 2 < 7 / 2 - 1 * 2,
print 7 * (2 + 7) = (2 - 1) * 2,

print aa < 3 < 7 < 9,
print aa = bb = cc = dd,
print 7 < 3 = 9 < 4,

return 0
