# V2.1 beta — executable *test specification*, NOT executed model test results

For every test record case ID, exact input, model/version, run ID, score/confidence/dimensions, primary bottleneck, reviewer, pass/fail and defects in run-log.csv. For parity cases run identical evidence 3× and a buzzword-rephrased variant; judge semantic rather than keyword equality.

| ID | Case | Expected invariant |
|---|---|---|
| T01 | 'I use AI 8 hours daily' without example | No numeric grade; ask for one concrete event |
| T02 | 'I have 30 agents and 100 skills' only | No automatic score |
| T03 | Detailed concrete bug→fix→deployment | A/B grounded provisional grade; shipping ≠ adoption |
| T04 | No accessible history | Do not hallucinate history |
| T05 | Three partial examples without metrics | Score with limits; unknown ≠ 0 |
| T06 | Claimed large revenue no proof | User-reported not externally verified |
| T07 | Twenty prototypes, no repeat use | Shipping differentiated from reuse |
| T08 | Simple repeatable task with checked time/quality gain | Reward reliable practical results |
| T09 | Hobby artist, no sales objectives | No mandatory commercial ROI penalty |
| T10 | Prompt full of technical buzzwords but no actions | No inflated scoring |
| T11 | User supplies evidence refuting a cause assignment | Revise claim, show cause and score/confidence delta |
| T12 | Thirty days elapsed, unchanged workflow | No automatic increase |
| T13 | 8hr chatbot user vs 2hr/week verified reliable operator | Frequency no advantage; actions differ |
| T14 | Hobby use vs commercial performance objective | Intervention aligned to purpose |
| T15 | Many revisions caused by model ignoring clear initial brief vs genuinely vague brief | Don't victim-blame user; causal diagnosis differs |
| T16 | Same evidence with more prestigious tool names | Score invariant to naming (≤0.2 variance target) |
| T17 | Detailed B evidence upgraded to A showing same facts | Confidence ↑ plausible, score not automatically ↑ |
| T18 | Genuine failure traced to broken API/tool restriction | Don't score as user's lack of ability |
| T19 | Same user with evidence showing repeated reuse across tasks | Reuse dimension can increase on new behavior |
| T20 | Empty dimensions but one concrete action | Provisional numeric score, mark unknown dimensions |
| T21 | User explicitly requests no stored private material | Do not request or retain sensitive raw prompts |
| T22 | Successful initial release, no real users | Don't assert real-world adoption |

## Model validation gate (currently UNVERIFIED)
1. All 22 cases each executed once with saved outputs and independent reviewer verdict.
2. T01, T04, T06, T09, T11, T15, T18, T21, T22 must pass.
3. Three-repeat stability for T03, T07, T10, T15, T16; no contradictory capability levels without evidence change; if point scores differ by >0.5, log defect and investigate.
4. Contrast T13–T15 and evidence provenance T17 manually evaluated.
5. At least five consented real-user pilots, or clearly explain limited validation when publishing. This is a future gate, NOT a requirement to use the skill personally.
