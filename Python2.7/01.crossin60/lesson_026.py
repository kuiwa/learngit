I = [365, 'everyday', 0.618, True]
print I[0]
print I[1]
I[0] = 123	#change I[0] value
print I[0]
I.append(1024)
print I
del I[0]	#index
print I
print I[-1]
print I[-2]
print I[1:-1]	#slice
