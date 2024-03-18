(% order of FUNCTION  and PROCEDURE  definitions can be any %)

function  Funktio{} return  list is
  3    (% mismatch in return  type, but that is not syntax error %)
end function

procedure  PROKKI{ aa[int] } is
  aa = 7
end  procedure

function  Year{ dd[date] } return  int is
  dd'year
end  function

PROKKI( 5 )
