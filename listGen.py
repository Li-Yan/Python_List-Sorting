from random import uniform
import sys

if (len(sys.argv) > 1):
	size = int(sys.argv[1])
else:
	size = 100

r = 10

for i in range(0, size - 1):
	sys.stdout.write('{0} '.format(int(r * uniform(0, 1)) - r / 2))
sys.stdout.write('{0}\n'.format(int(r * uniform(0, 1)) - r / 2))