(% note that use of undefined variables are NOT part of syntax checking %)

function  Aa{} return  int is
  (7+3) / 2
end  function

function  Ta{} return  int is
    Aa( 7 )
end  function

function  Aa{} return  int is
    2011-11-17
end  function

function  Aa{} return  int is
    2022-02-22 + 10
end  function

function  Len{} return  int
  var today = Today()
is
    today'length
end  function

function  Aa{} return  int is
    (7 * 8 + 2 - 11)
end  function

function  Aa{} return  int is
    aa < bb
end  function

function  Aa{} return  int is
    do
        aa'year
    unless aa = 7 otherwise
        aa'day
    done
end  function

return 0
