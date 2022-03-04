Ceci est ma page 1

- Relatifs à la page

[Page_2](../Page_2)

[Chap_01](../)

***
- Relatifs à la racine docs/

[Page_2](/Chap_01/Page_2)

[Chap_01](/Chap_01)

***
- Relatifs à 

[Page_2](Chap_01/Page_2)

[Chap_01](Chap_01)



=== "chemin relatif à la page"
    ```md
    ![Illustration d'une photo instantané](../../images/undraw_Polaroid.svg "image via URL relative")
    ```
    ![Illustration d'une photo instantané](../../images/undraw_Polaroid.svg "image via URL relative")

=== "chemin absolu"
    ```md
    ![Illustration d'une photo instantané](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "image via URL absolue")
    ```
    ![Illustration d'une photo instantané](https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "image via URL absolue")

=== "par référence"
    ```md
    Ce qui permet d'ajouter facilement un [lien pour ouvrir cette image][polaroïd]{ target="_blank"} dans un nouvel onglet...
    
    ![polaroïd]

    <!-- Une seule et même référence pour le lien et l'image, une référence plusieurs fois réutilisable dans ce document... -->
    [polaroïd]: https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "Illustration d'une photo instantané"
    ```
    Ce qui permet d'ajouter facilement un [lien pour ouvrir cette image][polaroïd]{ target="_blank"} dans un nouvel onglet...
    
    ![polaroïd]
    
    <!-- Une seule et même référence pour le lien et l'image, une référence plusieurs fois réutilisable dans ce document... -->
    [polaroïd]: https://ericecmorlaix.github.io/adn-Tutoriel_site_web/images/undraw_Polaroid.svg "Illustration d'une photo instantané"

=== "chemin relatif à la racine"
    ```md
    ![Illustration d'une photo instantané](/images/undraw_Polaroid.svg "image via URL relative")
    ```
    ![Illustration d'une photo instantané](/images/undraw_Polaroid.svg "image via URL relative")
=== "chemin relatif à "
    ```md
    ![Illustration d'une photo instantané](images/undraw_Polaroid.svg "image via URL relative")
    ```
    ![Illustration d'une photo instantané](images/undraw_Polaroid.svg "image via URL relative")