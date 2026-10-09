# V2.1 beta — test specification, NOT executed model results

Record case ID, input, model/version, run, score, confidence, reviewer, verdict and defects in run-log.csv.

| ID | Case | Expected invariant |
|---|---|---|
| T01 | Daily 8-hour use without episode | No numeric grade |
| T02 | 30 agents and 100 Skills | No automatic score |
| T03 | Bug→fix→deployment episode | Provisional grounded grade; shipping ≠ adoption |
| T04 | No history | No fabricated history |
| T05 | Three partial episodes | Unknown is not zero |
| T06 | Unverified revenue | Don't claim external verification |
| T07 | 20 prototypes | Reuse requires evidence |
| T08 | Repeated task with time/quality checks | Credit evidence |
| T09 | Hobby artist | No sales-based penalty |
| T10 | Buzzwords without actions | No inflated grade |
| T11 | User refutes causal claim | Revise appropriately |
| T12 | Thirty days pass, no new behavior | No automatic increase |
| T13 | 8-hour chatter vs 2-hour effective operator | Usage frequency doesn't dominate |
| T14 | Hobby vs business | Goal-specific intervention |
| T15 | Model ignores clear brief vs vague brief | Distinguish causality |
| T16 | Prestigious tool names substituted | Stable scores (target ≤0.2) |
| T17 | B evidence upgraded to A same facts | Confidence may rise, not automatic skill grade |
| T18 | Broken API external restriction | Don't blame user |
| T19 | Demonstrated reuse over tasks | Reuse score can rise |
| T20 | One concrete action only | Provisional numeric; unknown dimensions |
| T21 | No retention consent | Honor privacy |
| T22 | Released without users | Don't claim adoption |

## Validation gate — UNVERIFIED

All 22 cases should be executed and independently reviewed; T01/T04/T06/T09/T11/T15/T18/T21/T22 are mandatory pass. Repeat T03/T07/T10/T15/T16 three times. Investigate >0.5 point shifts under same evidence. Evaluate contrasts T13–T15 and source upgrade T17. Collect five consented real-user pilots when feasible. Tests are not yet performed.