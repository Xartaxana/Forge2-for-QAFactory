# Testing rules of forge 2

Card C1-6 (amended by B8). Rule text for workers; each rule is stated once.

1. What is tested. Tool code only: files under `forge/tools/`, `forge/hooks/`, `factory/tools/`, `measure/tools/`. Rule
   text, documents and config have no test; they are judged by their card's keys.
2. Layers. Two, no third: stories run on real run artifacts once such artifacts exist, and data joints (one data file
   read against the file or tool that consumes it). A test outside these layers is not written.
3. One parameterised table per behaviour. A new case is a row of an existing table; a new test file only where the
   card's `test:` line places it.
4. `expected from:` names where the expected value came from, and only three sources are legal: the spec (a card line
   or an edge), a rule (a line of this file or of the rules), or
   the owner's word, quoted with its carrier (a `W-` record once B3's registry exists). The output of the
   code under test is never a source: a value copied from a run of the code proves nothing.
5. Volume. A branch carries no more test lines than code lines; a row that does not fit is reported as not written,
   never squeezed in. A new test file runs in at most 10 seconds.
6. CI canon. The whole canon runs within one hour. The job list is `forge/ci-jobs.json` and nowhere else: neither
   `.github/workflows/ci.yml` nor `forge/tools/ci.py` holds a job id or command. A job's row carries `state`: `built`
   or `not_built`; a `not_built` row is a named state (its tool does not exist, so it is not run, never shown as green, listed with its count), and the
   `not_built` set only shrinks (a new job enters `built`; `ci.py check --base <ref>` refuses growth).
7. Pre-push `ci.py` is the early net; Actions is the judge. A job that exits 3 (part not judged here) passes locally
   with `not judged here: <job>` and is red on Actions. `all-green` is the only required check.
8. The `tests` job stays `not_built` until the first file under
   `forge/tests/` lands.
