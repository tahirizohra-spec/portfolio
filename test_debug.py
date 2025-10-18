import debugpy

# Lancer le serveur debug
debugpy.listen(("0.0.0.0", 5678))
print("✅ En attente de connexion VSCode...")

# Optionnel : attendre que VSCode se connecte
debugpy.wait_for_client()
print("✅ VSCode connecté !")

# Exemple simple à déboguer :
def addition(a, b):
    result = a + b
    print(f"Résultat = {result}")
    return result

x = 5
y = 7
addition(x, y)

print("Programme terminé ✅")


