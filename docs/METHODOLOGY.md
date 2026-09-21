# The Phase and Step Methodology

The project's workflow is strictly structured around incremental, verifiable progress, designed to survive context switching, abrupt session endings, and handoffs between team members or AI sessions.

## 1. Hierarchy & Scope
- **Hierarchy:** Work is broken down into major Phases (e.g., P0, P1, ... P9). Each phase is subdivided into discrete Steps (e.g., P0-S1, P3-S2).
- **Small Scopes:** Steps are intentionally kept small (designed to take roughly 30–90 minutes each) to minimize the cost of lost work.

## 2. The Contract vs. The State
- `PLAN.md` is the immutable contract. It contains the authoritative list of phases, steps, and their acceptance criteria. It changes rarely and only to refine requirements, never to record progress.
- `STATUS.md` is the state. It tracks progress, handoff notes, and which steps are TODO, IN_PROGRESS, BLOCKED, DONE, or SUPERSEDED.
- `DECISIONS.md` is the reasoning. Non-obvious technical choices and their rationales are appended here so the context outlives the conversation that generated it.

## 3. Milestone Markers
- `▲` indicates a phase is required for a viable product.
- `— SUBMITTABLE —` designates the exact cutoff where the project becomes a complete baseline, meaning everything after it is an optional enhancement (upside).

## 4. Test Alignment & Continuous Committing
- Every single step maps exactly to a test suite marker (e.g., `@pytest.mark.p0_s1` or a specific `pio test` environment).
- Because sessions can end abruptly, broken work is committed rather than lost. The state of that broken work is explicitly recorded in `STATUS.md`.

## 5. Mandatory Step-by-Step Review Gate
- **Never Execute Steps Consecutively Without Review:** The agent/engineer must execute exactly **one step at a time**.
- Upon completing a step, running its cumulative verification gate (`./scripts/verify.sh <STEP_ID>`), updating `STATUS.md`, and committing the progress to Git, the agent **MUST STOP and wait for explicit user review and approval**.
- Proceeding automatically to the next step without user consent is strictly prohibited. Every step requires a dedicated checkpoint for review, artifact inspection, and alignment.

---

# The Definition of Done (DoD) Mechanism

The DoD mechanism is strictly objective. A step is never done because it "looks right," "seems finished," or "works properly." It is done when a machine says it is done.

## 1. The Gate Script
- A step is considered DONE if and only if its verification gate exits zero (e.g., running `./scripts/verify.sh P3-S2`). If the script fails, the step is not done.

## 2. Cumulative Verification
- The gate does not just run tests for the current step. It runs the tests for the current step plus the tests for every prior step. This guarantees that a new step can never silently break an older one.

## 3. Strictly Machine-Checkable
Every single DoD item in the plan must fall into one of exactly three permitted, falsifiable forms:
1. **File:** A file exists at path X with property Y.
2. **Command:** A specific command runs and produces output Y or exits zero.
3. **Test:** A specifically named test passes (e.g., `tests/test_p3_s2.py::test_clean_case`).

## 4. Banned Subjectivity & Verification
- Requirements phrased as "works correctly," "is implemented," or "handles X properly" are strictly prohibited as DoD items.
- **Trust but Verify:** If a previous session marks a step as DONE in the status board, the next session must always run the gate for that step (`./scripts/verify.sh <LAST_DONE_STEP_ID>`). If it fails, the status must be corrected before new work begins.
