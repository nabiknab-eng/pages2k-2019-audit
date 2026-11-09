"""Apply the editorial update to the verified v2.0 release for GitHub Pages."""

from pathlib import Path
import sys


PAGE = Path("finalni_studie_v2/PAGES2k_2019_fyzikalni_a_statisticky_audit_v2.html")
SUMMARY = """<section id="strucne" aria-labelledby="strucne-nadpis">
<h2 id="strucne-nadpis">Dva výsledky auditu</h2>
<div class="provenance audit">
<p><strong>Teplotní graf.</strong> Z publikovaných výstupů autorů jsme znovu sestavili hlavní graf globální teploty (Figure 1a). Hodnoty se shodují v mezích zaokrouhlení. Tím ověřujeme sestavení grafu z výstupů původních metod, které již vycházejí z autorského výběru záznamů. <a href="#figure1">Jak jsme graf ověřili</a>.</p>
<p><strong>Růst stromů.</strong> V samostatném srovnání 95 lokalit při stejných pozorovaných věcích vzorků vyšla průměrná šířka letokruhů v letech 1951–2000 o 37,4 % vyšší než v letech 1801–1850. Výsledek popisuje růst stromů ve zkoumaném souboru. Pro odhad teploty je třeba samostatně ověřit vztah růstu k teplotě. <a href="#age">Věkové srovnání a podrobné výsledky</a>.</p>
</div>
<p class="new-note">Úvod a popis výběru dat byly doplněny pro web. Archiv v2.0 ke stažení obsahuje původní znění, vstupy a výpočty.</p>
</section>"""

SCREENING = """<strong>Výběr dat: 692 záznamů ve výchozí databázi → 257 po regionálním teplotním výběru (R-FDR) → různé podmnožiny podle rekonstrukční metody.</strong> Databáze zahrnuje letokruhy i další nepřímé záznamy."""

CATALOGUE = """<p><strong>Podklad pro další ověření.</strong> Katalog <a href="https://essd.copernicus.org/articles/18/1185/2026/">DoD2k (2026)</a> propojuje pět zdrojových kolekcí záznamů za poslední dvě tisíciletí a identifikuje jejich překryvy. Nabízí širší soubor kandidátů pro budoucí test citlivosti na výběr dat. Výsledky tohoto auditu z něj nevycházejí.</p>"""


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f"Expected one editorial anchor: {old!r}")
    return text.replace(old, new, 1)


def main(site):
    page = site / PAGE
    html = page.read_bytes().decode("utf-8")
    anchor = '</header>\n<section id="cteni">'
    html = replace_once(html, anchor, '</header>\n' + SUMMARY + '\n<section id="cteni">')
    html = replace_once(
        html,
        'Hlavní experiment používá 257 záznamů vybraných regionálním teplotním screeningem <strong>R-FDR</strong>.',
        SCREENING,
    )
    anchor = '[1, Methods]</a><a class="citation" href="https://doi.org/10.6084/m9.figshare.8137706.v3" title="Neukom et al. Reconstruction ensembles, Figshare 8137706, verze 3; sedm TXT po 1 000 členech.">[4]</a></p>'
    html = replace_once(html, anchor, anchor + CATALOGUE)
    page.write_bytes(html.encode("utf-8"))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
