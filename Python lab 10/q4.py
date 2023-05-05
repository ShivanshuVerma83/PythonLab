import re

test_str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'

print("The original string is : " + str(test_str))

tag = "b"

reg_str = "<" + tag + ">(.*?)</" + tag + ">"
res = re.findall(reg_str, test_str)


print("The Strings extracted : " + str(res))