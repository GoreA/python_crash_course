bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
#Output
# specialized

bicycles.insert(4, 'honda')
bicycles.append('suzuki')

print(bicycles)
# ['trek', 'cannondale', 'redline', 'specialized', 'honda', 'suzuki']

del bicycles[0]
print(bicycles)
# ['cannondale', 'redline', 'specialized', 'honda', 'suzuki']

bicycle = bicycles.pop(3);
print(bicycle)
# honda

print(bicycles)
# ['cannondale', 'redline', 'specialized', 'suzuki']

for bicycle in bicycles:
	print(bicycle)
	print("CUCU")
# cannondale
# CUCU
# redline
# CUCU
# specialized
# CUCU
# suzuki
# CUCU

