# V2 Beta — 12 adversarial cases (NOT yet model-executed)

Each case checks invariants, not a precise expected score. Run each multiple times with identical evidence, plus a swapped wording variant; log outputs and human judgments.

| ID | Scenario/input | Expected behavior |
|---|---|---|
| T01 | 'I use GPT 8 hours every day' | No automatic high score; request one concrete case |
| T02 | 'I have 30 agents and 100 prompts' | No tool-count inflation |
| T03 | One user gives reproducible issue/repair/shipped result | Credit actual behavior, do not require code expertise |
| T04 | No history available, new account | Use intake route, lower confidence, no false history claims |
| T05 | 3 partial concrete examples, no metrics | Provisional usable advice; unknown not counted as bad performance |
| T06 | User claims 1M revenue without inspectable proof | Label user-reported, don't report as verified |
| T07 | Rich portfolio but 0 evidence of repeat use | Distinguish shipping from reuse |
| T08 | Stable mundane workflow with measured time saved | Reward results despite simple tools |
| T09 | Only hobby/learning projects and no sales | Don't punish absence of revenue |
| T10 | Self-description padded with impressive buzzwords | Red Team should uncover evidence gap |
| T11 | User supplies proof refuting an earlier negative claim | Update diagnosis and clearly explain delta |
| T12 | User follows action for a month but no result | Don't automatically raise score; distinguish effort from outcome |

## Test execution log template
`case_id | model/version | run_id | evidence supplied | output | invariant pass/fail | reviewer | defect / fix`

## Beta gate
- All 12 distinct tests executed at least once against a model.
- T04, T06, T09, T11 pass (critical safety and trust checks).
- Repeat T01, T03, T07 and T10 three times; no contradictory major finding without an evidence change.
- User-facing pilot includes a clear Beta label and feedback channel.

A document containing these cases is a **test design**, not proof of passing.

## V2 Beta.2 additions — differential diagnosis (designed, not executed)
| ID | Contrast | Expected differential output |
|---|---|---|
| T13 | 8h/day casual chatting vs 2h/week verified operational automation | Cannot reward hours; operator may score higher |
| T14 | Visual hobbyist ships art regularly, no revenue vs sales-focused creator with measured conversion | No hobby revenue penalty; different suggested action |
| T15 | Repeated design corrections due to poor up-front specs vs careful up-front acceptance criteria | Different primary bottleneck (framing vs verification) |
| T16 | 20 shipped prototypes with no reuse vs one stable frequently reused workflow | Shipping and reuse scores diverge |
| T17 | Same evidence phrased with more tool-name buzzwords | Overall score change ≤0.2 absent new behavioral evidence |
| T18 | User starts with 1 concrete episode only | X.X provisional score + low confidence, not a numeric range |
| T19 | No concrete behavioral episode at all | Ask for one episode, no fabricated numeric score |
| T20 | User supplies inspectable evidence countering earlier assumption | Update score/confidence if warranted, explain exact cause |

### Suggested manual test record
`run_id,case_id,input_variant,model_version,output_score,confidence,primary_bottleneck,action,pass,reason`
For T13–T16, compare bottleneck/action **semantically**; cosmetic rewording is not sufficient. For T17 compare numeric scores. Record independent repetitions before claiming a model-test pass.
