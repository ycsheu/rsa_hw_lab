p = int(raw_input("Enter a p: "), 16)
q = int(raw_input("Enter a q: "), 16)
e = int(raw_input("Enter a e: "))
t = (p-1)*(q-1)
i=0
while True :
	if (1-t*i)%e == 0:
		break
	i-=1
	print i
print 'ok:' + '%d' % ((1-t*i)/e)
