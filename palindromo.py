n = raw_input(">")
if n.isdigit():
    d = [h for h in n]
    if d == d[::-1]:  print "El numero es capicua: %s"%(n)
    else: print "El numero no es capicua : %s"%(n)
else:
    d = [h for h in n]
    if d == d[::-1]:  print "El texto es palindromo: %s"%(n)
    else: print "El texto no es palindromo : %s"%(n)