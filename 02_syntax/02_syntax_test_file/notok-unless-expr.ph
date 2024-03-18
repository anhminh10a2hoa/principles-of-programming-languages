(% nested unless_statements are ok %)
do do aa = 24 unless 7 < 10 otherwise aa = 3 done unless 1<8 otherwise aa = 9 done,

(% one unless_expr as rlvalue: %)
wappu.year = do 24 unless wappu'year < 100 otherwise 100+400 done,

(% unless_expr is not part of expression, so it cannot be nested: %)
notwappu = do do 24 unless 7 < 10 otherwise 3 done unless 1<8 otherwise 9 done
