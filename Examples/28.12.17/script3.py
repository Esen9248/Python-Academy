library = {
	'1965':{
		'novels':{
			'Duma': [
				"Three Mushketers",
				'20 Years Later',
				'Vikon',
			],
			'Fitzgerald': [
				'the great Gatsby',
			],
			'Herbert': [
				'Dune',
				'Children of Dune',
			]
		},
		'Fantasy': {
			'Tolkien': [
				'The Lord Of the Rings',
				'The Hobbit',
			  ]
		}
	  },
  '1978': {
  	'horror': {
  		'King': [
  			'Langaniers',]
  	 	}
  }
}

books1965 = library['1965']
novels = books1965['novels']
StivenKing = library['1978']['horror']['King']

print(novels['Duma'])
print(StivenKing)


print(library['1965']['novels']['Duma'])
print(library['1965']['novels'].keys())

print(len(library))
print(len(novels))

for i in novels['Duma']:
	print(i)