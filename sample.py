from tabulate import tabulate
# from rooms import LivingSpace, Office

d = [
	{
		'Capacity': 4, 
		'Type': 'LIVINGSPACE', 
		'Name': 'Krypton'
	}, 
	{
		'Capacity': 4, 
		'Type': 'LIVINGSPACE', 
		'Name': 'Jail'
	}, 
	{
		'Capacity': 6, 
		'Type': 'OFFICE', 
		'Name': 'Krypton'
	}
]
h = (d[0].keys())
print(h)

print(tabulate(d, headers="keys"))