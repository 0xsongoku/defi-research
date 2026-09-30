# Bronnen

Eén bestand per bron: `intel/sources/<bron>.md`. Eén bron tegelijk toevoegen.

## Workflow nieuwe bron (API of MCP)

1. **Notitie** met onderstaande kop.
2. **Verify-test:** één bekend feit vergelijken met een tweede, echt onafhankelijke bron
   (bv. USDC totalSupply via RPC vs. Etherscan; TVL van één protocol vs. de site van dat protocol).
3. Pas bij PASS: status `verified` + datum. Daarna mag de bron in analyses.
4. **MCP-servers:** alleen read-only. Versie vastzetten, broncode bekeken, geen tools die kunnen
   ondertekenen of versturen. Noteer welke tools van de server gebruikt mogen worden.

## Kop per bron

```
# <bron>
**Status:** candidate / verified (JJJJ-MM-DD) / dropped
**Type:** API / MCP / website
**Levert:** welke data
**Auth:** geen / read-only key (`<VARNAAM>` in ~/.config/defi-research/.env)
**Limieten:** rate limit, kosten, historie
**Bekende valkuilen:** stille fouten, vertraging, afwijkende definities
**Verify-test:** wat vergeleken, met welke bron, uitkomst, datum
**Onafhankelijk van:** welke andere bronnen deze data niet delen
```
