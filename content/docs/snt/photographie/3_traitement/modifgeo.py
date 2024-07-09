from pillowSNT import*

image=ouvrir("ficellelaplusbelle.jpg")
largeur,hauteur=image.size   # affecte à largeur la largeur de l'image en pixel et à hauteur la hauteur de l'image en pixel

imageretournee=Image.new("RGB", (largeur,hauteur))  # crée une nouvelle image de même taille que image
for x in range(largeur): # boucle pour traiter toute la largeur de l'image
    for y in range(hauteur): # boucle pour traiter toute la hauteur de l'image
        imageretournee.putpixel((x,y),image.getpixel((largeur-1-x,y))) # déplacement d'un pixel de image vers la nouvelle image

afficher(imageretournee)
sauver(imageretournee,"ficellevert.jpg")



