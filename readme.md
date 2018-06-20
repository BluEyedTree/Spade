Example input:
["CAGAAGT", "TGACAG","GAAGT"]


Example output (the result is a tree, but here is the "pretty" print representation

Layer: 0

A
	0 	[1, 3, 4]
	1 	[2, 4]
	2 	[1, 2]
G
	0 	[2, 5]
	1 	[1, 5]
	2 	[0, 3]
T
	0 	[6]
	1 	[0]
	2 	[4]

Layer: 1

AA
	0 	[3, 4]
	1 	[4]
	2 	[2]
AG
	0 	[2, 5]
	1 	[5]
	2 	[3]
GA
	0 	[3, 4]
	1 	[2, 4]
	2 	[1, 2]
GG
	0 	[5]
	1 	[5]
	2 	[3]

Layer: 2

AAG
	0 	[5]
	1 	[5]
	2 	[3]
GAA
	0 	[4]
	1 	[4]
	2 	[2]
GAG
	0 	[5]
	1 	[5]
	2 	[3]

Layer: 3

GAAG
	0 	[5]
	1 	[5]
	2 	[3]

