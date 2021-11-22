###############
# Débuter avec Material for MkDocs https://gitlab.com/ens-fr/mkdocs
"""
- /usr/local/bin/python -m pip install mkdocs-macros-plugin
"""
###############

import os

def define_env(env):
    "Hook function"

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        return f"""<iframe src="https://console.basthon.fr/?from={env.variables.site_url}{env.variables.page.url}../{exo}" width=100% height={hauteur}></iframe>

[Lien dans une autre page](https://console.basthon.fr/?from={env.variables.site_url}{env.variables.page.url}../{exo})
"""

    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""

    @env.macro
    def py(nom: str) -> str:
        "macro python rapide"
        return script('python', "scripts/" + nom + ".py")

    @env.macro
    def html_fig(num: int) -> str:
        "Renvoie le code HTML de la figure n° `num`"
        return f'--8<-- "docs/' + os.path.dirname(env.variables.page.url.rstrip('/')) + f'/figures/fig_{num}.html"'





###############
# Enumération https://gitlab.com/ens-fr/enumeration/-/tree/master
"""
    - pip install termtosvg
    - pip install drawSvg
    - pip install ipythonblocks
"""
###############

import os
from ipythonblocks import BlockGrid, colors

def define_env(env):
    "Hook function"

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        return f"""<iframe src="https://console.basthon.fr/?from={env.variables.site_url}{env.variables.page.url}../{exo}" width=100% height={hauteur}></iframe>

[Lien dans une autre page](https://console.basthon.fr/?from={env.variables.site_url}{env.variables.page.url}../{exo})
"""

    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""

    @env.macro
    def py(nom: str) -> str:
        "macro python rapide"
        return script('python', "scripts/" + nom + ".py")

    @env.macro
    def html_fig(num: int) -> str:
        "Renvoie le code HTML de la figure n° `num`"
        return f'--8<-- "docs/' + os.path.dirname(env.variables.page.url.rstrip('/')) + f'/figures/fig_{num}.html"'


    @env.macro
    def pv_intro():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['White'])
        grid[:, 0] = colors['Blue']
        grid[:, 5] = colors['Blue']
        grid[0, 1:5] = colors['LightGreen']
        grid[3, 1:5] = colors['Green']
        grid[1:3, 1:3] = colors['Red']
        grid[1:3, 3:5] = colors['DarkRed']
        grid[0:2, 6:8] = colors['Red']
        grid[2:4, 6:8] = colors['DarkRed']
        return grid._repr_html_()

    @env.macro
    def trois_motifs():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['White'])
        grid[:, 0] = colors['Blue']
        grid[0, 2:6] = colors['Green']
        grid[0:2, 7:9] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_0():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[:, 8:10] = (255, 255, 255)
        return grid._repr_html_()

    @env.macro
    def rect4x8_1():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 8:10] = (255, 255, 255)
        return grid._repr_html_()

    @env.macro
    def rect4x8_2():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0, 8:10] = (255, 255, 255)
        grid[3, 8:10] = (255, 255, 255)
        return grid._repr_html_()

    @env.macro
    def rect4x8_3():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[:, 7] = colors['Blue']
        return grid._repr_html_()

    @env.macro
    def rect4x8_4():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0, 4:8] = colors['Green']
        grid[1, 4:8] = colors['LightGreen']
        grid[2, 4:8] = colors['Green']
        grid[3, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_5():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 6:8] = colors['DarkRed']
        grid[2:4, 6:8] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_6():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 6:8] = colors['Red']
        grid[2, 4:8] = colors['Green']
        grid[3, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_7():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0, 4:8] = colors['Green']
        grid[1:3, 6:8] = colors['Red']
        grid[3, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_8():
        grid = BlockGrid(width=8, height=4, block_size=50, fill=colors['Black'])
        grid[0, 4:8] = colors['Green']
        grid[1, 4:8] = colors['LightGreen']
        grid[2:4, 6:8] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_9():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 8:10] = colors['White']
        grid[2:4, 8:10] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_10():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0:2, 8:10] = colors['White']
        grid[2, 6:10] = colors['Green']
        grid[3, 6:10] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def rect4x8_11():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0, 8:10] = colors['White']
        grid[3, 8:10] = colors['White']
        grid[1:3, 8:10] = colors['Red']
        return grid._repr_html_()

    @env.macro
    def rect4x8_12():
        grid = BlockGrid(width=10, height=4, block_size=50, fill=colors['Black'])
        grid[0, 8:10] = colors['White']
        grid[3, 8:10] = colors['White']
        grid[1, 6:10] = colors['Green']
        grid[2, 6:10] = colors['LightGreen']
        grid[3, 4:8] = colors['Green']
        grid[0, 4:8] = colors['LightGreen']
        return grid._repr_html_()

    @env.macro
    def table_a():
        a = [1, 1, 2, 3]
        b = [1, 1, 3, 4]
        c = [1, 1, 2, 3]
        for n in range(4, 24):
            # On ajoute a[n], puis b[n], puis c[n]
            a.append(a[n-1] + a[n-2] + a[n-4] + 2*b[n-4] + c[n-4])
            b.append(a[n] + b[n-2])
            c.append(a[n] + c[n-4])

        def markdown(a, ni, nf):
            """Renvoie un joli tableau markdown des valeurs de
            la suite a_n pour n dans [ni, nf["""
            ans = "|$n$|"
            for n in range(ni, nf): ans += f"${n}$|"
            ans += "\n|:---:|"
            for n in range(ni, nf): ans += ":---:|"
            ans+= "\n|$a_n$|"
            for n in range(ni, nf): ans += f"${a[n]}$|"
            return ans + "\n\n"

        return markdown(a, 0, 24)

###############
# Bac à sable https://gitlab.com/ens-fr/sandbox/-/tree/master
"""
mkdocs-material
mkdocs-macros-plugin
markdown-aafigure
markdown-svgbob
mkdocs-graphviz
mkdocs_pymdownx_material_extras
mkdocs-asy
mkdocs-thumbnails
mkdocs-awesome-pages-plugin
mkdocs-kroki-plugin
mkdocs-markmap

"""
###############

import os
import sys
import subprocess
import shutil

def define_env(env):
    "Hook function"

    @env.macro
    def info() -> str:
        sortie = ""

        processus_complet = subprocess.run(
            ["gnuplot", "--version"],
            capture_output=True,
            text=True)
        if processus_complet.returncode != 0:
            return "Erreur avec GnuPlot\n" + processus_complet.stderr
        sortie += processus_complet.stdout
        sortie += processus_complet.stderr
        
        sortie += "\n"*2

        processus_complet = subprocess.run(
            ["asy", "-version"],
            capture_output=True,
            text=True)
        if processus_complet.returncode != 0:
            return "Erreur avec Asy\n" + processus_complet.stderr
        sortie += processus_complet.stdout
        sortie += processus_complet.stderr

        return sortie


    @env.macro
    def run(moteur: str, script: str, args_moteur=[]) -> str:
        """macro qui prend
            - un moteur [python, gnuplot, asy, latex, ...]
            - un nom de fichier `script` qui est dans {env.variables.script_dir}
        - déduit une association de sortie (type + affichage)
            - matplotlib | gnuplot | asy | latex -> .svg -> dans une balise image
            - python -> .out -> dans une fence python
            - drawSvg | ipythonblock -> .html -> nature
        
        >>> run('python', 'truc.py')
        '```python\nsortie .txt de truc.py\n```\n'
        
        >>> run('gnuplot', 'fig.p')
        '![gnuplot fig.p](fig.p.svg)'
        
        >>> run('drawSvg', 'bidule.py')
        'du contenu .html prêt à tourner'
        
        >>> run('python-moteur2', 'jouet.py')  # 'moteur2' pourrait être 'mermaid' | 'raw' | '' |
        '```moteur2\nsortie de truc.py\n```\n'
        
        
        - La macro regarde si `script.sortie.svg|.html|.txt` existe aussi et est plus récent,
        - sinon, regarde les droits en écriture dans le dossier de `script`
        - crée ou recrée `...sortie...` dans le dossier de `script`
        - ou alors un nouveau dossier local `tmp_run_macro`.

        """
        try:
            m_time_src = os.stat(env.variables.gnuplot_dir + file).st_mtime_ns
        except FileNotFoundError:
            print(f"WARNING macro gnuplot : Fichier {file} absent", file=sys.stderr)
            return f":warning: Fichier {file} absent"

        found = True
        try:
            m_time_svg = os.stat(env.variables.gnuplot_dir + file + '.svg').st_mtime_ns
        except FileNotFoundError:
            found = False

        if not(found) or (m_time_src > m_time_svg):
            pass
        # pas finie
        
    @env.macro
    def gnuplot(file: str) -> str:
        processus_complet = subprocess.run(
            ["gnuplot", env.variables.gnuplot_dir + file],
            capture_output=True,
            text=True)
        if processus_complet.returncode != 0:
            return "Erreur avec GnuPlot\n" + processus_complet.stderr
        sortie = processus_complet.stdout.replace('\n', '\t')
        return sortie[sortie.find('<svg'):]

    @env.macro
    def asy(file: str) -> str:
        racine, suffix = file[:-4], file[-4:]
        if suffix != '.asy':
            return f"Fichier {file} invalide ; il doit se terminer par '.asy'"
        
        tmp_eps = "temp_" + racine + ".eps"
        processus_complet = subprocess.run(
            ["asy", "-o" + tmp_eps, 
             env.variables.asy_dir + file],
            capture_output=True)
        if processus_complet.returncode != 0:
            return "Erreur avec Asy\n" + processus_complet.stderr.decode("utf-8")
        
        processus_complet = subprocess.run(
            ["epstopdf", tmp_eps],
            capture_output=True)
        if processus_complet.returncode != 0:
            return "Erreur avec epstopdf\n" + processus_complet.stderr.decode("utf-8")
        
        tmp_pdf = "temp_" + racine + ".pdf"
        tmp_svg = "temp_" + racine + ".svg"
        processus_complet = subprocess.run(
            ["pdf2svg", tmp_pdf, tmp_svg],
            capture_output=True)
        if processus_complet.returncode != 0:
            return "Erreur avec pdf2svg\n" + processus_complet.stderr.decode("utf-8") + \
                processus_complet.stdout.decode("utf-8") + "\n" + \
                    "\n".join(truc for truc in processus_complet.args)
        
        with open(tmp_svg, 'r') as f:
            sortie = f.readlines()

        # ménage
        processus_complet = subprocess.run(
            ["rm", tmp_eps, tmp_pdf, tmp_svg],
            capture_output=True)
        if processus_complet.returncode != 0:
            return "Erreur avec rm\n" + processus_complet.stderr.decode("utf-8") + \
                processus_complet.stdout.decode("utf-8") + "\n" + \
                    "\n".join(truc for truc in processus_complet.args)
        
        return "\t".join(sortie[1:])

    @env.macro
    def asy3D(file: str) -> str:
        racine, suffix = file[:-4], file[-4:]
        if suffix != '.asy':
            return f"Fichier {file} invalide ; il doit se terminer par '.asy'"

        sortie_html = racine + ".html"
        processus_complet = subprocess.run(
            ["asy","-fhtml", "-offline", "-odocs/"+sortie_html,
             env.variables.asy_dir + file],
            capture_output=True)
        if processus_complet.returncode != 0:
            return "Erreur avec Asy\n" + processus_complet.stderr.decode("utf-8")
        
        return f'<iframe src="../{sortie_html}" width="568" height="416" frameborder="0"></iframe>'



    @env.macro
    def python_ide(exo: str, hauteur: int = 700) -> str:
        """Renvoie du HTML pour embarquer un fichier `exo` dans un ide sommaire
        + Basthon est la solution 2021, RGPD ok
        """
        lien = f"https://console.basthon.fr/?from={env.variables.scripts_url}{exo}"
        return f"<iframe src={lien} width=100% height={hauteur}></iframe>" + \
                f"[Lien dans une autre page]({lien})"
    
    @env.macro
    def python_carnet(carnet: str, aux: str = '', module: str = '',
                      auxs=None, modules=None,
                      hauteur: int = 700) -> str:
        """Renvoie du HTML pour embarquer un fichier `carnet.ipynb` dans un notebook
        + Basthon est la solution 2021, RGPD ok
        """
        lien = f"https://notebook.basthon.fr/?"
        if carnet != '':
            lien += f"from={env.variables.scripts_url}{carnet}&"
        else:
            lien += f"from={env.variables.scripts_url}1_cell_python.ipynb&"
        
        if aux != '':
            lien += f"aux={env.variables.scripts_url}{aux}&"
        if auxs is not None:
            for aux in auxs:
                lien += f"aux={env.variables.scripts_url}{aux}&"
        
        if module != '':
            lien += f"module={env.variables.scripts_url}{module}&"
        if modules is not None:
            for module in modules:
                lien += f"module={env.variables.scripts_url}{module}&"
        
        return f"<iframe src={lien} width=100% height={hauteur}></iframe>" + \
                f"[Lien dans une autre page]({lien})"
