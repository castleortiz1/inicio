import seaborn as sns

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Crear el gráfico
sns.scatterplot(x, y)

# Agregar título y etiquetas
plt.title("Relación entre x e y")
plt.xlabel("x")
plt.ylabel("y")

# Mostrar el gráfico
plt.show()
