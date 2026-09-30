# Roadmap

**Status:** 🟢 actief — fase 1 afgerond 2026-09-30

Klein beginnen. Elke fase pas starten als de vorige iets oplevert.

| Fase | Wat | Eric doet | Status |
|------|-----|-----------|--------|
| 0 | Repo, deploy key, oude ideeën veiligstellen | Deploy key toevoegen, brede key weg | 🔧 |
| 1 | Skelet: CLAUDE.md, profiel, lessen, memory, TODO, ORACLE, settings, budgettest | Persona kiezen, profiel invullen | ✅ |
| 2 | Eerste bron + verify-test | Read-only key in `~/.config/defi-research/.env` | ⏸️ |
| 3 | Handmatige analyses met correcties (= training) | Protocollen kiezen die je kent, corrigeren | ⏸️ |
| 4 | Skills; daarna signalen met paper tracking | Plan signaalbrug goedkeuren | ⏸️ |
| 5 | Executor op andere Chromebook (aparte repo) | Alles | ⏸️ |

## Fase 4 — eisen aan de signaalbrug (uit Fable-review 2026-09-30)

Eerst een apart plan `plans/signal_bridge_plan.md`, laten reviewen, dan bouwen.

- **Goedkeuring aan de executor-kant**, handmatig op de andere machine. Een `approved`-vlag in deze
  repo is geen handtekening: Claude commit hier zelf.
- **Schema:** JSON Schema met `schema_version`; executor weigert onbekende versies. Velden o.a.
  `id`, `created_at`, `valid_until`, `status` (open/cancelled/expired/superseded), `supersedes`,
  referentieprijs + max. afwijking. Geen vrije tekst in velden die de executor leest. Intrekken =
  nieuw record, nooit bewerken.
- **Git-brug:** executor leest met een read-only deploy key, accepteert alleen fast-forward (stopt
  als nieuwe HEAD geen afstammeling is van de laatst geziene commit). Risk caps staan hard in de
  executor-config, nooit in een signaal.
- **Paper tracking, methode vooraf vast:** spread/slippage/gas/fees meerekenen; instap op het
  moment dat de executor had kúnnen handelen; bronlatentie; liquiditeitsdiepte voor de omvang;
  benchmark BTC/ETH aanhouden; horizon per signaal vooraf; ook afgewezen signalen loggen;
  gecorreleerde signalen als cluster; uitkomst berekend door een script, niet door Claude.
- **Live-gate (executor):** ≥30 paper-signalen over ≥2 maanden, positief na kosten én boven
  benchmark, kill switch getest, startkapitaal door Eric gekozen.
- **Andere Chromebook:** wallet-key alleen leesbaar voor het botproces, niet voor Claude-sessies.
