##for line in open("sss_log"):
 ##print(line[:-1])
data = open(("sss_log"))
line = data.readlines()
keff_in = (line[96:115])
lst = []
for i in keff_in:
    lst.append(i[34:40])
type(lst)

#output = open("sss_log", "w")
#t_fibo = (0,1)
#for n in range(20):
 #t_fibo = (t_fibo[-1], sum(t_fibo))
 #output.write("\t".join(map(lambda i: str(i), t_fibo)) + "\n")
#output.close()
