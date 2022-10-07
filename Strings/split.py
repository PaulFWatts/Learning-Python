time = "1:19:48"
hours, minutes, seconds = time.split(":")
print(hours, minutes, seconds)

graph = "A->B->C->D"
nodes = graph.split("->")
print(nodes)

langston = "Does it dry up\nlike a raisin in the sun?\n"
lines = langston.splitlines()
print(lines)

line = "Rubber duck|5|10"
item_name, the_rest = line.split("|", maxsplit=1)
print(item_name)

the_rest, amount = line.rsplit("|", maxsplit=1)
print(amount)
