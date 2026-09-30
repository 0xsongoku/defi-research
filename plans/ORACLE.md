# ORACLE

Ideeënbak. Ik zaai ideeën; onderzoek verrijkt ze. Geen TODO's — geannoteerd denken-hardop.

Format per idee:

```
## <korte naam> — JJJJ-MM-DD

**Strategie:** wat het in één zin doet
**Trigger/signaal:** waar komt de waarde vandaan
**Open vragen:** wat moet je nog uitzoeken
**Status:** idea / researching / dropped / promoted
```

---

> Overgenomen uit `0xsongoku/trading` (2026-06-14) op 2026-09-30. Ongewijzigd, dus nog niet
> getoetst (verify-first).

## fundamental_screener — 2026-06-14

**Strategie:** screen mid-cap tokens (market-cap-rank ~20-150) op fundamentals → kandidatenlijst met groeipotentieel, mogelijk uitmondend in concreet investeer-advies. Filters: **tokenomics op fully-diluted basis (FDV)**, **volume stijgend over 30 dagen**. Pas een formule toe die *potentiële* MC tegen *huidige* MC afzet (groeipotentieel/upside-ratio).
**Trigger/signaal:** ondergewaardeerde FDV t.o.v. realistisch groeipotentieel; 30d-volumestijging als aandacht-/momentum-proxy. De band rank 20-150 = voorbij de mega-caps (groei-ruimte) maar boven de micro-cap-ruis.
**Open vragen:** (1) **welke formule precies** voor "groeipotentieel vs huidige MC" — comparable/TAM-MC, FDV/MC-ratio, of iets met categorie-mediaan? (2) databron + limieten (CoinGecko/CMC API gratis-tier, welke velden: FDV, circulating, volume-30d?); (3) **FDV-only valkuil** — lage circulating + grote toekomstige unlocks = verkoopdruk; moet vesting/unlock-schema mee? (4) hoe ver gaat "investment advies" — signaal/score, of allocatie-suggestie? (verify-first: geen advies bouwen op één ongetoetste ratio); (5) waarom exact 20-150 — te laag voor 100x, te hoog voor veiligheid? band valideren tegen historie.
**Status:** idea

## ta_dashboard — 2026-06-14

**Strategie:** technische-analyse-laag in de UI met **buy/sell-zones** op daily- en weekly-chart + een paar duidelijke indicatoren (**RSI/MACD**), met **TradingView aangesloten**.
**Trigger/signaal:** oversold/overbought (RSI), trend-/momentum-cross (MACD), support/resistance-zones per timeframe; daily+weekly confluentie als sterkste signaal.
**Open vragen:** (1) **TradingView-integratie** — gratis widget-embed, betaalde Charting Library (licentie), of data zelf via API + eigen chart? (2) buy/sell-zones handmatig getekend of **auto** afgeleid uit indicatoren/S-R-algoritme? (3) confluentie-regel daily×weekly formaliseren; (4) alleen tonen (signaal) of ook alerts? (5) past TA op lange-termijn-spot-horizon, of is dit vooral timing-laag bovenop de fundamentele screener?
**Status:** idea

## btc_cycle_macro — 2026-06-14

**Strategie:** lange-termijn **macro-signalen die de BTC-cyclus volgen** (halving-offset, cyclus-fase) om portfolio-breed risk-on/risk-off te timen — de overkoepelende laag boven de losse coin-signalen.
**Trigger/signaal:** cyclus-metrics → fase-bepaling: bv. MVRV/SOPR (on-chain), Pi-cycle-top, halving-offset, BTC-dominance-rotatie → vertaalt naar accumulate / hold / de-risk.
**Open vragen:** (1) **welke metrics** — on-chain (MVRV/SOPR, vereist Glassnode-achtige bron, deels betaald) vs puur prijs-gebaseerd (Pi-cycle, MA's, gratis)? (2) databron + kosten; (3) hoe vertaalt fase naar **concreet advies** (cash-allocatie-%? per-band-actie?); (4) **cyclus-these is fragiel** — post-ETF/macro-regime kan de historische cyclus breken; verify-first, niet blind op vorige cycli ankeren; (5) verhouding tot `ta_dashboard` (macro-filter dat de TA-signalen poort?).
**Status:** idea
