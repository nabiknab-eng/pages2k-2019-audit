"""Apply the editorial update to the verified v2.0 release for GitHub Pages."""

from pathlib import Path
import sys


PAGE = Path("finalni_studie_v2/PAGES2k_2019_fyzikalni_a_statisticky_audit_v2.html")
SUMMARY = """<section id="strucne" aria-labelledby="strucne-nadpis">
<h2 id="strucne-nadpis">Dva výsledky auditu</h2>
<div class="provenance audit">
<p><strong>Teplotní graf.</strong> Z publikovaných výstupů autorů jsme znovu sestavili hlavní graf globální teploty (Figure 1a). Hodnoty se shodují v mezích zaokrouhlení. Tím ověřujeme sestavení grafu z výstupů původních metod, které již vycházejí z autorského výběru záznamů. <a href="#figure1">Jak jsme graf ověřili</a>.</p>
<p><strong>Růst stromů.</strong> V samostatném srovnání 95 lokalit při stejných pozorovaných věcích je průměrná normalizovaná úroveň šířek v letech 1951–2000 o 37,4 % vyšší než v letech 1801–1850. Nejprve šířky vztahujeme k vlastní referenci lokality, poté stejně vážíme společné věky a lokality. Procento počítáme až z poměru obou síťových úrovní. Není to teplotní změna ani růst uvnitř samotného období 1951–2000. Výsledek popisuje růst stromů ve zkoumaném souboru. Pro odhad teploty je třeba samostatně ověřit vztah růstu k teplotě. <a href="#age">Věkové srovnání a podrobné výsledky</a>.</p>
</div>
<p class="new-note">Úvod a popis výběru dat byly doplněny pro web. Archiv v2.0 ke stažení obsahuje původní znění, vstupy a výpočty.</p>
</section>"""

SCREENING = """<strong>Výběr dat: 692 záznamů ve výchozí databázi → 257 po regionálním teplotním výběru (R-FDR) → různé podmnožiny podle rekonstrukční metody.</strong> Databáze zahrnuje letokruhy i další nepřímé záznamy."""

CATALOGUE = """<p><strong>Podklad pro další ověření.</strong> Katalog <a href="https://essd.copernicus.org/articles/18/1185/2026/">DoD2k (2026)</a> propojuje pět zdrojových kolekcí záznamů za poslední dvě tisíciletí a identifikuje jejich překryvy. Nabízí širší soubor kandidátů pro budoucí test citlivosti na výběr dat. Výsledky tohoto auditu z něj nevycházejí.</p>"""


APPROVED_DETAILS = {
    "cteni": """<div class="provenance limit"><p><strong>Co měří letokruh.</strong> Šířka W je radiální přírůstek. Pro kruhový průřez platí ΔA = π[r² − (r − W)²] = 2πrW − πW²; stejná šířka při různém poloměru neznamená stejný přírůstek plochy ani biomasy. Ta závisí také na výšce, tvaru a hustotě dřeva i rozdělení uhlíku ve stromu.</p><p>V okolí určitého stavu lze místní odezvu schematicky linearizovat: ΔW ≈ a<sub>T</sub>ΔT + a<sub>V</sub>ΔV + a<sub>C</sub>ΔC + … + ε. Koeficienty pro teplotu, vodní podmínky a CO₂ nemusí být stálé v místě ani v čase. Z jedné změny šířky bez dalších vazeb nelze jednoznačně dopočítat více současně neznámých změn prostředí. Jde o ilustraci, nikoli o nový fitovaný model.</p></div>""",
    "figure1": """<details><summary>Co přesně propouští filtr?</summary><p>Pro ideální frekvenční odezvu použitého digitálního Butterworthova filtru řádu 2 po obou průchodech, mimo okraje záznamu, je amplitudový přenos A(P) = 1/{1 + [tan(π/P)/tan(π/62)]⁴}. Při periodě P = 62 let vychází A = 1/2. Naproti tomu aritmetický průměr L ročních hodnot má přenos |sin(πL/P)/[L sin(π/P)]|. Název filtru neurčuje nejkratší přeživší událost; u konečného záznamu záleží i na doplnění okrajů.</p></details>""",
    "age": """<div class="provenance audit"><p><strong>Přesný význam 37,4 %.</strong> Každou šířku dělíme vlastní referencí lokality r<sub>i</sub>: průměrem dostupných ročních mediánů za 1801–1900. Roční medián vyžaduje alespoň pět vzorků a reference 50 platných let. V každé lokalitě průměrujeme vzorky po společných přesných pozorovaných věcích a potom dáváme věkům i 95 lokalitám stejné váhy.</p><p>I<sub>i,p</sub> = (1/|A<sub>i</sub>|) Σ<sub>a∈Aᵢ</sub> (W̄<sub>i,a,p</sub>/r<sub>i</sub>); I<sub>p</sub> = (1/95)Σ<sub>i=1…95</sub>I<sub>i,p</sub>. Výsledek je 100 × (I<sub>1951–2000</sub>/I<sub>1801–1850</sub> − 1) = 100 × (1,4794183150/1,0764510263 − 1) = 37,4348 %. Jde o poměr agregovaných normalizovaných úrovní, nikoli o průměr procent jednotlivých stromů nebo poměr všech šířek sloučených v mm.</p></div>""",
    "ladder": """<p class="new-note">Kontrast K = (b₂ − b₁)/(|b₂| + |b₁|) je bezrozměrný, má znaménko rozdílu sklonů a leží mezi −1 a +1. Pro dva nulové sklony není definován. Při přechodu z poklesu na růst je K = +1 bez ohledu na velikost obou sklonů, proto jej čtěte spolu s b₁ a b₂.</p>""",
    "timing": """<p class="new-note">Pro pevnou síť lokalit, neměnné váhy a stejné úplné roky platí b(ΣwᵢIᵢ) = Σwᵢb(Iᵢ): OLS sklon průměru je váženým průměrem místních sklonů. Při proměnlivých vahách nebo lokalitách tato rovnost obecně neplatí. Percentil průměrného sklonu navíc není průměrem místních percentilů.</p>""",
}


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
    for section_id, detail in APPROVED_DETAILS.items():
        marker = f'<section id="{section_id}">'
        html = replace_once(html, marker, marker + detail)
    page.write_bytes(html.encode("utf-8"))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
