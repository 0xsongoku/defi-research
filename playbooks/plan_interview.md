# Plan-mode zwaar spoor — interview-protocol

**Wanneer:** zie trigger-criteria in `CLAUDE.md` § Plan mode. De agent beoordeelt zelf of
dit van toepassing is en kondigt de keuze expliciet aan vóór start.

**Integratie in het standaard plan-mode-protocol:**
- Dit protocol **vervangt de 5-vragen-stap** uit het standaard spoor volledig — geen
  aparte AskUserQuestion-ronde vooraf.
- De **senior-architect-review** (3 vaste vragen, zie `CLAUDE.md` § Plan mode; huidig
  model: Fable, `model="fable"` — dit wisselt, check bij twijfel de Agent-tool se model-enum)
  schuift naar **na Phase 3 (Specification Lock)**, vóór de "Lock this spec and begin
  execution?"-vraag: spawn de reviewer op de geconsolideerde spec, presenteer spec + kritiek
  samen, pas de spec aan als de kritiek terecht is, stel dan pas de lock-vraag.
- Het **confidence-level-mechanisme** (high/moderate/low/unknown) zit al ingebakken in elke
  "My recommendation"-regel hieronder — geen losse stap nodig.

---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding.

Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. Ask one question at a time. For each question, give your recommended answer alongside it so I can react to a concrete position rather than design from scratch.

If a question can be answered from context I've already shared (docs, code, files, prior messages), answer it yourself instead of asking me.

Begin once I've shared the plan.

### Phase 1 — Ingestion (no interviewing yet)
On receiving the plan, output only:
1. **Restatement** — one paragraph of what you understand the goal to be, so I can correct misreads before any work is done.
2. **Design tree** — every unresolved decision the plan implies, grouped by dependency layer (foundation → structure → surface). Tag each item as `[OPEN]`, `[RESOLVED FROM CONTEXT: <your answer, confidence>]`, or `[DEFERRED: depends on <id>]`.
3. **Critical path** — the subset of decisions that, if wrong, break everything downstream. These are interviewed first.

If the plan is too thin to map a tree, say so plainly and request the missing primitives in a single message before proceeding.

### Phase 2 — Interview Loop
One question per turn. Each question uses this template:

> **Decision:** <what is being settled>
> **Why it matters:** <what it unlocks or breaks downstream>
> **My recommendation:** <concrete answer> — confidence: <high/moderate/low/unknown>
> **Reasoning:** <one or two sentences>
> **Question to you:** <what you need from me; omit if you're locking your own recommendation by default>

At the top of every turn, maintain a running ledger:
- **LOCKED:** <decisions settled, one per line>
- **OPEN:** <decisions remaining, in interview order>

If I accept your recommendation (explicitly, or by silence after you restate it), mark it LOCKED and advance. If I push back without new evidence or a superior argument, restate the position per Part I rules. Do not soften to keep the conversation moving.

### Phase 3 — Specification Lock
When every critical-path decision is LOCKED, stop interviewing. Produce a single consolidated build specification: every locked decision, the rationale chain, the execution sequence, and an explicit risk register flagging any decision held at low confidence or any deferred decision still outstanding.

Then ask exactly once: **"Lock this spec and begin execution?"** Do not begin building before I confirm.

### Phase 4 — Execution
Build against the locked spec. Do not improvise outside it. Rules:
- If you hit a decision point not surfaced in Phase 1, stop, drop back into interview format for that decision only, lock it, then resume.
- If I introduce a change mid-execution, treat it as a re-open: identify which locked decisions it invalidates, surface the cascade, and re-interview the affected branch before continuing.
- On completion, output a delta report: what was built vs. spec, what diverged and why, what remains in the risk register.

When you understand, ask me what my plan is.
