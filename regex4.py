import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^1*(0*11+)*0*1*$/",
r"/^$/",
r"//",
r"//",
r"//",
r"//",
r"/(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*/mi",
r"//",
r"//",
r"//"]
print(myRegexLst[idx])



import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^1*(0*11+)*0*1*$/",
r"/^(?!(1*0+10)|(0*1+01))[01]*$/",
r"//",
r"//",
r"//",
r"//",
r"/(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*/mi",
r"//",
r"//",
r"//"]
print(myRegexLst[idx])

import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^(?!1*0+10)[01]*$/",
r"/^(?!0+10)(?!1+01)[01]*$/",
r"//",
r"//",
r"//",
r"//",
r"/(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*/mi",
r"//",
r"//",
r"//"]
print(myRegexLst[idx])


import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^(?!.*010)[01]*$/",
r"/^(?!(1*(0+1)0|1\20*))[01]*$/",
r"/^([01])+([01]*\w+)?$/",
r"/^0+[01]*0+$|^1+[01]*1+$|^0*$|^1*$/",
r"//",
r"//",
r"/(?=\w*a)(?=\w*e)(?=\w*i)(?=\w*o)(?=\w*u)\w*/mi",
r"//",
r"//",
r"//"]
print(myRegexLst[idx])

import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^(?!.*010)\d*$/",
r"/^(?!.*(010|101))\d*$/",
r"/^([01])(\1*[01]*\1+)*$/",
r"/(?!(\w)+\w*\1\b)\b\w+/i",
r"//",
r"//",
r"/(?!\w*([aeiou])\w*(\1))(?=.*a)(?=.*e)(?=\w*i)(?=.*o)(?=\w*u)\b\w*/i",
r"/^(00|11|(01|10)(00|11)*(01|10))*(0|(01|10)(11|00)*1)$/",
r"/^(0|1(01*0)*1)+$/",
r"/^(?!^(0|(1(01*0)*10*)+)$)[01]+$/"]
print(myRegexLst[idx])

#actual
import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^(?!.*010)\d*$/",
r"/^(?!.*(010|101))\d*$/",
r"/^([01])(\1*[01]*\1+)*$/",
r"/(?!(\w)+\w*\1\b)\b\w+/i",
r"/\b\w*((\w)\w*\2\w*(\w)\w*\3|(\w)\w*(\w)\w*\4\w*\5|(\w)\w*(\w)\w*\7\w*\6)\w*/i",
r"//",
r"/(?!\w*([aeiou])\w*(\1))(?=.*a)(?=.*e)(?=\w*i)(?=.*o)(?=\w*u)\b\w*/i",
r"/^(?!^([01]{2})*$)^1*0(1|01*0)*$/",
r"/^(0|1(01*0)*1)+$/",
r"/^(?!^(0|(1(01*0)*10*)+)$)[01]+$/"]
print(myRegexLst[idx])

#actual
import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^(?!.*010)\d*$/", #meets
r"/^(?!.*(010|101))\d*$/", #meets
r"/^([01])(\1*[01]*\1+)*$/",
r"/(?!(\w)+\w*\1\b)\b\w+/i", #meets
r"/\b\w*((\w)\w*(\2\w*(\w)\w*\4|(\w)\w*(\2\w*\5|\5\w*\2)))\w*/i",
r"/(?!(\w)+\w*\1\b)\b\w*(\w)\w*\1(?!\w*(\w)\w*\2)\w*\1\w*/i",
r"/(?!\w*([aeiou])\w*(\1))(?=.*a)(?=.*e)(?=\w*i)(?=.*o)(?=\w*u)\b\w*/i",
r"/^(?!(..)*$)1*0(1|01*0)*$/",
r"/^(0|1(01*0)*1)+$/", #meets
r"/^(?!^(0|(1(01*0)*10*)+)$)[01]+$/"]
print(myRegexLst[idx])

#actual
import sys
idx = int(sys.argv[1])-60
myRegexLst = [r"/^(?!.*010)\d*$/", #14, meets
r"/^(?!.*(010|101))\d*$/", #20, meets
r"/^(0|1)(0*1*\1)*$/", #16
r"/(?!(\w)+\w*\1\b)\b\w+/i", #21, meets
r"/\b((\w)*\w*(\2\w*(\w)\w*\4|(\w)\w*(\2\w*\5|\5\w*\2)))\w*/i", #56
r"/(?=(\w)*\w*\1\w*\1)\b((\w)(?!\w*\3)|\1)+\b/i", #42, meets
r"/(?!\w*([aeiou])\w*(\1))(?=.*a)(?=.*e)(?=\w*i)(?=.*o)(?=\w*u)\b\w*/i", #65
r"/^(?!(..)*$)(0|10*1)*$/", #21, meets
r"/^(0|1(01*0)*1)+$/", #16, meets
r"/^(?!(0|(1(01*0)*10*)+)$)[01]+$/"] #30
print(myRegexLst[idx])













