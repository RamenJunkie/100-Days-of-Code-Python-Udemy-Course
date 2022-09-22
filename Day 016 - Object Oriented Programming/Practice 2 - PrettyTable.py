from prettytable import PrettyTable

table = PrettyTable([])
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander","Bulbasaur"])
table.add_column("Type",["Electric","Water","Fire","Grass"])
table.align = "l"

print(table)