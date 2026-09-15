# PAGES2k 2019 — fyzikální a statistický audit

**[Otevřít úplnou studii s 28 grafy](https://nabiknab-eng.github.io/pages2k-2019-audit/)** · **[Stáhnout reprodukční balíček](https://github.com/nabiknab-eng/pages2k-2019-audit/releases/tag/v2.0)**

Česká studie propojuje audit publikovaných teplotních rekonstrukcí s analýzou původních šířek letokruhů a odvozených biologických chronologií. Rozšířená verze 2 přidává historické analogy růstových trendů, porovnání vybraných a vynechaných skupin, kontrolu věku a vysvětlení mezí interpretace screeningu.

## Co výsledky znamenají

- Nový biologický test používá roční SF-RCS chronologie a OLS trendy v úplných 50letých a 100letých oknech. Jednotkou je **index/století**, nikoli °C/století. Do tohoto výpočtu nevstupují instrumentální teploty.
- Výsledek závisí na délce období, geografii, počtu lokalit, screeningu a věkovém složení. Historické analogy existují v řadě lokalit a některých sítí; nelze z toho odvozovat globální teplotní prvenství ani jedinou příčinu změn růstu.
- Historické charakteristiky vynechaných a použitých řad se částečně překrývají. To samo o sobě nedokazuje stejnou teplotní citlivost ani neoprávněnost každého vyřazení. Úvod studie rozlišuje fyziologický výběr databáze a následný statistický R-FDR screening.
- Nejdelší pevné sítě jsou malé a všechny sítě tohoto testu končící rokem 2000 leží na severní polokouli. Nejde o globálně reprezentativní průměr všech stromů.
- Přesné párové výstupy STD a R-FDR pro krátkou kalibraci ze Supplementary Fig. 17 nebyly ve zkontrolovaných archivech nalezeny. Studie tento limit uvádí; nechybějící rekonstrukci nenahrazuje průměrem surových proxy.

## Studie a původní data

Sedm globálních rekonstrukčních metod a příslušná Fig. 1 / Supplementary Fig. 17 patří k článku **PAGES2k Consortium (2019), Consistent multidecadal variability in global temperature reconstructions and simulations over the Common Era**, Nature Geoscience, [DOI 10.1038/s41561-019-0400-0](https://doi.org/10.1038/s41561-019-0400-0). Autorská datová kolekce: [Figshare, DOI 10.6084/m9.figshare.c.4507043](https://doi.org/10.6084/m9.figshare.c.4507043).

Původně zadaný článek **Neukom et al. (2019), No evidence for globally coherent warm and cold periods over the preindustrial Common Era**, Nature, [DOI 10.1038/s41586-019-1401-2](https://doi.org/10.1038/s41586-019-1401-2), je jiná, související prostorová studie. Audit toto rozlišení zachovává. Jde o nezávislou analýzu, nikoli oficiální repozitář PAGES2k nebo autorů článků.

## Obsah ke stažení

Release **v2.0** obsahuje `pages2k-audit-site.zip`: rozbalením vznikne samostatně čitelný web a datové adresáře. HTML má obrázky vložené a funguje i offline. Relativní odkazy na CSV, JSON, NPZ, grafy a skripty jsou zachovány. Větší data jsou v release, aby nezatěžovala historii Git.

- `finalni_studie_v2/` — hlavní rozšířená studie, datový slovník, nové výsledky a skripty.
- `finalni_studie/` — předchozí audit, numerické vstupy, výstupy a reprodukční archivy.
- `letokruhy_audit_vek_a_selekce/phase2_observed_age.npz` — pozorované věky pro novou citlivostní analýzu.
- `PUBLICATION_MANIFEST.csv` — SHA256 všech souborů této veřejné distribuce.
- `PUBLICATION_CHANGES.json` — přesně vyjmenované rozdíly proti místnímu archivnímu balíčku.

Starší archiv `finalni_studie/archives/screening_reprodukce.zip` obsahuje instrumentální mřížku **pouze pro oddělený audit screeningu**. Starší zpráva uchovává také oddělená teplotní srovnání. Tyto podklady nejsou vstupem nového biologického testu; proxy-only reprodukce je v samostatném archivu.

## Reprodukce a integrita

Po rozbalení se řiďte `finalni_studie_v2/README_reprodukce.md` a `DATOVY_SLOVNIK.md`. Python 3.12; použité verze knihoven jsou zdokumentované v balíčku. Z kořene rozbalené distribuce lze spustit:

```sh
python finalni_studie_v2/analyza_historickych_analogu.py
python finalni_studie_v2/grafy_a_kontroly.py
python finalni_studie_v2/revize_html.py
```

Veřejná kopie zachovává všechny vědecké hodnoty, HTML a obrázky beze změny. Dva textové soubory mají nahrazenou místní cestu k počítači; systémové `.DS_Store` a dva plné článkové PDF nejsou šířeny. Články jsou dostupné u vydavatele. Původní validační záznamy a manifesty jsou zachovány jako doklad předpublikační kontroly: **původní striktní kontrola všech hashů nemůže veřejné distribuci beze změn projít**, protože zahrnuje i uvedené PDF a původní podobu dvou metadatových souborů. Veřejnou kopii ověřuje její vlastní manifest. Numerické vstupy nové analýzy zůstaly totožné.

Reprodukční skripty mohou přegenerovat výstupy; před vlastními úpravami si uchovejte kopii distribuce. Popisné percentily nejsou testy nezávislých oken, protože se klouzavá okna překrývají.

## Původ a práva

Přesná URL, DOI, data stažení a kontrolní součty zdrojů jsou v manifestech a u tvrzení ve studii. Data a převzatý autorský kód si zachovávají podmínky svých původních zdrojů; tento repozitář jim nepřiděluje novou souhrnnou licenci. Při dalším použití citujte původní zdroje i konkrétní verzi tohoto auditu.
