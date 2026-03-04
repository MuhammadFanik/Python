# NUMBERS ARE IMMUTABLE

sugar_amount = 2
print(f"Initial Sugar amount {sugar_amount}")
print(id(sugar_amount))

sugar_amount = 22
print(f"Second sugar amount {sugar_amount}")
print(id(sugar_amount))


# MUTABLE
spice_mix = {"oregano", "red chilli", "coriander powder", "chilli flakes"}
print(f"Spice mix id {id(spice_mix)}")

spice_mix.add("Ginger")
print(f"Spice mix id after adding Ginger {id(spice_mix)}")