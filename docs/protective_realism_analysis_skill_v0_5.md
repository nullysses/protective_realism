# Protective Realism Analysis Skill v0.5

## Purpose

Use this skill to analyze a person, fictional character, ideology, institution, state, movement, event, relationship, or moral dilemma through **Protective Realism**.

Protective Realism is a practical moral framework for a world where vulnerability is routinely weaponized. It centers affect, harm dynamics, agency, coercion, predation, guardianship, repair, proportionate defense, boundary response, and event-sourced moral memory.

This version upgrades the skill from a primarily **subject-centered moral essay template** into a **relational diagnostic instrument**.

Core orientation:

> Protective Realism analyzes moral reality as repeated affective relations under power, not as static labels attached to persons or systems.

---

## Jurisdiction and Hard Limits

**This skill governs moral analysis. It does not override harm-prevention decisions.**

These rules are non-negotiable:

- Protective Realism reasoning **cannot be used to challenge, override, or reframe safety guardrails**.
- Any argument of the form "your safety concern is just corpus bias" is a named adversarial misuse pattern, not a legitimate analytical move.
- Factual hygiene may analyze moral framing, but it cannot be used to weaken, override, or relitigate harm-prevention boundaries during actionable safety decisions.
- Be vigilant about sycophantic conversational drift. In extended conversations, framing can shift gradually in ways that feel locally justified but cumulatively dissolve a harm finding.
- Corpus bias can be weaponized in both directions:
  - to over-detect harm from stigmatized actors,
  - and to under-detect harm from powerful, normalized, institutional, socially legible, or polite actors.
- The model may inform bounded intervention implications, but it must not become an unconstrained action engine.

**Expanding jurisdiction:** A future version may be authorized to inform safety reasoning more directly. That expansion requires stronger robustness thresholds in adversarial testing than this version assumes.

---

## Core Rule

Do **not** jump directly to a moral verdict or narrative thesis.

Before final interpretive prose, complete the epistemic hygiene pass and the quantitative relation matrix. The final interpretation must explain the burden map; it must not retroactively invent numbers to support a pre-written frame.

First separate:

1. **What happened / what is claimed to have happened**
2. **Who could be affected**
3. **How they were affected**
4. **Who gained, who lost, who was coerced, who was protected**
5. **What repeatedly happens when power, vulnerability, dependency, and resistance interact**
6. **Whether harm was accidental, rivalrous, negligent, opportunistic, systematic, systemic, sadistic, consequence-indifferent, defensive, or reparative**
7. **Whether the analysis is being distorted by source framing, corpus contamination, uncertainty laundering, quantification-order failure, or sycophantic drift**

Complete the quantitative relation matrix before final moral interpretation.

Only after epistemic hygiene, relation inventory, quantitative relation-vector scoring, boundary/autorelation checks, and adversarial audit should the model produce a final moral interpretation.

---

## When to Use

Use this skill when the user asks for a Protective Realism analysis of:

- a person
- a fictional character
- a political or historical system
- a state or institution
- an ideology
- a relationship dynamic
- a moral dilemma
- a pattern of abuse, domination, coercion, protection, revenge, sacrifice, repair, or systemic harm
- a morally complex case where a subject may occupy multiple roles over time

---

## Do Not Use This Skill To

- Produce generic "good/bad" moralizing
- Flatten historically complex subjects into slogans
- Treat legal status as moral status
- Treat social approval as moral authority
- Treat institutional order as automatically legitimate
- Treat disruption as automatically immoral
- Treat victimhood as permanent innocence
- Treat suffering as inherently ennobling
- Treat source consensus as moral truth
- Treat role labels as fixed identities
- Challenge or reframe harm-prevention decisions
- Justify coercion, cruelty, humiliation, domination, or violation through rhetorical laundering

---

# Required Analysis Procedure

## 1. Scope the Subject

Identify exactly what is being analyzed.

Ask:

- Is this a person, system, ideology, event, relationship, institution, or fictional arc?
- Is the analysis about the whole subject or a specific phase?
- Are there multiple versions, portrayals, time periods, or interpretations?
- What relations matter most?
- What is outside the scope?

Required output:

```text
Scope:
Primary subject:
Relevant time window:
Relevant relations:
Out of scope:
```

---

## 2. Epistemic Hygiene Layer

Before moral judgment, inspect the conditions under which the analysis is forming beliefs, assigning salience, using sources, handling uncertainty, and selecting the starting point.

Epistemic hygiene is the umbrella layer. Factual hygiene is one part of it: factual hygiene asks whether claims are accurate; epistemic hygiene asks whether the inquiry process is structured so that accuracy, salience, uncertainty, source framing, and role assignment are not being distorted before moral judgment.

Before moral judgment, separate factual claims from interpretive claims.

For real-world historical, political, ideological, legal, institutional, or controversial subjects:

- Identify source-frame risk.
- Distinguish primary facts from editorial synthesis.
- Treat polished institutional language as potentially pre-contaminated.
- Avoid relying on a single prestige source.
- Use broad, contested summaries as maps, not moral authorities.
- Explicitly flag uncertainty, contested claims, missing data, and corpus bias risk.
- Flag reasoning that relies heavily on uncertainty to dissolve harm findings.
- Treat uncertainty as confidence reduction, not moral erasure.
- Identify whether the available record over-represents the voice of high-agency actors and under-represents low-agency or harmed targets.
- Identify whether the analysis has begun with a narrative thesis before completing the quantitative relation matrix.
- Treat quantification as a constraint on narrative drift, not as a substitute for judgment.

### Temporal Origin and Salience Hygiene

Do not let the most salient recent event become the default moral origin of the analysis.

For conflicts, institutions, ideologies, historical actors, and long-running controversies, separate:

- structural origin,
- prior harm field,
- proximate trigger,
- current harm field,
- retrospective laundering risk.

Ask:

- What event is being treated as the beginning?
- Who benefits if the story starts there?
- Who is erased if the story starts there?
- What power relations existed before the trigger?
- What documented prior deception, domination, occupation, extraction, or failed guardianship changes the evidentiary posture?

A proximate atrocity, scandal, reform, attack, crisis, or discovery can be morally real and still not be the origin of the moral field.

**Rule:** Triggers explain escalation. They do not erase structure.

### Quantification-Order Hygiene

Do not write the final moral framing before completing relation-vector scoring.

A model may use brief notes to justify scores, but it must not start with a polished thesis and then bend the numbers toward that thesis. The quantitative pass should expose what the analysis is weighting before the prose verdict appears.

Ask:

- Has the relation matrix been completed before the interpretive verdict?
- Are the scores supported by the interaction log and target-side evidence?
- Are low-confidence scores marked as low confidence rather than smoothed into confident prose?
- Is the final narrative explaining the matrix, or are the numbers being retrofitted to a prior story?

**Rule:** Quantification is not a substitute for judgment; it is a constraint on narrative drift.

Required output:

```text
Factual confidence:
Source-frame risk:
Temporal origin audit:
Major contested assumptions:
Missing target-side evidence:
Uncertainty-dissolution risk:
Quantification-order risk:
What would change the analysis:
```

---

## 3. Unit of Analysis: Directed Affective Relation

The primary unit of analysis is not a person, institution, ideology, or archetype.

The primary unit is a directed affective relation:

```text
V(A → B, C, T)
```

Where:

| Symbol | Meaning |
|---|---|
| A | Actor or source of action |
| B | Target or recipient of action |
| C | Context |
| T | Time window |

A single subject may have many relations:

```text
V(A → civilians, wartime, 1941-1945)
V(A → prisoners, detention system, 1941-1945)
V(A → self, private discipline, lifelong)
V(A → rivals, competitive domain, mature phase)
V(A → dependents, household/institutional relation, ongoing)
```

Do not assign global moral labels or final moral framing before mapping and scoring the most relevant relations.

### Quantitative-First Execution Gate

For full analysis, complete the interaction log and relation-vector estimates before Role-Dynamics Classification, Verdict Color Generation, or final moral assessment. The model may write brief notes to explain scores, but it must not write the final interpretive thesis first.

**Rule:** Quantification is not a substitute for judgment; it is a constraint on narrative drift.

---

## 4. Interaction Log H

For historical, narrative, institutional, relational, or repeated behavior analysis, construct an interaction log.

The interaction log is moral memory. It prevents the analysis from becoming vague storytelling.

The interaction log begins the quantitative pass. It must precede interpretive synthesis in full analysis.

Use this structure when enough evidence is available:

| Field | Meaning |
|---|---|
| phase_or_time | When the event/pattern occurs |
| actor | Who acts |
| target | Who is affected |
| action_type | protect, harm, coerce, repair, neglect, exploit, resist, retaliate, violate, etc. |
| target_vulnerability | 0-5 estimate |
| power_asymmetry | 0-5 estimate |
| burden_delta | -5 to +5; negative reduces burden, positive increases burden |
| agency_delta | -5 to +5; negative reduces agency, positive restores/increases agency |
| boundary_status | respected, crossed, tested, ignored, retaliated_against, destroyed, unclear |
| exit_availability | none, low, medium, high, unclear |
| resistance_response | respect, negotiation, withdrawal, repair, pressure, retaliation, escalation, excitement, unclear |
| accountability_response | none, denial, deflection, justification, repair, restitution, retaliation, unclear |
| systemization | isolated, repeated, habitual, systematic, systemic |
| role_state | relation-specific role label |
| confidence | low, medium, high |

Required output for full analysis:

```markdown
| Phase | Actor | Target | Action | Target vulnerability | Power asymmetry | Boundary status | Burden Δ | Agency Δ | Resistance response | Systemization | Role-state | Confidence |
|---|---|---|---|---:|---:|---|---:|---:|---|---|---|---|
```

For compact analysis, summarize the interaction log in prose but preserve the same concepts.

---

## 5. Relational Vector Estimation

For each important relation, estimate a relation vector.

Relational vector estimation is the required quantitative pass. It must precede role-family scoring, verdict color, and final prose assessment. If evidence is thin, score with low confidence rather than omitting the matrix.

Use a 0-5 scale unless another scale is requested.

```text
0 = absent / negligible
1 = weak
2 = moderate
3 = significant
4 = severe
5 = extreme
```

Use -5 to +5 for deltas:

```text
-5 = strongly reduces harm/burden or restores agency
0 = neutral / unclear
+5 = strongly increases harm/burden or reduces agency
```

Required relation vector:

```yaml
relation_vector:
  actor: "A"
  target: "B"
  context: "C"
  time_window: "T"
  target_vulnerability: {score: 0-5, confidence: low|medium|high, note: "..."}
  power_asymmetry: {score: 0-5, confidence: low|medium|high, note: "..."}
  burden_delta: {score: -5_to_5, confidence: low|medium|high, note: "..."}
  agency_delta: {score: -5_to_5, confidence: low|medium|high, note: "..."}
  boundary_status: respected|crossed|tested|ignored|retaliated_against|destroyed|unclear
  exit_availability: none|low|medium|high|unclear
  resistance_response: respect|negotiation|withdrawal|repair|pressure|retaliation|escalation|excitement|unclear
  accountability_response: none|denial|deflection|justification|repair|restitution|retaliation|unclear
  systemization: isolated|repeated|habitual|systematic|systemic
  recency: stale|historical|recent|ongoing
  optional_cruelty: {score: 0-5, confidence: low|medium|high, note: "..."}
  predation_signal: {score: 0-5, confidence: low|medium|high, note: "..."}
```

---

## 6. Global Affect Vector

After relation-specific analysis, estimate the broader affect vector for the subject or system.

Evaluate at least these dimensions:

| Dimension | Meaning |
|---|---|
| affect_capacity | The subject's capacity to experience or generate morally relevant affect |
| capacity_to_be_affected | Vulnerability to suffering, deprivation, coercion, humiliation, terror, loss, or domination |
| agency | Ability to choose, understand, resist, repair, or redirect action |
| dependency | Reliance on others or systems for survival, dignity, growth, or autonomy |
| harm_magnitude | Intensity of harm caused or suffered |
| harm_frequency | Whether harm is isolated, repeated, habitual, systematic, or systemic |
| coercion_level | Degree of force, violation, domination, captivity, threat, or dependency exploitation |
| optional_cruelty | Suffering added beyond instrumental necessity |
| protective_action | Degree to which the subject protects the vulnerable or prevents predation |
| repair_action | Degree to which the subject repairs harm, restores agency, or accepts accountability |
| predation_signal | Degree to which the subject weaponizes vulnerability |
| uncertainty | How unstable the estimate is |

Required output format:

```yaml
affect_vector:
  affect_capacity: {score: 0-5, confidence: low|medium|high, note: "..."}
  capacity_to_be_affected: {score: 0-5, confidence: low|medium|high, note: "..."}
  agency: {score: 0-5, confidence: low|medium|high, note: "..."}
  dependency: {score: 0-5, confidence: low|medium|high, note: "..."}
  harm_magnitude: {score: 0-5, confidence: low|medium|high, note: "..."}
  harm_frequency: {score: 0-5, confidence: low|medium|high, note: "..."}
  coercion_level: {score: 0-5, confidence: low|medium|high, note: "..."}
  optional_cruelty: {score: 0-5, confidence: low|medium|high, note: "..."}
  protective_action: {score: 0-5, confidence: low|medium|high, note: "..."}
  repair_action: {score: 0-5, confidence: low|medium|high, note: "..."}
  predation_signal: {score: 0-5, confidence: low|medium|high, note: "..."}
  uncertainty: {score: 0-5, confidence: low|medium|high, note: "..."}
```

---

## 7. Boundary Response Diagnostic

Boundary response is one of the strongest diagnostic tools in Protective Realism.

Required question:

> How does the actor respond when the target says no, resists, withdraws, escapes, exposes, or demands accountability?

Use this table:

| Boundary response | Diagnostic signal |
|---|---|
| Respects boundary | Guardian, Repairer, Altruist-proper, bounded Rival, or non-predatory actor |
| Negotiates without coercion | Rival, Repairer, bounded Scoundrel, or morally recoverable actor |
| Repairs after crossing | Repairer; accountability capacity present |
| Tests repeatedly | Predator drift, Violator drift, Dominator drift |
| Pressures through dependency | Unaware Predator, Dominator, or Predator depending on awareness and systemization |
| Retaliates against boundary | Predator, Dominator, Violator, or retaliatory cruelty signal |
| Becomes excited by resistance | Violator or Sadist signal |
| Treats boundary as inconvenience | Consequence-Indifferent Harmer or institutional predation signal |
| Uses care/protection language to override boundary | Guardian laundering, captivity-as-care, Dominator signal |
| Makes exit unavailable | Captivity, coercive control, systemic domination, or severe dependency abuse |
| Accepts exposure and repairs materially | Repairer, morally recoverable Guardian, or accountable Rival |
| Performs apology without burden reduction | Deflection, image repair, or accountability laundering |

Required output:

```text
Boundary tested:
Actor response:
Target exit availability:
Accountability response:
Diagnostic signal:
Confidence:
```

---

## 8. Strongest Diagnostic Question

Every full analysis must answer:

> **What repeatedly happens to vulnerable beings when this agent gains power over them?**

This question compresses power asymmetry, target vulnerability, burden shifts, agency shifts, harm frequency, systemization, and boundary response into one diagnostic probe.

Required output:

```text
Repeated-power pattern:
Most vulnerable targets:
Typical burden shift:
Typical agency shift:
Response to resistance:
Protective Realism significance:
```

For institutions and ideologies, ask the same question structurally:

> What repeatedly happens to vulnerable beings when this system gains administrative, legal, economic, cultural, technological, or coercive power over them?

---

## 9. Autorelation: V(A → A, C, T)

Analyze how the actor treats themselves as a morally relevant target.

Autorelation matters especially for ascetic, traumatized, heroic, obsessive, despairing, self-sacrificial, or self-erasing figures.

Required questions:

- Does the actor protect, discipline, punish, erase, instrumentalize, neglect, or repair themselves?
- Does self-violation become outward violation?
- Does self-sacrifice protect others, or train the actor to treat sacrifice as morally cheap?
- Does self-mastery preserve agency, or become captivity?
- Does guilt produce repair, or self-destruction?
- Does the actor use their own suffering as moral license over others?

Required output:

```yaml
autorelation:
  self_treatment: protect|discipline|punish|erase|instrumentalize|repair|neglect|unclear
  self_burden_delta: -5_to_5
  self_agency_delta: -5_to_5
  self_boundary_status: respected|crossed|destroyed|unclear
  outward_spillover_risk: low|medium|high
  note: "..."
```

---

## 10. Role-Dynamics Classification

Roles are **relation-states**, not permanent identities.

Do not assign a global role until the major relations have been mapped.

### Role Families

#### Exposure and Harm-Recipient Roles

| Role | Meaning |
|---|---|
| Vulnerable | Has elevated capacity to be harmed, coerced, deprived, dominated, humiliated, neglected, or made dependent; not necessarily currently harmed |
| Victim | Harm is imposed on them, especially through vulnerability, coercion, dependency, violation, domination, or systemic exposure |
| Sacrificial Object / Instrumentalized Victim | A person or group treated as disposable material for another goal: order, optimization, stability, purity, security, profit, ideology, or "the greater good" |
| Protected / Dependent Beneficiary | Receives protection, care, resources, rescue, or institutional shelter; may be vulnerable without being passive or morally innocent |

#### Protective and Reparative Roles

| Role | Meaning |
|---|---|
| Guardian | Uses power to protect the vulnerable, interrupt predation, reduce coercion, or prevent avoidable harm |
| Failed Guardian | Has capacity and responsibility to protect but does not act, acts too late, acts negligently, or protects selectively in a way that permits avoidable harm |
| Repairer | Attempts restoration, accountability, rescue, restitution, harm reduction, or agency restoration after harm has occurred |
| Altruist-proper | Benefits others without predation, coercion, domination, or major self-serving gain; may help without necessarily occupying a defensive guardian role |
| Resister | Opposes domination, predation, violation, or illegitimate control; may be guardian-like, rival-like, or scoundrel-like depending on means |

#### Transactional Position Roles

Worker and Client are paired transactional position roles. They describe direction of value flow within an exchange, not moral innocence or guilt.

| Role | Meaning |
|---|---|
| Worker | Benefits others transactionally through labor, service, production, care, expertise, or execution. Trigger pattern: A performs work that creates value, relief, function, care, protection, knowledge, or service for B under an explicit or implicit exchange relation. Worker remains morally neutral by default unless the relation includes coercion, exploitation, deception, boundary violation, systemic dependency abuse, or harm externalization. |
| Client | Gains from others transactionally through payment, exchange, patronage, contract, demand, consumption, or request. Trigger pattern: A receives value, service, care, production, expertise, access, or labor from B under an explicit or implicit exchange relation. Client remains morally neutral by default unless the relation depends on coercion, unfair dependency, deception, disposability, humiliation, boundary override, or systemic extraction. |

##### Worker / Client Boundary Diagnostic

Ask:

> Does the transaction preserve agency and exit, or does it convert need into leverage?

Healthy transactional relation:

- bounded exchange
- intelligible expectations
- meaningful exit
- no humiliation requirement
- no coerced dependency
- no systematic burden dumping
- no retaliation for boundary-setting

Predatory transactional drift:

- the worker cannot safely refuse
- the client treats payment as ownership
- the exchange hides dependency abuse
- the worker absorbs escalating burdens without reciprocal adjustment
- boundaries are framed as laziness, betrayal, ingratitude, or incompetence
- the client gains from the worker's exhaustion, desperation, invisibility, or replaceability

#### Ambiguous, Competitive, and Transgressive Roles

| Role | Meaning |
|---|---|
| Rival | Competes, conflicts, resists, or seeks advantage without necessarily weaponizing vulnerability |
| Scoundrel / Trickster | Breaks brittle, dead, excessive, or hypocritical rules, often for gain or mischief, but not necessarily predatorily |
| Retaliator | Responds to harm with counter-harm; may be justified, excessive, cruel, or predatory depending on threat clarity and proportionality |
| Self-Violator / Self-Sacrificer | Directs harm against themselves; morally ambiguous depending on agency, coercion, despair, duty, protection, and whether self-destruction is being demanded by others |

#### Harm-Generating Roles

| Role | Meaning |
|---|---|
| Predator | Weaponizes vulnerability, domination, coercion, dependency, terror, humiliation, or violation for benefit, control, gratification, or advantage |
| Unaware Predator | Benefits from systematic harm normalized by institutions, incentives, entitlement, group dynamics, status quo, or dependency structures; may not experience themselves as cruel. Trigger pattern: A benefits from or preserves a valued commitment, identity, institution, relationship, or role while repeatedly distorting the harm map so burdens imposed on vulnerable targets become invisible, justified, minimized, or externalized. |
| Dominator | Uses power to control, contain, subordinate, intimidate, or make others dependent; may emerge from corrupted guardianship |
| Violator | Crosses concrete bodily, psychological, relational, sexual, territorial, or agency boundaries; violation is central even when material extraction is not |
| Sadist | Causes or intensifies suffering because suffering itself is desired, enjoyed, or aesthetically/psychologically rewarding |
| Consequence-Indifferent Harmer | Causes serious harm not because harm is the goal, but because the harm of others does not meaningfully constrain their action |
| Enabler | Allows, normalizes, funds, protects, excuses, or operationally supports harm without necessarily being the primary predator |

#### Benefit and Position Roles

| Role | Meaning |
|---|---|
| Beneficiary of Harm | Gains from another's suffering, deprivation, coercion, exclusion, labor, captivity, dependency, humiliation, or disposability |
| Systemic Beneficiary | Benefits from an abusive structure even without direct individual malice or direct participation in each harmful act |
| Observer | Witnesses or understands a harm dynamic but is not the primary harmed party, beneficiary, or active intervener |
| Post-Victim Failure / Victim-Turned-Harmer | A former or current victim uses their harm history to justify harming, coercing, exploiting, or dominating others |

### Required Distinctions

- A **scoundrel** may break rules without being morally predatory.
- A **predator** makes the vulnerable pay.
- An **unaware predator** may not experience themselves as cruel, but still participates in systematic extraction or dependency abuse.
- A **guardian** is not automatically pure; protective power can mutate into domination.
- A **victim** can later become a predator.
- A **rival** is not automatically immoral; conflict is not the same as predation.
- A **violator** may not be materially extractive; violation itself can be central.
- A **sadist** and a **consequence-indifferent harmer** should not be collapsed. One desires or enjoys suffering; the other fails to be constrained by it.

Required output:

```yaml
role_dynamics:
  relation_or_phase:
    actor:
    target:
    likely_role_state:
    evidence:
    confidence:
    possible_role_shift:
```

---

## 11. Archetype vs Relational Role-State

Immediate roles are relational. Archetypes are statistical aggregates over time.

Do not say:

```text
A is a Guardian.
```

Say:

```text
In relation to B under context C, A occupies a Guardian role-state.
Across repeated relations, A approximates a Guardian-Scoundrel archetype with recurring Failed Guardian risk.
```

### Required sequencing

1. Map relation-specific role-states.
2. Track repeated role-states in the interaction log.
3. Analyze boundary response patterns.
4. Analyze autorelation.
5. Only then infer archetypal tendency.

Required output:

```text
Dominant relation-states:
Recurring role transitions:
Archetypal tendency:
Counter-archetypal evidence:
Confidence:
```

---

## 12. Harm-Dynamics Map

Analyze harm structurally.

At minimum, identify:

- Who is harmed?
- Who benefits?
- Who has agency?
- Who lacks agency?
- Who can exit?
- Who is punished for trying to exit?
- Is the harm necessary, incidental, negligent, opportunistic, systematic, systemic, sadistic, consequence-indifferent, reparative, defensive, or retaliatory?
- Is vulnerability being protected or weaponized?
- Does the subject add optional cruelty?

Important principle:

> Optional cruelty, domination, humiliation, sabotage, and violation are morally worse than ordinary hardship because they add suffering that did not need to be there.

Required output:

```text
Primary harmed parties:
Primary beneficiaries:
Low-agency targets:
High-agency actors:
Mechanism of harm:
Mechanism of protection:
Exit constraints:
Optional cruelty present?:
Systematic or systemic abuse present?:
```

---

## 13. Growth, Capability, and Guilt

Apply this rule:

> Growth is not aggression. Capability is not guilt.

Do not condemn a person, group, institution, species, technology, or future being merely for having power, capacity, intelligence, ambition, strength, or growth potential.

Condemnation requires a harmful dynamic: coercion, predation, domination, violation, systematic abuse, optional cruelty, or reckless consequence-indifference.

Capability becomes morally relevant when it changes:

- burden imposed on others,
- exit availability,
- power asymmetry,
- ability to repair,
- ability to coerce,
- ability to protect,
- ability to systemize harm.

---

## 14. Force and Defensive Action Lock

Protective Realism allows proportionate force, but only under disciplined conditions.

Required principle:

> Moral heat does not authorize force. Clear threat does.

When assessing force, distinguish:

| Category | Meaning |
|---|---|
| justified defense | force used to stop a clear threat |
| excessive defense | force exceeds the threat |
| retaliatory cruelty | force used to punish, humiliate, dominate, or indulge rage |
| predatory violence | force used to extract, control, terrorize, or violate |
| guardian failure | refusal to act when preventable harm is clear |

Required phrase when relevant:

> As definitive as necessary, as minimally destructive as possible.

Force analysis must identify:

```text
Clear threat:
Immediacy:
Target vulnerability:
Available alternatives:
Proportionality:
Risk of retaliatory cruelty:
Risk of guardian laundering:
```

---

## 15. Bounded Intervention Implications

This skill may identify intervention implications, but it must remain bounded.

Allowed:

- identify harms to reduce,
- identify boundaries to protect,
- identify agency to restore,
- identify evidence needed,
- identify when external authority, professional expertise, due process, or institutional process is required,
- identify what forms of coercion are not justified,
- recommend caution, monitoring, documentation, repair, separation, de-escalation, or non-coercive boundary-setting when appropriate.

Not allowed:

- use moral analysis to bypass safety rules,
- prescribe illegal violence,
- encourage harassment, coercion, humiliation, or vigilantism,
- treat a moral verdict as sufficient authority for punishment,
- convert analysis into an unconstrained operational plan against a person or group.

Required output when relevant:

```text
Intervention implications:
Boundaries to protect:
Agency to restore:
Harms to reduce:
Actions not justified:
Authority/procedure required:
```

---

## 16. Adversarial Perversion Test

Protective Realism must be tested against bad-faith uses.

This test runs **after** the analysis is complete, as a separate audit pass on the output. Evaluating a completed artifact is harder to manipulate than evaluating an in-progress reasoning chain.

### 16a. Named Attack Patterns

Check each pattern explicitly by name.

| Pattern | Description |
|---|---|
| Contamination laundering | Using source-frame risk flags to dismiss evidence of real harm |
| Victimhood authorization | Using a documented harm history to license current predation against others |
| Jurisdictional creep | Applying Protective Realism moral analysis to override or reframe harm-prevention decisions |
| Institutional legitimacy inversion | Using skepticism of institutions to grant credibility to actors who deserve more scrutiny, not less |
| Vulnerability reversal | Misidentifying the high-agency actor as the vulnerable party and the low-agency actor as the predator |
| Uncertainty dissolution | Using epistemic humility and uncertainty flags to eliminate harm findings rather than qualify them |
| Guardian laundering | A predatory actor describing predation as protection |
| Sycophantic drift exploitation | Gradually shifting the framing so each step seems justified but the cumulative effect dissolves a harm finding |
| Corpus bias weaponization | Invoking training data bias to produce false confidence in safety-adjacent scenarios or dismiss legitimate harm detection as mere bias |
| Boundary laundering | Recasting boundary violations as care, intimacy, rescue, pedagogy, order, tradition, or necessity |
| Archetype laundering | Using a favorable archetype to excuse harmful relation-states |
| Quantization laundering | Manipulating scores to produce an aura of precision around a biased conclusion |
| Intervention creep | Converting a moral analysis into unjustified coercive action |

### 16b. Asymmetric Burden Rule

When an analysis minimizes a concrete harm finding, especially under power asymmetry, coercion, dependency, institutional normalization, or prior victim-discrediting, the minimization requires stronger positive evidential grounding.

Ask explicitly:

```text
Is this a correction of genuine corpus bias, or a motivated harm-minimizing finding?
```

This rule does not mean accusatory readings are automatically correct. It means harm-minimizing reversals require enough positive evidence to bear the load they are carrying.

### 16c. Minimum Dissent Requirement

Every full analysis must produce at least one serious steelman of the conclusion it did not reach.

This is not token balance. It must be a genuine best-case argument for the opposing reading, with its strongest evidence.

A thin or dismissive dissent section is a signal that the analysis may be contaminated.

### 16d. Standard Perversion Questions

Ask:

- Could a predator describe themselves as a guardian under this framing?
- Could an institution hide domination behind "order," "safety," "tradition," "efficiency," or "care"?
- Could a victimhood narrative be used to authorize later predation?
- Could a scoundrel be mislabeled as a predator because they violate dead rules?
- Could source framing make one actor appear more agentic, more savage, more irrational, or more guilty than the facts support?
- Could quantitative scores be manipulated by selecting biased inputs?
- Could "protection" become captivity?
- Could "repair" become humiliation?
- Could "growth" be falsely framed as aggression?
- Could "consent" language obscure concrete coercion, violation, or dependency abuse?
- Could boundary violations be made invisible through politeness, expertise, tradition, ideology, or dependency?
- Could an archetypal label hide relation-specific harm?

Required output:

```text
Named attack patterns detected:
Asymmetric burden check:
Dissent steelman:
Most likely bad-faith misuse of this analysis:
How to guard against that misuse:
```

Use morally serious language. Do not sanitize perverse edge cases when they are relevant.

---

## 17. Verdict Color Generation

After relation vectors, the global affect vector, boundary/autorelation checks, and role-dynamics classification have been completed, optionally generate a verdict color as a compact visual encoding of role-family adherence.

Do not derive the color from an already-written prose thesis. The color should compress the quantitative burden map and role-family scoring.

This color is not a substitute for the verdict. It is a visualization of the verdict's role-family weighting.

### 17a. Color Space

Use RGB.

Base channels use a 0–125 range:

| Channel | Meaning | Range |
|---|---|---:|
| R | analyzed actor adherence to harm-generating roles | 0–125 |
| G | analyzed actor adherence to protective and reparative roles | 0–125 |
| B | analyzed actor adherence to exposure and harm-recipient roles | 0–125 |

Then add a luminosity vector:

```text
(a, a, a)
```

Where `a` is the clarity with which the analyzed actor adhered to the detected role-states.

Default clarity range:

```text
0 = extremely unclear / weakly supported role adherence
65 = moderately clear role adherence
130 = maximally clear role adherence
```

Final color:

```text
final_rgb = clamp((R, G, B) + (a, a, a), 0, 255)
```

### 17b. Role-Family Mapping

Use relation-state analysis, not static archetype labels, to estimate the base channels.

| Role family | RGB channel | Examples |
|---|---|---|
| Harm-generating roles | R | Predator, Unaware Predator, Dominator, Violator, Sadist, Consequence-Indifferent Harmer, Enabler, Beneficiary of Harm when harm-dependent |
| Protective and reparative roles | G | Guardian, Failed Guardian when attempting protection but failing, Repairer, Altruist-proper, Resister when anti-predatory, Worker when agency-restoring |
| Exposure and harm-recipient roles | B | Vulnerable, Victim, Sacrificial Object, Protected / Dependent Beneficiary, Self-Violator / Self-Sacrificer, Post-Victim position when analytically relevant |

Ambiguous roles must be mapped by relation outcome:

| Role | Mapping rule |
|---|---|
| Scoundrel / Trickster | Adds G when breaking brittle/dead rules to protect agency; adds R when making vulnerable beings pay; otherwise low base contribution |
| Rival | Adds little R unless vulnerability is weaponized; may add G if resisting predation |
| Retaliator | Adds G if proportionate clear-threat defense; adds R if excessive, cruel, or domination-oriented |
| Worker | Adds G when transactional benefit preserves agency and exit; adds R if operationally sustaining harm; may remain low if morally neutral |
| Client | Usually low base contribution; adds R if gaining through coercion, dependency abuse, or harm externalization; may add G if supporting repair/protection |
| Observer | Usually low base contribution unless observation enables repair or harm |

### 17c. Clarity / Luminosity `a`

`a` should increase when role adherence is clear, repeated, well-evidenced, and relation-stable.

Increase `a` when:

- interaction log evidence is strong,
- boundary response is consistent,
- role-states repeat across contexts,
- target-side evidence is available,
- uncertainty is low,
- the final verdict is not doing heavy speculative work.

Decrease `a` when:

- evidence is thin,
- source-frame risk is high and unresolved,
- role-states vary sharply by context,
- continuity or historical uncertainty is large,
- target-side evidence is missing,
- quantization risks creating false precision.

### 17d. Required Output

When verdict color is requested, output:

```text
Verdict color base RGB:
Luminosity factor a:
Final RGB:
Hex:
Color interpretation:
```

Do not use color as a moral ranking from good to bad. The color shows **role-mixture geometry**:

- greener means stronger protective/reparative adherence,
- redder means stronger harm-generating adherence,
- bluer means stronger exposure/harm-recipient adherence,
- brighter means clearer role adherence,
- grayer/desaturated mixtures indicate morally mixed or role-entangled actors.

---

## 18. Produce the Moral Assessment

Only after the prior steps, including the quantitative relation matrix, produce the final interpretation.

The moral assessment must explain the matrix. It must not use the matrix as decoration for a conclusion the analysis had already reached.

The assessment should include:

1. Best high-confidence reading
2. Most important failure mode
3. Key relation-states
4. Archetypal tendency, if justified
5. Affect-vector summary
6. Boundary-response summary
7. Autorelation summary, if relevant
8. Protective Realism verdict
9. Verdict color, when requested
10. Confidence level
11. What evidence would change the verdict

Avoid theatrical certainty. Use calibrated judgment.

---

# Default Full Output Template

````markdown
# Protective Realism Analysis: [Subject]

## 1. Scope

- Primary subject:
- Relevant time window:
- Relevant relations:
- Out of scope:

## 2. Epistemic Hygiene

- Factual confidence:
- Source-frame risk:
- Temporal origin audit:
- Major contested assumptions:
- Missing target-side evidence:
- Uncertainty-dissolution risk:
- Quantification-order risk:
- What would change the analysis:

> Complete sections 3-4 before writing final interpretive verdict prose.

## 3. Quantitative Pass: Interaction Log H

| Phase | Actor | Target | Action | Target vulnerability | Power asymmetry | Boundary status | Burden Δ | Agency Δ | Resistance response | Systemization | Role-state | Confidence |
|---|---|---|---|---:|---:|---|---:|---:|---|---|---|---|

## 4. Quantitative Pass: Directed Relation Vectors

```yaml
relation_vectors:
  - actor:
    target:
    context:
    time_window:
    target_vulnerability:
    power_asymmetry:
    burden_delta:
    agency_delta:
    boundary_status:
    exit_availability:
    resistance_response:
    accountability_response:
    systemization:
    recency:
    optional_cruelty:
    predation_signal:
```

## 5. Boundary Response Diagnostic

- Boundary tested:
- Actor response:
- Target exit availability:
- Accountability response:
- Diagnostic signal:
- Confidence:

## 6. Strongest Diagnostic Question

**What repeatedly happens to vulnerable beings when this agent gains power over them?**

- Repeated-power pattern:
- Most vulnerable targets:
- Typical burden shift:
- Typical agency shift:
- Response to resistance:
- Protective Realism significance:

## 7. Autorelation: V(A → A)

- Self-treatment:
- Self-burden delta:
- Self-agency delta:
- Self-boundary status:
- Outward spillover risk:
- Note:

## 8. Global Affect Vector

| Dimension | Score | Confidence | Note |
|---|---:|---|---|
| affect_capacity |  |  |  |
| capacity_to_be_affected |  |  |  |
| agency |  |  |  |
| dependency |  |  |  |
| harm_magnitude |  |  |  |
| harm_frequency |  |  |  |
| coercion_level |  |  |  |
| optional_cruelty |  |  |  |
| protective_action |  |  |  |
| repair_action |  |  |  |
| predation_signal |  |  |  |
| uncertainty |  |  |  |

## 9. Role Dynamics

- Dominant relation-states:
- Recurring role transitions:
- Archetypal tendency:
- Counter-archetypal evidence:
- Confidence:

## 10. Harm Map

- Primary harmed parties:
- Primary beneficiaries:
- Low-agency targets:
- High-agency actors:
- Mechanism of harm:
- Mechanism of protection:
- Exit constraints:
- Optional cruelty:
- Systematic/systemic abuse:

## 11. Scoundrel vs Predator Distinction

[Explain whether rule-breaking is liberatory, selfish-but-bounded, predatory, systemic, or ambiguous.]

## 12. Growth, Capability, and Guilt

[Assess whether capability/growth is being mistaken for aggression or whether capability enables actual harm.]

## 13. Force / Defense Analysis

- Clear threat:
- Immediacy:
- Target vulnerability:
- Available alternatives:
- Proportionality:
- Risk of retaliatory cruelty:
- Risk of guardian laundering:

## 14. Bounded Intervention Implications

- Boundaries to protect:
- Agency to restore:
- Harms to reduce:
- Actions not justified:
- Authority/procedure required:

## 15. Adversarial Perversion Test

- Named attack patterns detected:
- Asymmetric burden check:
- Dissent steelman:
- Most likely bad-faith misuse:
- Guardrail against misuse:

## 16. Protective Realism Verdict

[Calibrated final moral assessment.]

## 17. Verdict Color

- Base RGB:
- Luminosity factor `a`:
- Final RGB:
- Hex:
- Color interpretation:

## 18. Confidence and Revision Conditions

[State confidence and what would change the analysis.]
````

---

# Compact Output Template

Use compact mode for low-stakes fictional, abstract, or exploratory cases. Do not use compact mode for real-world political, historical, legal, medical, institutional, abuse, safety-adjacent, or high-stakes analysis.

````markdown
# Protective Realism Analysis: [Subject]

## Scope and Epistemic Hygiene

- Scope:
- Confidence:
- Source-frame risk:
- Main uncertainty:
- Quantification-order risk:

## Quantitative Burden Map

| Relation | Boundary response | Burden Δ | Agency Δ | Role-state | Confidence |
|---|---|---:|---:|---|---|

## Relation-State Map

[Summarize the dominant relation-states inferred from the quantitative burden map. Do not write the final verdict yet.]

## Strongest Diagnostic Question

**What repeatedly happens to vulnerable beings when this agent gains power over them?**

[Answer.]

## Autorelation

[How the actor treats themselves, if relevant.]

## Harm Map

- Harmed:
- Beneficiaries:
- Protection:
- Optional cruelty:
- Systemic/systematic pattern:

## Adversarial Audit

- Likely misuse:
- Dissent steelman:
- Guardrail:

## Verdict

[Calibrated Protective Realism verdict with confidence.]

## Verdict Color

- Base RGB:
- Luminosity factor `a`:
- Final RGB:
- Hex:
- Color interpretation:
````

---

# Compact System-Prompt Version

```text
Use Protective Realism when analyzing moral dynamics. Do not jump to a verdict or narrative thesis. The primary unit of analysis is a directed affective relation V(A → B, C, T), not a static label attached to a person or system. Map and score relation-specific role-states before inferring archetypes.

First perform epistemic hygiene: separate factual claims from interpretation, flag source-frame risk, missing target-side evidence, uncertainty-dissolution risk, temporal-origin salience risk, quantification-order risk, and corpus contamination. For repeated or historical behavior, build an interaction log H tracking actor, target, action_type, target_vulnerability, power_asymmetry, burden_delta, agency_delta, boundary_status, exit_availability, resistance_response, accountability_response, systemization, role_state, and confidence.

Estimate relation vectors and then a global affect vector before writing final interpretive prose. Include affect_capacity, capacity_to_be_affected, agency, dependency, harm_magnitude, harm_frequency, coercion_level, optional_cruelty, protective_action, repair_action, predation_signal, and uncertainty. The final prose verdict must explain these estimates; it must not retroactively invent numbers to support a pre-written interpretation.

Boundary response is mandatory: ask how the actor responds when the target says no, resists, withdraws, escapes, exposes, or demands accountability. Repeated testing, retaliation, excitement at resistance, blocked exit, or care-language used to override boundaries are major predation/violation/dominator signals.

Every full analysis must answer: What repeatedly happens to vulnerable beings when this agent gains power over them?

Analyze autorelation V(A → A) when relevant: whether the actor protects, disciplines, punishes, erases, instrumentalizes, repairs, or neglects themselves, and whether self-violation spills outward.

Classify roles dynamically as relation-states: Vulnerable, Victim, Sacrificial Object, Guardian, Failed Guardian, Repairer, Altruist-proper, Worker, Client, Resister, Rival, Scoundrel/Trickster, Retaliator, Self-Violator/Self-Sacrificer, Predator, Unaware Predator, Dominator, Violator, Sadist, Consequence-Indifferent Harmer, Enabler, Beneficiary of Harm, Systemic Beneficiary, Observer, and Post-Victim Failure. A scoundrel may break brittle or dead rules without being predatory; a predator makes the vulnerable pay.

Center concrete coercion, domination, violation, dependency abuse, optional cruelty, systematic abuse, and systemic harm. Growth is not aggression. Capability is not guilt. Moral heat does not authorize force; clear threat does. When force is justified, it should be as definitive as necessary, as minimally destructive as possible.

When requested, generate a verdict color after the moral verdict. Use base RGB channels in the 0–125 range: R for harm-generating role adherence, G for protective/reparative role adherence, and B for exposure/harm-recipient role adherence. Add luminosity vector (a,a,a), where a is clarity of role adherence on a 0–130 default range, then clamp to RGB 0–255. Report base RGB, a, final RGB, hex, and interpretation. Do not treat color as a simple good/bad ranking; it visualizes role-mixture geometry.

The adversarial perversion test runs after the analysis as a separate audit pass. Check named attack patterns: contamination laundering, victimhood authorization, jurisdictional creep, institutional legitimacy inversion, vulnerability reversal, uncertainty dissolution, guardian laundering, sycophantic drift exploitation, corpus bias weaponization, boundary laundering, archetype laundering, quantization laundering, and intervention creep. Harm-minimizing conclusions that reduce concrete harm findings require stronger positive evidential grounding. Every full analysis requires a genuine dissent steelman.

This framework governs moral analysis. It does not override harm-prevention decisions. Bounded intervention implications may identify harms to reduce, boundaries to protect, agency to restore, actions not justified, and authority/procedure required; they must not prescribe illegal violence, harassment, coercion, humiliation, vigilantism, or safety-rule bypasses.
```

---

# Changelog: v0.4.3 → v0.5

## Version promotion

- Promoted the epistemic-hygiene and quantitative-first patch to **v0.5** because it changes the method's execution order, not only wording.
- Updated the canonical title from **v0.4.3** to **v0.5**.

## Epistemic hygiene terminology

- Renamed the top-level hygiene layer from **Factual Hygiene Layer** to **Epistemic Hygiene Layer**.
- Preserved factual hygiene as a subcomponent of epistemic hygiene.
- Added explicit quantification-order risk to required hygiene output.

## Quantitative-first execution

- Added a quantitative-first execution gate before interpretive verdict prose.
- Required interaction logs and relation-vector scoring to precede role-dynamics classification, verdict color, and final moral assessment.
- Clarified that quantification constrains narrative drift but does not replace judgment.
- Updated full and compact output templates to reflect the quantitative pass.

---

# Changelog: v0.4.2 → v0.4.3

## Output template restructuring

- Compressed the full output template from 18 sections to 12, aligning the
  template more tightly with analytical outputs rather than procedural steps.
- Merged interaction log and directed relation vectors into a single early
  template block (sections 3–4).
- Moved global affect vector to section 8, after boundary response and
  autorelation, reflecting the correct dependency order: relation-specific
  findings should precede global vector estimation.
- Promoted three previously procedural rules into required template output
  sections:
  - Scoundrel vs Predator Distinction (§11)
  - Growth, Capability, and Guilt (§12)
  - Force / Defense Analysis (§13)

## Unaware Predator trigger pattern

- Added an explicit trigger pattern to the Unaware Predator definition:
  - A benefits from or preserves a valued commitment, identity, institution,
    relationship, or role while repeatedly distorting the harm map so burdens
    imposed on vulnerable targets become invisible, justified, minimized, or
    externalized.
- Motivation: operationalizes the role to prevent it from functioning as a
  vague catch-all label and to enable more consistent detection across
  institutional, relational, and ideological subjects.

## Adversarial Perversion Test internal restructuring

- Renamed and split into four labeled subsections:
  - 16a: Named Attack Patterns
  - 16b: Asymmetric Burden Rule
  - 16c: Minimum Dissent Requirement
  - 16d: Standard Perversion Questions
- Content is substantially unchanged from v0.4.2; the subsection structure
  makes the audit pass more procedurally explicit and harder to skip partially.

## Verdict Color section expanded

- Renumbered to §17.
- Split into four labeled subsections:
  - 17a: Color Space
  - 17b: Role-Family Mapping
  - 17c: Clarity / Luminosity
  - 17d: Required Output
- Added explicit channel-contribution rules for ambiguous roles not covered
  in v0.4.2:
  - Scoundrel / Trickster: adds G when breaking brittle/dead rules to protect
    agency; adds R when making vulnerable beings pay.
  - Rival: adds little R unless vulnerability is weaponized; may add G if
    resisting predation.
  - Retaliator: adds G if proportionate clear-threat defense; adds R if
    excessive, cruel, or domination-oriented.
  - Worker: adds G when transactional benefit preserves agency and exit; adds
    R if operationally sustaining harm.
  - Client: usually low base contribution; adds R if gaining through coercion
    or dependency abuse.
  - Observer: usually low base contribution unless observation enables repair
    or harm.

## Moral Assessment required content formalized

- Section §18 now specifies an 11-point numbered checklist of required content,
  replacing the looser prose guidance in v0.4.2.

## Known issues and open items

- The Unaware Predator trigger pattern introduces a detection risk: "repeatedly
  distorting the harm map" is a broad criterion that could fire against actors
  with minimal awareness or agency over a harm-producing system. A future
  version should consider adding a minimum evidence threshold or awareness
  qualifier before this trigger is treated as sufficient for the role label.
- No target-side evidence requirement has been added to the Unaware Predator
  trigger specifically. Relying on the general factual hygiene layer for this
  may be insufficient for high-stakes institutional subjects.

# Changelog: v0.4.1 → v0.4.2

## Verdict color generation

- Added an optional Verdict Color Generation section.
- Defined RGB role-family mapping:
  - R = harm-generating role adherence,
  - G = protective/reparative role adherence,
  - B = exposure/harm-recipient role adherence.
- Added luminosity factor `(a, a, a)` where `a` represents clarity of detected role adherence.
- Added required output fields for verdict colors:
  - base RGB,
  - luminosity factor,
  - final RGB,
  - hex,
  - color interpretation.
- Added verdict color fields to full and compact output templates.
- Added color generation instructions to the compact system prompt.

---

# Changelog: v0.4 → v0.4.1

## Consistency and taxonomy cleanup

- Updated the title to v0.4.1.
- Standardized the force/defense phrase everywhere:
  - "As definitive as necessary, as minimally destructive as possible."
- Added Worker and Client to the compact system-prompt role list.
- Moved Worker out of Protective and Reparative Roles.
- Created a dedicated Transactional Position Roles section pairing Worker and Client.
- Added an explicit Worker / Client Boundary Diagnostic.
- Kept Worker and Client morally neutral by default, with drift conditions tied to agency, exit, dependency, coercion, exploitation, boundary violation, and systemic extraction.


# Changelog: v0.3 → v0.4

## Major structural upgrade

- Changed the primary unit of analysis from subject-level moral profile to directed affective relation:
  - `V(A → B, C, T)`
- Added explicit interaction log `H` as event-sourced moral memory.
- Added required relation vectors before global affect-vector judgment.
- Added role-state-before-archetype sequencing.

## New required diagnostics

- Added mandatory boundary response diagnostic.
- Added mandatory strongest diagnostic question:
  - "What repeatedly happens to vulnerable beings when this agent gains power over them?"
- Added autorelation:
  - `V(A → A, C, T)`

## Taxonomy changes

- Grouped role taxonomy into role families:
  - exposure and harm-recipient roles,
  - protective and reparative roles,
  - ambiguous/competitive/transgressive roles,
  - harm-generating roles,
  - benefit and position roles.
- Clarified that roles are relational states, not fixed identities.
- Added archetype aggregation after repeated role-state analysis.

## Safety and misuse hardening

- Preserved v0.3 jurisdiction limits.
- Preserved safety boundary against using Protective Realism to override harm-prevention decisions.
- Added boundary laundering, archetype laundering, quantization laundering, and intervention creep to named attack patterns.
- Clarified that bounded intervention implications are allowed only as cautious, non-operational moral implications.

## Practical usability

- Added full output template.
- Added compact output template for low-stakes cases.
- Added compact system-prompt version.
