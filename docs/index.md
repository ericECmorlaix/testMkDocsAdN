---
hide:
  - navigation
  - toc
---
Ceci est un tutoriel pour déployer un site web depuis un dépôt git
 avec le framework material pour mkdocs en incluant, ou pas, des notebook jupyter...

 [Chap_01](./Chap_01)

 [Chap_01](/Chap_01)

[Chap_01](Chap_01)

![building_websites](images/undraw_building_websites_i78t.svg){: align=right width=50%}


???+ adn "Créer, déployer puis maintenir son site :"

    1.  ;

    2.  ;

    3.  ;



???+ adncode "Coder pour générer ses pages web  :"

    1. ;

???+ adncogs "Coder pour générer ses pages web  :"

    1.  ;


![Bienvenue](images/undraw_handcrafts_welcome.svg "Degemer Mat !"){width=25% .center }

=== "chemin relatif à la page"
    ```md
    ![Illustration d'une photo instantané](./images/undraw_Polaroid.svg "image via URL relative")
    ```
    ![Illustration d'une photo instantané](./images/undraw_Polaroid.svg "image via URL relative")

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








