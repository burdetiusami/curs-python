# Sa se inlocuiasca in textul alocat variabilei "var_string", sirurile de caractere aferente pozitiilor
# de start si stop, cu string-urile din lista "patches"

# var_string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

# //[start, end, patch]

# patches = [[4, 14, "Conquistador"], [25, 31, "King"],[42, 49, "Pallace"]]

var_string = "The Inquisitor must meet Varric on top of Skyhold\'s battlements to be introduced."
print(var_string[4:14], var_string[25:31], var_string[42:49])

patched_string = var_string.replace('Inquisitor', 'Conquistador').replace('Varric', 'King').replace('Skyhold', 'Pallace')
print(patched_string)








