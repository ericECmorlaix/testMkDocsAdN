# https://edenmaths.gitlab.io/ecs1/2020_21/bac_a_sable.html
# https://gitlab.com/GiYoM/ecs1/-/tree/master

#################################
#
#
#  console python
#
#
############################


def pyodide0():
    s ="<div>Code:<textarea placeholder=\"Tapez votre code ici\" id='code' class=\"txta\" ></textarea> <br> <button id='rouge' onclick='evaluatePython()'>Exécuter</button> <button id='rouge' onclick='clearOutput()'>Nettoyer</button> <button id='affiche'>Afficher/Masquer</button> </div> <br> <div>Résultat:<textarea id='output' class=\"txta common\" ></textarea> </div>"
    return s



################
#
#
#
#     MERMAID ; les arbres
#
#
######################


from typing import Optional, TypeVar, Any, List, Generic
from typing_extensions import Protocol
from abc import abstractmethod
import subprocess

# On crée un type générique d'objets comparables
# On ne peut en effet créer d'ABR qu'avec des valeurs
# comparables
C = TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    """
    Un protocole est un type abstrait dont les sous-types ont la même
    structure.
    Ici, on crée un type d'objets comparables : les objets doivent
    pouvoir être comparés avec les méthodes ==, < et >
    """
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other


class Noeud(Generic[C]):
    """
    Un noeud a une valeur et pointe vers deux autres noeuds (petit et
    grand) ou éventuellement le vide.
    On insère de nouvelles valeurs en partant de la racine du noeud et
    en bifurquant selon la comparaison avec la valeur du noeud.

    """

    def __init__(self: 'Noeud[C]', val: C) -> None:
        """
        Un noeud a toujours une valeur mais pointe vers un autre noeud
        ou éventuellement le vide (None)
        """
        self.__val: C = val
        self.__grand: Optional['Noeud[C]'] = None
        self.__petit: Optional['Noeud[C]'] = None

    def insere(self: 'Noeud[C]', val: C) -> None:
        """
        Permet d'insérer une valeur comparable dans un noeud.
        """
        if val < self.__val:
            if self.__petit:
                self.__petit.insere(val)
            else:
                self.__petit = Noeud(val)
        elif val > self.__val:
            if self.__grand:
                self.__grand.insere(val)
            else:
                self.__grand = Noeud(val)
        else:
            print(f'{val} est un doublon')

    def hauteur(self: 'Noeud[C]') -> int:
        """
        Nombre de niveaux de l'arbre
        """
        hb: int = self.__grand.hauteur() if self.__grand else 0
        hh: int = self.__petit.hauteur() if self.__petit else 0
        return 1 + max(hb, hh)

    def nb_noeuds(self: 'Noeud[C]') -> int:
        nb: int = self.__grand.nb_noeuds() if self.__grand else 0
        nh: int = self.__petit.nb_noeuds() if self.__petit else 0
        return 1 + nb + nh

    def est_feuille(self: 'Noeud[C]') -> bool:
        return not (self.__grand or self.__petit)

    def est_unaire(self: 'Noeud[C]') -> bool:
        return not ((self.__grand and self.__petit) or self.est_feuille())

    def nb_feuilles(self: 'Noeud[C]') -> int:
        if self.est_feuille():
            return 1
        elif self.__petit and not self.__grand:
            return self.__petit.nb_feuilles()
        elif self.__grand and not self.__petit:
            return self.__grand.nb_feuilles()
        elif self.__grand and self.__petit:
            return self.__grand.nb_feuilles() + self.__petit.nb_feuilles()
        else:
            return 0

    def contient(self: 'Noeud[C]', v: C, cpt=0) -> bool:
        val: C = self.__val
        if v == val:
            #print(f'En {cpt+1} comparaisons')
            return True
        elif v > val and self.__grand:
            return self.__grand.contient(v, cpt+1)
        elif v < val and self.__petit:
            return self.__petit.contient(v, cpt+1)
        else:
            #print(f'En {cpt+1} comparaisons')
            return False

    def visite_pre(self: 'Noeud[C]') -> None:
        print(self.__val)
        for cote in [self.__petit, self.__grand]:
            if cote:
                cote.visite_pre()

    def visite_post(self: 'Noeud[C]') -> None:
        for cote in [self.__petit, self.__grand]:
            if cote:
                cote.visite_post()
        print(self.__val)

    def visite_inf(self: 'Noeud[C]') -> None:
        if self.__petit:
            self.__petit.visite_inf()
        print(self.__val)
        if self.__grand:
            self.__grand.visite_inf()

    def visite_niveau(self: 'Noeud[C]') -> None:
        a_visiter: List['Noeud[C]'] = [self]
        while a_visiter != []:
            noeud: 'Noeud[C]' = a_visiter[0]
            print(noeud.__val)
            a_visiter = a_visiter[1:]
            if noeud.__petit:
                a_visiter.append(noeud.__petit)
            if noeud.__grand:
                a_visiter.append(noeud.__grand)

    def mini(self: 'Noeud[C]') -> C:
        if self.__petit is None:
            return self.__val
        else:
            return self.__petit.mini()
        
    def maxi(self: 'Noeud[C]') -> C:
        if self.__grand is None:
            return self.__val
        else:
            return self.__grand.maxi()
        
    #  Outils de représentation
    
    def tree2viz(self: 'Noeud[C]') -> str:
        """
        Utilise graphviz pour représenter l'arbre.
        Au besoin, l'installer:
          $ sudo apt-get install graphviz
        Chaque arête est représentée sous la forme:
        père -> fils;
        """
        s = ''
        v = self.__val
        if self.__petit and self.__grand:
            s += f'{self.__petit.__val}[style=filled,fillcolor=cadetblue3];\n'
            s += f'{self.__grand.__val}[style=filled,fillcolor=darkorange];\n'
            s += f'{v}->{self.__petit.__val};\n'
            s += f'{v}->{self.__grand.__val};\n'
            s += self.__petit.tree2viz()
            s += self.__grand.tree2viz()
        elif self.__petit and not self.__grand:
            s += f'{self.__petit.__val}[style=filled,fillcolor=cadetblue3];\n'
            s += f'{v}->{self.__petit.__val};\n'
            s += f'nullp{v}[shape=point];\n{v}->nullp{v};\n'
            s += self.__petit.tree2viz()
        elif self.__grand and not self.__petit:
            s += f'{self.__grand.__val}[style=filled,fillcolor=darkorange];\n'
            s += f'nullg{v}[shape=point];\n{v}->nullg{v};\n'
            s += f'{v}->{self.__grand.__val};\n'
            s += self.__grand.tree2viz()
        else:
            s += f'nullg{v}[shape=point];\n{v}->nullg{v};\n'
            s += f'nullp{v}[shape=point];\n{v}->nullp{v};\n'
        return s


####
#
#
#        La partie de l'export mermaid
#
#
#######

    
    def tree2md(self: 'Noeud[C]') -> str:
        """
        Renvoie un diagramme au format mermaid pour une intégration md
        """
        s = ''
        v = self.__val
        if self.__petit and self.__grand:
            s += f'   {v} --> {self.__petit.__val}:::pt\n'
            s += f'   {v} --> {self.__grand.__val}:::gd\n'
            s += self.__petit.tree2md()
            s += self.__grand.tree2md()
        elif self.__petit and not self.__grand:
            s += f'   {v}-->{self.__petit.__val}:::pt\n'
            s += f'   {v}-->nullp{v}(( )):::null\n'
            s += self.__petit.tree2md()
        elif self.__grand and not self.__petit:
            s += f'   {v}-->nullg{v}(( )):::null\n'
            s += f'   {v}-->{self.__grand.__val}:::gd\n'
            s += self.__grand.tree2md()
        else:
            s += f'   {v}-->nullg{v}(( )):::null\n'
            s += f'   {v}-->nullp{v}(( )):::null\n'
        return s

    def affichemd(self: 'Noeud[C]') -> None:
        """
        Finit de mettre au format dot de mermaid :
        digraph G{
           s1 -> s2;
           s1 -> s3;
        }
        puis exporte au format png et affiche le résultat
        avec l'outil de visualisation par défaut
        """
        nl = '\n'
        s = f'graph TD\n{self.tree2md()}'
        s += '   classDef gd fill:#f08080;\n   classDef pt fill:#00ffff;\n   classDef null fill:#ffffff;\n'
        return s


#######################################
#
#
#       la fin
#
#
#
################################################


    
    def affiche(self: 'Noeud[C]') -> None:
        """
        Finit de mettre au format dot de graphviz :
        digraph G{
           s1 -> s2;
           s1 -> s3;
        }
        puis exporte au format png et affiche le résultat
        avec l'outil de visualisation par défaut
        """
        nl = '\n'
        s = f'digraph G{{{nl} graph [ordering="out"];{nl}{self.tree2viz()}}}'
        with open('arbre.dot', 'w') as f:
            f.write(s)
        c = 'dot -Tpng arbre.dot -o arbre.png && xdg-open arbre.png'
        subprocess.call(c, shell=True)

    def __repr__(self: 'Noeud[C]') -> str:
        """
        Utilise graph-easy pour afficher les arbres en mode texte.
        Au besoin, installer graph-easy:
          $ sudo apt install cpanminus
          $ sudo cpanm Graph::Easy
        Ensuite on récupère la sortie standard qui est au format binaire
        et on l'encode en utf8 pour l'avoir au format str exigé par repr
        """
        nl = '\n'
        s = f'digraph G{{{nl}graph [ordering="out"];{nl}{self.tree2viz()}}}'
        with open('arbre.dot', 'w') as f:
            f.write(s)
        cc = 'graph-easy --from=dot --as_ascii arbre.dot'.split()
        res = subprocess.run(cc, stdout=subprocess.PIPE)
        return res.stdout.decode('utf-8')



class Arbre(Generic[C]):
    """
    Arbre binaire de recherche constitué de noeuds.
    Reprend les méthodes de la classe Noeud en incluant le cas vide
    et en construisant un arbre à partir d'un noeud.
    """

    def __init__(self: 'Arbre[C]') -> None:
        """
        Constructeur : un arbre est vide ou constitué de noeuds
        """
        self.__data: Optional[Noeud[C]] = None

    def est_vide(self: 'Arbre[C]') -> bool:
        """
        Testeur : vérifie si un arbre est vide
        """
        return self.__data is None

    def insere(self: 'Arbre[C]', val: C) -> None:
        """
        Insère un élément comparable dans un arbre selon le critère
        choisi pour les noeuds.
        Si l'arbre est vide, crée le noeud-data
        """
        if self.__data is None:
            self.__data = Noeud(val)
        else:
            self.__data.insere(val)

    def hauteur(self: 'Arbre[C]') -> int:
        if self.__data is None:
            return 0
        else:
            return self.__data.hauteur()

    def nb_noeuds(self: 'Arbre[C]') -> int:
        if self.__data is None:
            return 0
        else:
            return self.__data.nb_noeuds()

    def est_feuille(self: 'Arbre[C]') -> bool:
        if self.__data is None:
            return False
        else:
            return self.__data.est_feuille()

    def nb_feuilles(self: 'Arbre[C]') -> int:
        if self.__data is None:
            return 0
        else:
            return self.__data.nb_feuilles()

    def contient(self: 'Arbre[C]', v: C) -> bool:
        if self.__data is None:
            return False
        return self.__data.contient(v)

    def visite_pre(self: 'Arbre[C]') -> None:
        if self.__data:
            self.__data.visite_pre()

    def visite_post(self: 'Arbre[C]') -> None:
        if self.__data:
            self.__data.visite_post()

    def visite_inf(self: 'Arbre[C]') -> None:
        if self.__data:
            self.__data.visite_inf()

    def visite_inf_imp(self: 'Arbre[C]') -> None:
        if self.__data:
            self.__data.visite_inf_imp()

    def visite_niveau(self:'Arbre[C]') -> None:
        if self.__data:
            self.__data.visite_niveau()

    def mini(self: 'Arbre[C]') -> C:
        assert self.__data, 'Arbre vide ! Pas de minimum'
        return self.__data.mini()

    def maxi(self: 'Arbre[C]') -> C:
        assert self.__data, 'Arbre vide ! Pas de maximum'
        return self.__data.maxi()

    def affiche(self: 'Arbre[C]') -> None:
        assert self.__data, 'Arbre vide'
        self.__data.affiche()

    def data(self: 'Arbre[C]') -> None:
        return self.__data

    def __repr__(self: 'Arbre[C]') -> str:
        if self.__data is None:
            return 'Arbre_Vide'
        else:
            return self.__data.__repr__()

        


def define_env(env):
  "Hook function"
  @env.macro
  def chapitre(chap, titre, cpt_exo=0):
       env.variables['compteur_exo'] = cpt_exo
       env.variables['compteur_def'] = 0
       env.variables['compteur_thm'] = 0
       env.variables['compteur_chap'] = chap
       return f"# Chapitre {chap} - {titre}" 
  @env.macro
  def exercice(titre=""):
       env.variables['compteur_exo'] += 1
       return f"exo \"Recherche { env.variables['compteur_chap']}-{ env.variables['compteur_exo']} {titre}\""
  @env.macro
  def definition(titre):
       env.variables['compteur_def'] += 1
       return f"def \"Définition { env.variables['compteur_chap']}-{ env.variables['compteur_def']} - {titre}\""
  @env.macro
  def theoreme(titre):
       env.variables['compteur_thm'] += 1
       return f"thm \"Théorème { env.variables['compteur_chap']}-{ env.variables['compteur_thm']} - {titre}\""

  @env.macro
  def bst(xs):
      A = Arbre()
      for x in xs:
          A.insere(x)
      s = "```mermaid\n"
      s +=  A.data().affichemd()
      s += "```"
      return s

  @env.macro
  def pyodide():
      return pyodide0()
