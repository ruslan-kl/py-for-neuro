neuro = "Neuroscience (or neurobiology) is the scientific study \
of the nervous system."

# write the file
with open('neuroscience.txt', mode=___) as file:
    file.write(neuro)

neuro_cont = " It is a multidisciplinary science that combines \
physiology, anatomy, molecular biology, developmental biology, \
cytology, computer science and mathematical modeling to \
understand the fundamental and emergent properties of neurons \
and neural circuits."

# add new string to the file (append mode)
with open('neuroscience.txt', mode=___) as file:
    file.write(neuro_cont)

# read the file and save the output
with ___('___', mode=___) as ___:
    imported = ___.read()

print(imported)
