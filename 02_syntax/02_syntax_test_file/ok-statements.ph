
var var1 = 0
var var2 = + 0 - 1 * 2 / 3
var var3 = ( (3) + ( (7+3) * 10 ) )
var var4 = Call()
var var5 = Call( 3+7 )
var var6 = +Call( 3+7 )
var var7 = -Call( (3*aa) + Anothercall( ( 0*10 ) / 2 ) )
var var8 = variable'something
var var9 = var8 ' first + 2
var var10 = var9 ' first * var2'last

PROCCALL(),
PROCCALL( aa ),
PROCCALL(aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp),
PROCCALL( 7+3 ),
PROCCALL( 7*2 - 9/3 + (1 - 1+2) ),

do
  varx = Call()
unless aa
done,
do
  abc = +Call(bb)
unless  bb = 0
otherwise
  abc = -Call(bb)
done,

index = 1,
do
  PROC(),
  PROCSECOND(),
  index = index + 1
until index < 10 ,

index2 = 10,
do
  PROC(7),
  index2 = index2 - 1
until 0 < index2 , aa = 7,  (% strange location, but ok by the syntax %)

do
  aa = 1 until index2 < 3 + index2 = 3,

do
  var1 = 0,
  var2 = + 0 - 1 * 2 / 3
until 1 - (var1 = 0) ,

print  "something1" & Call(),
print  "something2" & ( ( ( 3 ) + 2 ) - 9 ) *2
