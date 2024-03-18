procedure PROKKI{ aa[int] } is
  aa = 7,
  do
    do
      CALL( aa )
    unless aa < 5 otherwise
      CALL( aa - 5 )
    done
  unless aa < 10 done
end procedure

procedure PROG{} return int
var bb = 10
var bc = Today()
is
  do
      return bb
  unless  bc'month < bb otherwise
    return bc'day
  done
end procedure

PROKKI( 5 ),
return (0)

