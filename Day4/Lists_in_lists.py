# fructe=["Lamaie, Banana, Mar, Nectarina"]
# legume=["Cartof, varza, Leustean"]
# total=[fructe, legume]
r1 = ["0", "0", "0"]
r2 = ["0", "0", "0"]
r3 = ["0", "0", "0"]
map = [r1, r2, r3]

position = input("Choose your position: ")
col = int(position[0]) - 1
row = int(position[1]) - 1
row_selected = map[row]
row_selected[col] = "1"
print(f"{r1}\n{r2}\n{r3}")
