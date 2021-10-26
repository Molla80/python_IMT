
for line in open('sss_log'):
    if line.startswith('k-eff (implicit)'):# or line.startswith('Referer'):
       print(line)
