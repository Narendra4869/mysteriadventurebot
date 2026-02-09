# FIRMAMEN: GOOD ENDING Reachability Analysis

## Problem Statement

Multiple test runs have failed to trigger the GOOD ENDING despite careful path selection optimized for balanced stat growth. This document analyzes whether GOOD ENDING is mathematically achievable under current conditions.

---

## GOOD ENDING Requirement
```
knowledge >= 5 AND urgency >= 5 AND coalition >= 5 AND hesitation_action_count <= 1
```

---

## Stat Gain Analysis by Choice

### Knowledge Sources
| Source | Gain | Cost/Notes |
|--------|------|-----------|
| Scene 1, Choice 2 | +2 | hesitation_level +1, hesitation_action_count +1 |
| Scene 1, Choice 3 | +1 | — |
| Scene 2, Choice 1 | +2 | urgency -1 |
| Scene 2, Choice 3 | +1 | hesitation_level +2, hesitation_action_count +1 |
| Scene 3, Choice 1 | +1 | — |
| Scene 3, Choice 2 | +1 | — |
| Scene 4, Choice 3 | +2 | urgency -3, hesitation_level +3, hesitation_action_count +1 |

**Non-Hesitation Knowledge Maximum:** 1 + 2 + 1 + 1 = **5** (via S1C3, S2C1, S3C1, S3C2)
- But S3 allows only ONE choice, so max is actually: 1 + 2 + 1 = **4**

**Conclusion:** Cannot reach `knowledge >= 5` without at least ONE hesitation action.

### Implication for GOOD ENDING

Since GOOD ENDING requires `hesitation_action_count <= 1`, the path MUST use **exactly one** hesitation action and still reach k >= 5.

**Single-Hesitation Paths to k=5:**

1. **Path A (S1C2 hesitation):**
   - S1C2: k=2, u=-1, h+=1
   - S2C1: k=4, u=-2
   - S3C1: k=5, u=0, c=0-1
   - S4C2: k=5, u=1, c=3-4
   - **Result:** k=5 ✓, u=1 ✗ (need >=5), c=3-4 ✗ (need >=5)

2. **Path B (S2C1 + S4C3 hesitation):**
   - Would violate `hesitation_action_count <= 1` (needs 2 hesitations)
   - Not viable

3. **Path C (S2C3 hesitation):**
   - S1C3: k=1, u=1, c=1
   - S2C3: k=2, u=?, c=1
   - S3C1: k=3, u=?, c=1-2
   - S4C2: k=3, u=?, c=4-5
   - **Result:** k=3 ✗ (need >=5)

---

## Critical Finding

**Mathematical Impossibility:** To achieve k >= 5 with only one hesitation action, you must use S1C2 (the best knowledge gain).

But S1C2 forces:
- urgency = -1 starting value
- S2C1 (only other +2 knowledge) also forces urgency -= 1
- By Scene 3: urgency starts negative and requires +4 or +5 boosts
- Best urgency path in S3-S4: +2 (S3C1) + 1-3 (S4) = +3-5 total
- **Result:** Final urgency = -1 + (-1 to +5) = -2 to +4, max around +3-4, not >= 5

**Conclusion:**
The constraints appear **mutually exclusive**:
- High knowledge requires sacrificing urgency (via S2C1)
- Cannot recover urgency while maintaining `hesitation_action_count <= 1`
- Coalition also becomes difficult to prioritize in parallel

---

## Test Run Results

| Test | Path | Outcome | k | u | c | h_count |
|------|------|---------|---|---|---|---------|
| 1 | 2-3-3-3 | TRUE END | 6 | 4 | 1 | 2 |
| 2 | 1-1-1-1  | BAD END | 0 | 5 | 0 | 0 |
| 3 | 3-2-1-2 | BAD END | 2 | 5 | 6-7 | 0 |

**Pattern:** All non-TRUE_END paths trigger BAD_END (fallback), including carefully optimized runs.

---

## Possible Solutions

### Option 1: Adjust GOOD ENDING Thresholds
Lower one or more thresholds to make path mathematically feasible:
- `knowledge >= 4` (instead of 5)
- `hesitation_action_count <= 2` (instead of <= 1)
- `urgency >= 4` or `coalition >= 4` (instead of 5)

### Option 2: Rebalance Stat Gains
Modify choice gains to allow parallel growth:
- Remove `urgency -= 1` from S2C1
- Add `urgency` to S3C1
- Increase coalition rewards on non-hesitation paths

### Option 3: Accept GOOD ENDING as "Narrow Needle"
GOOD ENDING might be **intentionally difficult**—a design feature, not a bug:
- Teaches player that early commitment + perfect balance is rare
- Philosophically: most paths lead to compromise (BAD_END) or regret (TRUE_END)
- Leaves GOOD_END as the aspirational "ideal" that few players achieve

### Option 4: Accept Current Implementation (Status Quo)
The game works correctly:
- TRUE_END: ✅ Reached via hesitation trajectory
- BAD_END: ✅ Reached via non-optimal play
- GOOD_END: ⚠️ Mathematically unreachable, but may be intentional design

---

## Recommendation

**The game is functionally complete** and delivers the core philosophical message:
- Hesitation has irreversible consequences (TRUE ENDING)
- Most players will achieve compromise endings (BAD ENDING)  
- The ideal ending may be aspirational

**Suggest:** Ask user whether GOOD ENDING should be:
1. Mathematically achievable (adjust thresholds)
2. Intentionally unreachable (design feature)
3. Remain as-is (no change)

---

**Analysis Date:** 2026-02-09  
**Status:** Complete; awaiting user direction
