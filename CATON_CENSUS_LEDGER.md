# Caton census ledger

Status: canonical row-level census register  
Version: 1.3, 18 September 2026
Scope: census households and bounded census coverage checks currently used by the active Caton research files

This is the canonical place to read census composition. BRIEF.md, dated handoffs, and task files may interpret these records, but they must not become competing transcriptions. This ledger does not replace source images, transcriptions, or claims.jsonl; it gives those layers one stable household ID and one consistent schema.

## Reading rules

1. raw_observation records what the source or cited derivative says, including uncertainty and conflicting readings.
2. normalized_observation maps the reading into the census schedule's original column labels. It does not silently repair a source.
3. interpretation is a hypothesis or analytical use of the record. It is never evidence.
4. A census names the head of household, not every person's parentage. A listed person is not thereby proved to be a child, sibling, or ancestor.
5. source_image: not retained and image_inspected: not recorded are explicit incompleteness markers, not negative evidence.
6. Count categories are census-era categories. In 1810/1820, 16_18 overlaps 16_26 and must not be added to it.
7. Stable identity labels are provisional disambiguators. They prevent same-name people from being merged before a relationship is proved.

## Canonical schema

Every household record has these fields:

| field | meaning |
|---|---|
| census_id | stable household ID; never reuse |
| claim_ids | claims that use this household |
| year | census year |
| reference_date | census day or source date; conflicts are stated inline |
| state, county, locality | jurisdiction and locality |
| head_as_written | name written or indexed as the head |
| source_citation | repository, roll, page, or index citation |
| page_or_image | stamped page, page side, image, or locator |
| source_image | local evidence path, or not retained |
| image_inspected | yes, no, or not recorded, with qualification |
| source_layer | primary_image, primary_image_plus_index, derivative_transcription, index_only, or claim_summary |
| transcription_confidence | confidence in the observed reading, separate from identity confidence |
| raw_observation | source-level reading, preserving conflict |
| normalized_observation | structured schedule fields |
| interpretation | separate analytical conclusion |
| identity_status | stable person label and proof status |
| evidence_status | image-verified, derivative-only, indexed, or incomplete |
| last_verified | date checked against active project files |

### Schedule schemas

For 1810 and 1820, use the printed categories:

males: under_10, 10_16, 16_18, 16_26, 26_45, 45_plus  
females: under_10, 10_16, 16_26, 26_45, 45_plus

For 1830 and 1840, use the printed categories:

males and females: under_5, 5_10, 10_15, 15_20, 20_30, 30_40, 40_50, 50_60, 60_70, 70_80, 80_90, 90_100, 100_plus

For 1850 and later, use person rows. Keep source wording in fields ending in _as_written and put normalized values in separate fields:

line, dwelling_number, family_number, surname_as_written, given_name_as_written, age_as_written, sex, race, occupation_as_written, real_estate_value_as_written, birthplace_as_written, normalized_birthplace, school, literacy, other_columns

## Household register

### US-1810-VA-PRINCE-WILLIAM-AARON-ELDER-01

- claim_ids: C157
- year: 1810; reference_date: 1810-08-06
- state: Virginia; county: Prince William; locality: not recorded
- head_as_written: Aaron Caton
- source_citation: 1810 federal census, Prince William County, Virginia
- page_or_image: page [52]6; source_image: evidence/1810_PrinceWilliamCo_VA_census_AaronCaton_household.pdf
- image_inspected: yes; source_layer: primary_image_plus_index
- transcription_confidence: high for tallies; medium for identity interpretation
- raw_observation: one free white male 26-45; one free white female 26-45; no other free white persons; no slaves
- normalized_observation: males {under_10: 0, 10_16: 0, 16_18: 0, 16_26: 0, 26_45: 1, 45_plus: 0}; females {under_10: 0, 10_16: 0, 16_26: 0, 26_45: 1, 45_plus: 0}; household_total 2
- interpretation: elder Aaron, probably born c.1765-1774; likely deceased or absent by 1820. Naming connection to the later Aaron is inference.
- identity_status: AARON-ELDER; distinct from AARON-1820; relationship unproved
- evidence_status: image-verified household; interpretation grade B in C157
- last_verified: 2026-09-15

### US-1810-VA-FAUQUIER-THOMAS-ELDER-01

- claim_ids: C159
- year: 1810; reference_date: 1810-08-06
- state: Virginia; county: Fauquier; locality: not recorded
- head_as_written: Thomas Caton
- source_citation: 1810 federal census, Fauquier County, Virginia
- page_or_image: page not recorded; tallies entered below the name; source_image: evidence/1810_FauquierCo_VA_census_ThomasCaton_household.pdf
- image_inspected: yes; source_layer: primary_image
- transcription_confidence: medium; depends on one-line-down column reading
- raw_observation: one male 45_plus; one female 16_26; one female 45_plus; no other people; no slaves
- normalized_observation: males {under_10: 0, 10_16: 0, 16_18: 0, 16_26: 0, 26_45: 0, 45_plus: 1}; females {under_10: 0, 10_16: 0, 16_26: 1, 26_45: 0, 45_plus: 1}; household_total 3
- interpretation: likely the elder Thomas later seen in Fauquier; 1820 woman may be a second wife
- identity_status: THOMAS-FAUQUIER-ELDER; not THOMAS-OHIO-1830
- evidence_status: image-verified, column-offset interpretation qualified
- last_verified: 2026-09-15

### US-1820-VA-FAUQUIER-THOMAS-ELDER-01

- claim_ids: C080, C209
- year: 1820; reference_date: 1820-08-07
- state: Virginia; county: Fauquier; locality: alphabetical C page, p.46, last entry before the totals
- head_as_written: Caton Thos.
- source_citation: 1820 federal census, Fauquier County, Virginia, NARA M33 roll 136, p.46
- page_or_image: p.46; source_image: evidence/1820_FauquierCo_VA_census_p46_ThosCaton_household.jpg (crops: _header_crop, _ThosCaton_row_crop)
- image_inspected: yes, 18 Sep 2026, read against the handwritten header (C209); source_layer: primary_image
- transcription_confidence: high
- raw_observation: males under 10 = 2, 10_16 = 1, 16_18 = 1, 16_26 = none, 26_45 = none, 45_plus = 1; females under 10 = 1, 26_45 = 1
- normalized_observation: males {under_10: 2, 10_16: 1, 16_18: 1, 16_26: 0, 26_45: 0, 45_plus: 1}; females {under_10: 1, 10_16: 0, 16_26: 0, 26_45: 1, 45_plus: 0}; household_total 6
- interpretation: one under-10 slot fits AARON-1820; the other may be a brother, stepson, or grandson. Presence and parentage remain unproved.
- identity_status: THOMAS-FAUQUIER-ELDER; candidate household for AARON-1820
- evidence_status: image-verified; the 16-18 = 1 / 16-26 = none combination is in the manuscript (the row above, Cockrill, has both columns filled)
- last_verified: 2026-09-18

### US-1820-VA-FAIRFAX-MOSES-01

- claim_ids: C165, C181
- year: 1820; reference_date: 1820-08-07
- state: Virginia; county: Fairfax; locality: district No. 11
- head_as_written: Moses Caton
- source_citation: 1820 federal census, Fairfax County, NARA M33 roll 137
- page_or_image: stamped p.507, archive image 71; source_image: evidence/1820_FairfaxCo_VA_census_p507_MosesCaton_household.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high for tallies
- raw_observation: males under 10 = 1, 10_16 = 1, 16_18 = 1, 16_26 = 2, 26_45 = 0, 45_plus = 1; females under 10 = 1, 10_16 = 1, 16_26 = 1, 26_45 = 1, 45_plus = 0
- normalized_observation: same printed categories; household_total 9, counting the overlapping 16_18 column once
- interpretation: under-10 male is age-compatible with AARON-1820, but C181 identifies the slot with contributor-reported Moses B. Caton Jr.; census does not prove that identification
- identity_status: MOSES-FAIRFAX; distinct from THOMAS-FAUQUIER-ELDER
- evidence_status: image-verified; person identifications derivative
- last_verified: 2026-09-15

### US-1820-VA-PRINCESS-ANNE-THOMAS-01

- claim_ids: C074
- year: 1820; reference_date: 1820-08-07
- state: Virginia; county: Princess Anne; locality: county schedule
- head_as_written: Thomas Caton
- source_citation: 1820 federal census, Princess Anne County, Virginia
- page_or_image: pages 946-947; source_image: not retained
- image_inspected: yes per supplied page record; source_layer: primary_image
- transcription_confidence: high for tallies; low for connection to Ohio County line
- raw_observation: males 10_16 = 2 and 26_45 = 1; no females recorded
- normalized_observation: males {under_10: 0, 10_16: 2, 16_18: 0, 16_26: 0, 26_45: 1, 45_plus: 0}; females {under_10: 0, 10_16: 0, 16_26: 0, 26_45: 0, 45_plus: 0}; household_total 3
- interpretation: Tidewater Thomas; do not merge with THOMAS-OHIO-1830 or THOMAS-FAUQUIER-ELDER
- identity_status: THOMAS-PRINCESS-ANNE
- evidence_status: supplied-page reading; local package incomplete
- last_verified: 2026-09-16

### US-1820-DC-WASHINGTON-MICHAEL-01

- claim_ids: C133
- year: 1820; reference_date: 1820-08-07
- state: District of Columbia; county: Washington City; locality: Third Ward
- head_as_written: Mich'l Caton
- source_citation: 1820 federal census, Washington City, D.C., M33 roll 5
- page_or_image: p.48, FamilySearch image 103 of 233; source_image: evidence/1820_DC_WashingtonCity_3rdWard_MichaelCaton_household.md
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high for tallies
- raw_observation: males 16_26 = 2; females under 10 = 1, 10_16 = 1, 16_26 = 1, 45_plus = 1; one person in manufactures; no slaves or free colored persons
- normalized_observation: males {under_10: 0, 10_16: 0, 16_18: 0, 16_26: 2, 26_45: 0, 45_plus: 0}; females {under_10: 1, 10_16: 1, 16_26: 1, 26_45: 0, 45_plus: 1}; household_total 6
- interpretation: George W. may fit one unnamed 16_26 slot, but an unnamed tally is not residence or kinship evidence; AARON-1820 absent
- identity_status: MICHAEL-DC-1820
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1830-VA-OHIO-THOMAS-01

- claim_ids: C010, C071, C073
- year: 1830; reference_date: 1830-06-01
- state: Virginia, now West Virginia; county: Ohio; locality: division of Timothy [unread]
- head_as_written: Thomas Caton
- source_citation: 1830 federal census, Ohio County, Virginia, NARA M19 roll 198
- page_or_image: p.209; source_image: evidence/OhioCounty1830_p209_names.jpg; evidence/OhioCounty1830_p209_continuation.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high for revised tallies
- raw_observation: exactly one Caton head in the alphabetical C sequence; males 5_10 = 1 and 30_40 = 1; females under 5 = 1 and 20_30 = 1
- normalized_observation: males {under_5: 0, 5_10: 1, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 1, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}
- interpretation: not excluded as an Aaron household because Aaron turned ten sixteen days before census day; not established as his father's household
- identity_status: THOMAS-OHIO-1830; never merge with THOMAS-FAUQUIER-ELDER
- evidence_status: image-verified; C010 exclusion retained only as superseded error
- last_verified: 2026-09-15

### US-1830-VA-FAUQUIER-THOMAS-SENIOR-01

- claim_ids: C082, C208
- year: 1830; reference_date: 1830-06-01
- state: Virginia; county: Fauquier; locality: p.471
- head_as_written: Thomas Caton Sen.
- source_citation: 1830 federal census, Fauquier County, Virginia, p.471 (NARA M19); FamilySearch image
- page_or_image: p.471; source_image: evidence/1830_FauquierCo_VA_census_p471_Caton_households.jpg (crops: _males_crop, _females_crop); image_inspected: yes, 18 Sep 2026, column by column against the printed header (C208)
- source_layer: primary_image; transcription_confidence: high
- raw_observation: male 60_70 = 1; females under 5 = 2, 10_15 = 1, 15_20 = 1, 40_50 = 1; no sons
- normalized_observation: males {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 1, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 2, 5_10: 0, 10_15: 1, 15_20: 1, 20_30: 0, 30_40: 0, 40_50: 1, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 6
- interpretation: age-consistent with THOMAS-FAUQUIER-ELDER; AARON-1820 and JOSEPH-FAUQUIER-1823 are not in this household in 1830
- identity_status: THOMAS-FAUQUIER-ELDER
- evidence_status: image-verified
- last_verified: 2026-09-18

### US-1830-VA-FAUQUIER-THOMAS-JUNIOR-01

- claim_ids: C082, C208
- year: 1830; reference_date: 1830-06-01
- state: Virginia; county: Fauquier; locality: p.471
- head_as_written: Thomas Caton Jun.
- source_citation: 1830 federal census, Fauquier County, Virginia, p.471 (NARA M19); FamilySearch image
- page_or_image: p.471; source_image: evidence/1830_FauquierCo_VA_census_p471_Caton_households.jpg (crops: _males_crop, _females_crop); image_inspected: yes, 18 Sep 2026, column by column against the printed header (C208)
- source_layer: primary_image; transcription_confidence: high
- raw_observation: male under 5 = 1 and 20_30 = 1; female 20_30 = 1
- normalized_observation: males {under_5: 1, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 3
- interpretation: a male 20-30 (b. 1800-10) - NOT the consenting father of William (b. 1800-10) of Dec 1828 unless the typescript 'Jr' is wrong (D-012); not a household for AARON-1820
- identity_status: THOMAS-FAUQUIER-YOUNGER
- evidence_status: image-verified
- last_verified: 2026-09-18

### US-1830-VA-FAUQUIER-WILLIAM-01

- claim_ids: C082, C208
- year: 1830; reference_date: 1830-06-01
- state: Virginia; county: Fauquier; locality: p.471
- head_as_written: William Caton
- source_citation: 1830 federal census, Fauquier County, Virginia, p.471 (NARA M19); FamilySearch image
- page_or_image: p.471; source_image: evidence/1830_FauquierCo_VA_census_p471_Caton_households.jpg (crops: _males_crop, _females_crop); image_inspected: yes, 18 Sep 2026, column by column against the printed header (C208)
- source_layer: primary_image; transcription_confidence: high
- raw_observation: male 20_30 = 1; females under 5 = 1 and 20_30 = 1
- normalized_observation: males {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 1, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 3
- interpretation: candidate William from the 1829 marriage papers and later Cooper cluster
- identity_status: WILLIAM-FAUQUIER
- evidence_status: image-verified
- last_verified: 2026-09-18

### US-1830-VA-FAIRFAX-MOSES-01

- claim_ids: C166
- year: 1830; reference_date: 1830-06-01
- state: Virginia; county: Fairfax; locality: p.238
- head_as_written: Moses Caton
- source_citation: 1830 federal census, Fairfax County, NARA M19 roll 201
- page_or_image: p.238, archive image 477; source_image: evidence/1830_FairfaxCo_VA_census_p238_MosesCaton_household.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: males 15_20 = 1, 20_30 = 2, 60_70 = 1; females 15_20 = 1, 30_40 = 1
- normalized_observation: males {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 1, 20_30: 2, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 1, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 1, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 6
- interpretation: no male 10_15 or 5_10; AARON-1820 and JOSEPH-FAUQUIER-1823 not in this household
- identity_status: MOSES-FAIRFAX
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1830-VA-FAIRFAX-WILLIAM-G-01

- claim_ids: C166
- year: 1830; reference_date: 1830-06-01
- state: Virginia; county: Fairfax; locality: p.250
- head_as_written: William G. Caton
- source_citation: 1830 federal census, Fairfax County, NARA M19 roll 201
- page_or_image: p.250, archive image 501; source_image: evidence/1830_FairfaxCo_VA_census_p250_WilliamG_JohnR_Caton.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: males under 5 = 1 and 20_30 = 1; females under 5 = 1 and 20_30 = 1
- normalized_observation: males {under_5: 1, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 1, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 4
- interpretation: no place for AARON-1820 or JOSEPH-FAUQUIER-1823
- identity_status: WILLIAM-G-FAIRFAX; do not merge with WILLIAM-FAUQUIER
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1830-VA-FAIRFAX-JOHN-R-01

- claim_ids: C166
- year: 1830; reference_date: 1830-06-01
- state: Virginia; county: Fairfax; locality: p.250
- head_as_written: John R. Caton
- source_citation: 1830 federal census, Fairfax County, Virginia, NARA M19 roll 201
- page_or_image: p.250, archive image 501; source_image: evidence/1830_FairfaxCo_VA_census_p250_WilliamG_JohnR_Caton.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: males under 5 = 2 and 30_40 = 1; female 30_40 = 1
- normalized_observation: males {under_5: 2, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 4
- interpretation: no place for AARON-1820 or JOSEPH-FAUQUIER-1823
- identity_status: JOHN-R-FAIRFAX; do not merge with other John Catons
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1840-VA-OHIO-THOS-01

- claim_ids: C090
- year: 1840; reference_date: 1840-06-01
- state: Virginia, now West Virginia; county: Ohio; locality: p.46 in FamilySearch index
- head_as_written: Thos. Caton
- source_citation: 1840 federal census, Ohio County, Virginia; FamilySearch index p.46, https://www.familysearch.org/ark:/61903/1:1:XHBW-ZNN?lang=en; NARA M704 roll 198. Original image group 005154918, image 59 of 161, APID TH-1951-25139-50152-56, https://www.familysearch.org/ark:/61903/3:1:33S7-9YY1-9RLG?view=index&personArk=%2Fark%3A%2F61903%2F1%3A1%3AXHBW-ZNN&action=view&cc=1786457&lang=en&groupId=M9FP-G2H
- page_or_image: FamilySearch index p.46; schedule image bears handwritten p.28; image group 005154918, image 59; source_image: evidence/1840_OhioCo_VA_ThosCaton_FS_group005154918_img59.jpg; header and row crops retained alongside it
- image_inspected: yes; full schedule, printed column headings, target row, and adjacent rows inspected; source_layer: primary_image_plus_index; transcription_confidence: high for row tallies and blanks, medium for identity
- raw_observation: Thos. Caton row: free-white males under 5 = 2 and 40_50 = 1; free-white females 5_10 = 3; all other free-white age cells blank; free-colored age cells blank. Count calculated from the observed marks = 6.
- normalized_observation: males {under_5: 2, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 0, 40_50: 1, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 3, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 6
- interpretation: no male 20_30 is enumerated, so AARON-1820 is not in this household. The 1840 head may be the Thomas enumerated in 1830, but identity continuity and any parentage relationship remain unproved.
- identity_status: THOMAS-OHIO-1830 candidate; continuity between the 1830 and 1840 heads unproved
- evidence_status: complete age-cell transcription from retained image; household total calculated from schedule marks
- last_verified: 2026-09-16

### US-1840-OH-DELAWARE-JESSE-01

- claim_ids: C100, C131
- year: 1840; reference_date: 1840-06-01
- state: Ohio; county: Delaware; locality: not recorded
- head_as_written: Jesse Caton
- source_citation: 1840 federal census, Delaware County, Ohio, FamilySearch index
- page_or_image: not recorded; source_image: evidence/1840_DelawareCo_OH_JesseCaton_household.jpg; image_inspected: yes per C131
- source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: one male 30_40; household of one
- normalized_observation: males {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 1
- interpretation: not the 1850 Fairfield Jesse; identity unresolved; no male 20_30, so not AARON-1820 in this household
- identity_status: JESSE-DELAWARE-1840; do not merge with JESSE-FAIRFIELD-1850
- evidence_status: image-verified from C131; county from FamilySearch search filter, page not recorded
- last_verified: 2026-09-16

### US-1840-OH-DELAWARE-JAMES-CAYTON-01

- claim_ids: C101, G019
- year: 1840; reference_date: 1840-06-01
- state: Ohio; county: Delaware per legacy claim C101, not independently verified; locality: no confirmed page or township
- head_as_written: James Cayton, as reported in the unverified C101 claim
- source_citation: prior FamilySearch 1840 census search reported by C101; the exact Delaware County match has not been reproduced. Review and search record: G019 / evidence/2026-09-16_census_blockage_review.md
- page_or_image: no Delaware County page verified. A separate Ohio result is Liberty Township, Hancock County, p.26, FamilySearch record XHRN-7CZ; its image is retained only as a comparison hit, not assigned to this record.
- source_image: not retained for the alleged Delaware County household; comparison image: evidence/1840_HancockCo_OH_p26_JamesCayton_FS_group005154851_img57.jpg
- image_inspected: no matched Delaware County image; separate Hancock County comparison image inspected
- source_layer: index_only; transcription_confidence: not assessable for the alleged Delaware County row
- raw_observation: C101 previously reported males under 5 = 1 and 30_40 = 1; females 5_10 = 2 and 20_30 = 1. These are retained as a historical claim only and were not independently reproduced.
- normalized_observation: not established; do not assign age categories or household total until a Delaware County schedule page is located and matched
- interpretation: the exact-place search returned no match; the Hancock County James Cayton is not evidence for a Delaware County household. No parentage or migration inference is supported by this entry.
- identity_status: JAMES-CAYTON-C101-UNVERIFIED; do not merge with the 1850 James Cayton until the 1840 source is located
- evidence_status: legacy claim under review; Delaware locator unverified; Hancock comparison hit is a different county and is not substituted
- last_verified: 2026-09-16

### US-1840-MO-COOPER-JOHN-01

- claim_ids: C057, C095
- year: 1840; reference_date: 1840-06-01
- state: Missouri; county: Cooper; locality: p.141
- head_as_written: John Caton
- source_citation: 1840 federal census, Cooper County, Missouri, p.141; FamilySearch index record XHTF-Z9T, https://www.familysearch.org/ark:/61903/1:1:XHTF-Z9T?lang=en; original image group 005154556, image 989 of 1315, APID TH-1942-25142-50785-77, https://www.familysearch.org/ark:/61903/3:1:33SQ-GYBS-9TDR?view=index&personArk=%2Fark%3A%2F61903%2F1%3A1%3AXHTF-Z9T&action=view&cc=1786457&lang=en
- page_or_image: p.141; page header Cooper Co.; FamilySearch names panel identifies John Caton household; source_image: evidence/1840_CooperCo_MO_p141_JohnCaton_FS_group005154556_img989.jpg; candidate row-band crop: evidence/1840_CooperCo_MO_p141_JohnCaton_candidate-row-band.jpg
- image_inspected: partial; original image and candidate row band inspected; row alignment not resolved; source_layer: primary_image_plus_index; transcription_confidence: not assigned because no independent row transcription
- raw_observation: FamilySearch locates a John Caton household on the p.141 Cooper County image. C057's prior reading reported males under 5 = 1, 5_10 = 1, 40_50 = 1; females under 5 = 2, 10_15 = 1, 20_30 = 1. Those age tallies remain an unverified prior reading, not a raw transcription from this review.
- normalized_observation: not established; no category values or household total assigned pending independent row alignment
- interpretation: possible collateral lead only. C095 concerns a later Delaware-born John Caton; identity continuity with this 1840 household is unproved. No kinship to Aaron is established.
- identity_status: JOHN-COOPER-DELAWARE-BORN
- evidence_status: index locator and original page retained; target row not independently transcribed; manual review required
- last_verified: 2026-09-16

### US-1840-MO-COOPER-WILLIAM-01

- claim_ids: C128
- year: 1840; reference_date: 1840-06-01
- state: Missouri; county: Cooper; locality: p.145
- head_as_written: Wm. Caton
- source_citation: 1840 federal census, Cooper County, Missouri
- page_or_image: p.145; source_image: evidence/1840_CooperCo_MO_p145_WmCaton_ThsCaton_NLaurie.jpg
- image_inspected: yes; source_layer: primary_image; transcription_confidence: high
- raw_observation: males under 5 = 1, 5_10 = 1, 10_15 = 1, 30_40 = 1; female 30_40 = 1
- normalized_observation: males {under_5: 1, 5_10: 1, 10_15: 1, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 5
- interpretation: likely Fauquier William, but the 10_15 boy and missing 1830 daughter keep identification at C
- identity_status: WILLIAM-FAUQUIER candidate
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1840-MO-COOPER-THS-01

- claim_ids: C128
- year: 1840; reference_date: 1840-06-01
- state: Missouri; county: Cooper; locality: p.145
- head_as_written: Ths. Caton
- source_citation: 1840 federal census, Cooper County, Missouri
- page_or_image: p.145; source_image: evidence/1840_CooperCo_MO_p145_WmCaton_ThsCaton_NLaurie.jpg
- image_inspected: yes; source_layer: primary_image; transcription_confidence: high
- raw_observation: males 5_10 = 2 and 30_40 = 1; female 10_15 = 1; no adult female
- normalized_observation: males {under_5: 0, 5_10: 2, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 0, 10_15: 1, 15_20: 0, 20_30: 0, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 4
- interpretation: possible THOMAS-FAUQUIER-YOUNGER; identity indeterminate
- identity_status: THOMAS-COOPER-1840; not THOMAS-COOPER-KENTUCKY-1850
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1840-MO-COOPER-GEORGE-W-01

- claim_ids: C129, C130
- year: 1840; reference_date: 1840-06-01
- state: Missouri; county: Cooper; locality: Boonville, p.135
- head_as_written: Geo. W. Caton
- source_citation: 1840 federal census, Cooper County, Missouri
- page_or_image: p.135; source_image: evidence/1840_CooperCo_MO_p135_GeoWCaton_household.jpg
- image_inspected: yes; source_layer: primary_image; transcription_confidence: high
- raw_observation: males 5_10 = 1, 10_15 = 1, 15_20 = 2, 20_30 = 2, 30_40 = 1; females under 5 = 2, 15_20 = 2, 30_40 = 1
- normalized_observation: males {under_5: 0, 5_10: 1, 10_15: 1, 15_20: 2, 20_30: 2, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 2, 5_10: 0, 10_15: 0, 15_20: 2, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 12
- interpretation: unnamed 20_30 and 15_20 slots fit AARON-1820 and JOSEPH-FAUQUIER-1823 by age, but unnamed tallies are not identity evidence and Aaron's 1841 Ohio marriage conflicts with Boonville residence
- identity_status: GEORGE-W-BOONVILLE-TAILOR; distinct from GEORGE-W-MUSKINGUM
- evidence_status: image-verified; person fits hypotheses
- last_verified: 2026-09-15

### US-1840-MO-RIVES-JONAS-01

- claim_ids: C059
- year: 1840; reference_date: 1840-06-01
- state: Missouri; county: Rives, renamed Henry in 1841; locality: p.367
- head_as_written: Jonas Caton
- source_citation: 1840 federal census, Rives County, Missouri
- page_or_image: p.367; source_image: not retained; image_inspected: yes, alignment unconfirmed
- source_layer: primary_image; transcription_confidence: low
- raw_observation: larger adjacent Caton household; full age-bracket structure not reliably read
- normalized_observation: age counts not recorded
- interpretation: candidate only; retain Rives as the 1840 county name
- identity_status: JONAS-RIVES-1840
- evidence_status: image located but not sufficiently transcribed
- last_verified: 2026-09-15

### US-1840-MO-RIVES-JOSHUA-01

- claim_ids: C059
- year: 1840; reference_date: 1840-06-01
- state: Missouri; county: Rives, renamed Henry in 1841; locality: p.367
- head_as_written: Joshua Caton
- source_citation: 1840 federal census, Rives County, Missouri
- page_or_image: p.367; source_image: not retained; image_inspected: yes, alignment unconfirmed
- source_layer: primary_image; transcription_confidence: low
- raw_observation: adjacent household with a single male tally; exact column not securely read
- normalized_observation: age counts not recorded
- interpretation: candidate only; no relationship to AARON-1820
- identity_status: JOSHUA-RIVES-1840
- evidence_status: image located but not sufficiently transcribed
- last_verified: 2026-09-15

### US-1840-OH-MUSKINGUM-GEORGE-W-01

- claim_ids: C183
- year: 1840; reference_date: 1840-06-01
- state: Ohio; county: Muskingum; locality: Newton Township, p.324
- head_as_written: George W. Caton
- source_citation: 1840 federal census, Muskingum County, Ohio, NARA M704 roll 418
- page_or_image: stamped p.324, image 157; source_image: evidence/1840_MuskingumCo_OH_NewtonTwp_p324_GeorgeWCaton_page.jpg; evidence/1840_MuskingumCo_OH_NewtonTwp_p324_GeorgeWCaton_row.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: males under 5 = 1, 5_10 = 1, 30_40 = 1; females under 5 = 2, 20_30 = 1
- normalized_observation: males {under_5: 1, 5_10: 1, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 2, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 6
- interpretation: no male 20_30; AARON-1820 not in this household
- identity_status: GEORGE-W-MUSKINGUM; distinct from GEORGE-W-BOONVILLE-TAILOR
- evidence_status: image-verified
- last_verified: 2026-09-16

### US-1840-OH-MUSKINGUM-THOS-01

- claim_ids: C183
- year: 1840; reference_date: 1840-06-01
- state: Ohio; county: Muskingum; locality: Salt Creek Township, p.468
- head_as_written: Thos. Caton; initial may be C or E
- source_citation: 1840 federal census, Muskingum County, Ohio, NARA M704 roll 418
- page_or_image: stamped p.468, image 447; source_image: evidence/1840_MuskingumCo_OH_SaltCreekTwp_p468_ThosCaton_page.jpg; evidence/1840_MuskingumCo_OH_SaltCreekTwp_p468_ThosCaton_row.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high for tallies, medium for name
- raw_observation: male 30_40 = 1; females under 5 = 1 and 20_30 = 1
- normalized_observation: males {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 1, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 1, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 1, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 3
- interpretation: not THOMAS-FAUQUIER-ELDER; no slot for AARON-1820
- identity_status: THOS-MUSKINGUM-1840; unresolved
- evidence_status: image-verified; identity grade B
- last_verified: 2026-09-15

### US-1840-OH-PERRY-ROSANA-01

- claim_ids: C174
- year: 1840; reference_date: 1840-06-01
- state: Ohio; county: Perry; locality: Reading Township
- head_as_written: Rosana Caton
- source_citation: 1840 federal census, Perry County, Ohio
- page_or_image: page not recorded; source_image: evidence/1840_PerryCo_OH_ReadingTwp_RosanaCaton_household.jpg
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high for tallies
- raw_observation: males 20_30 = 2; females 5_10 = 1 and 60_70 = 1
- normalized_observation: males {under_5: 0, 5_10: 0, 10_15: 0, 15_20: 0, 20_30: 2, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 0, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; females {under_5: 0, 5_10: 1, 10_15: 0, 15_20: 0, 20_30: 0, 30_40: 0, 40_50: 0, 50_60: 0, 60_70: 1, 70_80: 0, 80_90: 0, 90_100: 0, 100_plus: 0}; household_total 4
- interpretation: Moses's-widow identification withdrawn; likely Irish Caton household based on neighbors; unnamed age fit is not Aaron evidence
- identity_status: ROSANA-PERRY-1840; do not merge with Moses's family
- evidence_status: image-verified; identity unresolved
- last_verified: 2026-09-16

### US-1850-OH-DELAWARE-AARON-01

- claim_ids: C006, C016, C018, C038, C039
- year: 1850
- reference_date: 1850-08-02 per current USGenWeb transcription; older handoff reported 1850-08-22; image header/date needs direct recheck
- state: Ohio; county: Delaware; locality: Town of Delaware
- head_as_written: Aaron Caton
- source_citation: 1850 federal census, NARA M432 roll 675, Delaware County, Ohio
- page_or_image: p.179a-179b, stamped p.179; dwelling 1160, family 1163; source_image: evidence/Aaron_Caton_1850_Delaware_OH_n172_w1800.jpg
- image_inspected: yes; Julia's birthplace cell blotted; source_layer: primary_image_plus_index plus derivative transcription
- transcription_confidence: high for members/ages; medium or low for Julia birthplace
- raw_observation: p.179a lines 38-42: Aaron 30, male, tailor, Virginia; Sarah 26, female, Ohio; Julia 7, female, derivative reads Massachusetts; Mary E. 5, female, Ohio; Wm. B. 2, male, Ohio. p.179b line 1: Nancy 9/12, female, Ohio. Image cell for Julia is read in the project as Mo.
- normalized_observation: person rows for Aaron, Sarah, Julia, Mary E., Wm. B., Nancy; dwelling_number 1160; family_number 1163; Julia normalized_birthplace Missouri, with raw conflict retained
- interpretation: Missouri is the project value because image reading, 1860 census, and 1916 death certificate converge; USGenWeb Mass remains a derivative conflict, not deleted evidence
- identity_status: AARON-1820 direct-line household
- evidence_status: image and derivative transcription preserved; birthplace resolved only at project interpretation layer
- last_verified: 2026-09-15

### US-1850-OH-OHIO-BORING-01

- claim_ids: C011, C032
- year: 1850; reference_date: 1850-06-01
- state: Virginia, now West Virginia; county: Ohio; locality: Wheeling area
- head_as_written: John Boring
- source_citation: 1850 federal census, Ohio County, Virginia
- page_or_image: p.160b; source_image: evidence/1850_OhioCo_VA_p160b_transcription.txt
- image_inspected: not recorded; source_layer: derivative_transcription; transcription_confidence: high for Harrison
- raw_observation: Harrison Caton, age 14, male, Virginia, in John Boring's bricklayer household; not head and no relationship field establishes sonship
- normalized_observation: surname_as_written Caton; given_name_as_written Harrison; age_as_written 14; sex M; birthplace_as_written Virginia; household_head John Boring
- interpretation: apprentice or boarder possible; not proof of kinship to AARON-1820
- identity_status: HARRISON-BORING-1850; do not merge with other Harrison Catons
- evidence_status: derivative transcription; earlier “only Caton” scope was overstated
- last_verified: 2026-09-15

### US-1850-MO-CHARITON-JOSEPH-01

- claim_ids: C061, C076, C110
- year: 1850; reference_date: 1850-06-01
- state: Missouri; county: Chariton; locality: Brunswick City
- head_as_written: Joseph Caton
- source_citation: 1850 federal census, Chariton County, Missouri
- page_or_image: p.236; source_image: not retained; image_inspected: not recorded
- source_layer: derivative_transcription; transcription_confidence: high for head, medium for household, low for children's names
- raw_observation: Joseph 28, tailor, Virginia; Harriet 20, Ohio; two male children ages 2 and 9/12, Missouri; children's names read Darcy/Dorsey and Edgar
- normalized_observation: person rows for Joseph, Harriet, and two uncertain children; household_total 4
- interpretation: consistent with later Joseph born Fauquier account; relationship to AARON-1820 is inference from multiple records
- identity_status: JOSEPH-FAUQUIER-1823
- evidence_status: derivative household reading; image path not retained
- last_verified: 2026-09-15

### US-1850-MO-COOPER-JOHN-01

- claim_ids: C095, C096
- year: 1850; reference_date: 1850-10-09
- state: Missouri; county: Cooper; locality: District 23
- head_as_written: John Caton
- source_citation: 1850 federal census, Cooper County, Missouri
- page_or_image: p.268, household 902; source_image: not retained; image_inspected: not recorded
- source_layer: derivative_transcription; transcription_confidence: high for head/birthplace
- raw_observation: John 53, farmer, real estate $2,000, Delaware; Columbus M. 19, Benjamin 13, Elizabeth 11, Ophelia 9, Missouri
- normalized_observation: person rows; head_age_as_written 53; head_birthplace_as_written Delaware; occupation_as_written farmer
- interpretation: distinct Delaware-born Cooper line; do not merge with Fauquier Catons
- identity_status: JOHN-COOPER-DELAWARE-BORN
- evidence_status: derivative transcription; image not retained
- last_verified: 2026-09-15

### US-1850-MO-COOPER-WILLIAM-FAUQUIER-01

- claim_ids: C096, C098
- year: 1850; reference_date: 1850-06-01
- state: Missouri; county: Cooper; locality: transcription p.23, household 357
- head_as_written: William Caton
- source_citation: 1850 federal census, Cooper County, MOGenWeb transcription and page image
- page_or_image: p.23, household 357; source_image: evidence/1850_CooperCo_MO_p23_Caton-Laurie-Payne_households.png
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: William 38, Virginia; John W. 18, male, Virginia; Aaron F. 8, male, Missouri; Sarah Ann 6, Elizabeth 4, Wingfield 2, Missouri; no adult female
- normalized_observation: person rows; household_number 357; head_age_as_written 38; head_birthplace_as_written Virginia; household_total 6
- interpretation: likely Fauquier William because Daniel Laurie and Ann Laurie are two households away; Ann's maiden name comes from C092, not census
- identity_status: WILLIAM-FAUQUIER; identification supported by cluster and marriage evidence
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1850-MO-COOPER-THOMAS-KENTUCKY-01

- claim_ids: C096
- year: 1850; reference_date: 1850-06-01
- state: Missouri; county: Cooper; locality: household 1038, page not securely recorded
- head_as_written: Thomas Caton
- source_citation: 1850 federal census, Cooper County, MOGenWeb transcription
- page_or_image: not securely recorded; source_image: not retained; image_inspected: no
- source_layer: derivative_transcription; transcription_confidence: medium
- raw_observation: Thomas about 40, Kentucky; wife about 40, Kentucky; Lucinda 18, James 16, Newton 14, Nimrod about 12, Nancy 6, and other children; Missouri-born children
- normalized_observation: incomplete person rows; head_birthplace_as_written Kentucky
- interpretation: separate Kentucky-origin Cooper line
- identity_status: THOMAS-COOPER-KENTUCKY-1850; do not merge with Thomas-FAUQUIER
- evidence_status: derivative transcription; image verification pending
- last_verified: 2026-09-15

### US-1850-MO-COOPER-JAMES-PAYNE-352-01

- claim_ids: C098
- year: 1850; reference_date: 1850-06-01
- state: Missouri; county: Cooper; locality: transcription p.23, household 352
- head_as_written: James R. Payne
- source_citation: 1850 federal census, Cooper County, MOGenWeb transcription and page image
- page_or_image: p.23, household 352; source_image: evidence/1850_CooperCo_MO_p23_Caton-Laurie-Payne_households.png
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: James R. Payne, 38, born Virginia
- normalized_observation: person row; household_number 352; head_age_as_written 38; head_birthplace_as_written Virginia
- interpretation: proximity to the Fauquier Caton-Laurie cluster is relevant; no relationship to Catons is stated by this census
- identity_status: JAMES-PAYNE-COOPER-1850
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1850-MO-COOPER-CATHARINE-LAURIE-353-01

- claim_ids: C098
- year: 1850; reference_date: 1850-06-01
- state: Missouri; county: Cooper; locality: transcription p.23, household 353
- head_as_written: Catharine Laurie
- source_citation: 1850 federal census, Cooper County, MOGenWeb transcription and page image
- page_or_image: p.23, household 353; source_image: evidence/1850_CooperCo_MO_p23_Caton-Laurie-Payne_households.png
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: Catharine Laurie, 63, born Virginia; Isa Payne 15, Virginia; Abeam Newton 53, Virginia
- normalized_observation: person rows; household_number 353; head_age_as_written 63; head_birthplace_as_written Virginia
- interpretation: part of the adjacent Laurie-Payne cluster; relationship to Ann Laurie is not stated by this census
- identity_status: CATHARINE-LAURIE-COOPER-1850
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1850-MO-COOPER-DANIEL-LAURIE-354-01

- claim_ids: C098
- year: 1850; reference_date: 1850-06-01
- state: Missouri; county: Cooper; locality: transcription p.23, household 354
- head_as_written: Daniel Laurie
- source_citation: 1850 federal census, Cooper County, MOGenWeb transcription and page image
- page_or_image: p.23, household 354; source_image: evidence/1850_CooperCo_MO_p23_Caton-Laurie-Payne_households.png
- image_inspected: yes; source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: Daniel Laurie 44 and Ann Laurie 33, both Virginia; Joseph 15 Ohio; Martha Ann 12, Daniel R. 9, Catharine 7, Jacob 4, and Guiluanna 1, Missouri-born
- normalized_observation: person rows; household_number 354; Daniel and Ann birthplace_as_written Virginia; eldest child birthplace_as_written Ohio
- interpretation: Ann Laurie is the Ann Caton of the 1835 Fauquier marriage record; the route is Fauquier to Ohio to Cooper. Maiden name comes from C092, not this census.
- identity_status: DANIEL-LAURIE-COOPER-1850; ANN-CATON-LAURIE
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1850-MO-COOPER-MADDEX-THOMAS-77-01

- claim_ids: C205
- year: 1850; reference_date: 1850-06-01; enumerated 1850-08-14 per transcription
- state: Missouri; county: Cooper; locality: City of Boonville, transcription p.148, household 66
- head_as_written: John P. Maddex
- source_citation: 1850 federal census, Cooper County, Jim Thoma 2013 MOGenWeb transcription (Wayback copy)
- page_or_image: transcription p.148, dwelling/family 66, line 24; manuscript locator per ChatGPT register NARA M432 roll 397, unverified; source_image: not retained (transcription PDF retained as evidence/1850_CooperCo_MO_census_transcription_Thoma2013_mogenweb_archive.pdf)
- image_inspected: no; source_layer: derivative_transcription; transcription_confidence: medium
- raw_observation: Maddex John P. 47 M Constable $1,200 Virginia; Parthema G. 39 F Virginia; Jane 17 F Virginia; Tebisha D. 15 F Missouri; Michael G. 8 M Missouri; John A. 1 M Missouri; Caton Thomas 77 M "Taylor" Virginia (last row of the household)
- normalized_observation: person rows; household_number 66; Caton row: line 24, age_as_written 77, sex M, occupation_as_written Taylor, birthplace_as_written Virginia, normalized_birthplace Virginia; household_total 7
- interpretation: a Virginia-born tailor b. c.1772-73 living in a non-Caton household; placement states no kinship; age fits only the 1820 Fauquier head (45+) among the Fauquier Thomas brackets (C205)
- identity_status: THOMAS-COOPER-BOONVILLE-1850-77; unresolved; do not merge with THOMAS-FAUQUIER-ELDER or THOMAS-FAUQUIER-YOUNGER
- evidence_status: derivative transcription; image verification pending
- last_verified: 2026-09-18

### US-1850-MO-COOPER-HOWARD-JAMES-19-01

- claim_ids: C205
- year: 1850; reference_date: 1850-06-01; enumerated 1850-08-27 per transcription
- state: Missouri; county: Cooper; locality: District 23, transcription pp.183-184, household 335
- head_as_written: John C. Howard
- source_citation: 1850 federal census, Cooper County, Jim Thoma 2013 MOGenWeb transcription (Wayback copy)
- page_or_image: transcription p.184 line 2 (household begins p.183 line 37); source_image: not retained
- image_inspected: no; source_layer: derivative_transcription; transcription_confidence: medium
- raw_observation: Howard John C. 21 M Farmer Virginia; Ann M. 18 F Virginia; Mary R. 17 F Virginia; William H. H. 14 M Virginia; Alex G. 6 M Missouri; Goodrich A. 2 M Missouri; Caton James 19 M Carpenter Virginia; Warts Jonathan 35 M Laborer Pennsylvania; Thomas Thomas 22 M Laborer Missouri; Seruner [blank] 30 M Laborer Tennessee
- normalized_observation: person rows; household_number 335; Caton row: line 2, age_as_written 19, sex M, occupation_as_written Carpenter, birthplace_as_written Virginia, normalized_birthplace Virginia
- interpretation: a Virginia-born Caton b. c.1831 boarding with a Virginia-born family; not previously in the project; no link to any known Caton
- identity_status: JAMES-COOPER-1850-19; unresolved
- evidence_status: derivative transcription; image verification pending
- last_verified: 2026-09-18

### US-1850-OH-FAIRFIELD-JESSE-KATON-01

- claim_ids: C105, C119
- year: 1850; reference_date: 1850-09-17
- state: Ohio; county: Fairfield; locality: Rush Creek Township
- head_as_written: Jesse Katon
- source_citation: 1850 federal census, Fairfield County, Ohio
- page_or_image: p.428, dwelling 289; source_image: evidence/1850_FairfieldCo_OH_RushCreek_JesseKaton_household.pdf; image_inspected: yes per C119
- source_layer: primary_image_plus_index; transcription_confidence: high
- raw_observation: Jesse 43, farmer, Maryland; Nancy 37 Ohio; Thos. E. 15, Mary E. 10, John 8, Sarah 6, William 3, Ohio; preceding Eleanor and Kasia Katon household
- normalized_observation: person rows; head_age_as_written 43; head_birthplace_as_written Maryland; occupation_as_written farmer
- interpretation: not Delaware Jesse of 1840; C105 identification withdrawn
- identity_status: JESSE-FAIRFIELD-1850; do not merge with JESSE-DELAWARE-1840
- evidence_status: indexed/derived record; image not retained
- last_verified: 2026-09-15

### US-1850-MO-ST-CLAIR-GEORGE-W-01

- claim_ids: C123
- year: 1850; reference_date: 1850-08-18
- state: Missouri; county: St. Clair; locality: District 79, household 28
- head_as_written: George W. Caton
- source_citation: 1850 federal census, St. Clair County, M432-413
- page_or_image: p.4; source_image: not retained; image_inspected: no
- source_layer: derivative_transcription; transcription_confidence: medium
- raw_observation: George W. 50, tailor, Virginia; Sarah A. 43, Maryland; George R. 22, D.C.; Thos. N. 20, Missouri; Sabina 15 and Rebecca 8, Missouri; real estate $570
- normalized_observation: person rows; head_age_as_written 50; head_birthplace_as_written Virginia; occupation_as_written tailor
- interpretation: George W. of Alexandria/Boonville biography; Sarah's age makes her not the mother of AARON-1820 unless an earlier wife is involved
- identity_status: GEORGE-W-BOONVILLE-TAILOR
- evidence_status: imported transcription; image not inspected in this workspace
- last_verified: 2026-09-15

### US-1860-MO-LIVINGSTON-AARON-01

- claim_ids: C043, C044
- year: 1860; reference_date: 1860-06-20
- state: Missouri; county: Livingston; locality: Jackson Township, PO Springhill
- head_as_written: Aaron Caton
- source_citation: 1860 federal census, Livingston County, Missouri; FamilySearch index
- page_or_image: p.40, dwelling 264, family 265; source_image: not retained
- image_inspected: page/header reported in C043; local image not retained; source_layer: primary_image_plus_index
- transcription_confidence: medium; locator stronger than missing row extraction
- raw_observation: household located at Jackson Township, p.40, dwelling/family 264/265, enumerated 20 June; C044 records James Caton, age 1, Missouri
- normalized_observation: person rows retained {Aaron Caton: head, full row not transcribed; James Caton: age_as_written 1, birthplace_as_written Missouri}; full roster not recorded
- interpretation: direct-line household; 1860 James and 1870 Caton H./Henry are linked only as unresolved inference. Locality is Jackson, not Richland.
- identity_status: AARON-1820; child HENRY-OR-JAMES-1859 unresolved
- evidence_status: indexed locator plus reported page/header reading; image-level transcription incomplete
- last_verified: 2026-09-15

### US-1860-MO-BOONE-THOS-H-01

- claim_ids: C020
- year: 1860; reference_date: 1860-06-01
- state: Missouri; county: Boone; locality: Roche Township
- head_as_written: Thos. H. Caton
- source_citation: 1860 federal census, Boone County, Missouri, NARA M653 roll 608
- page_or_image: image n546; source_image: evidence/Boone_MO_1860_Roche_Twp_Caton_n546_w1800.jpg
- image_inspected: yes; source_layer: primary_image; transcription_confidence: high
- raw_observation: Thos. H. Caton, age 35, born Kentucky, Roche Township
- normalized_observation: person row; age_as_written 35; birthplace_as_written Kentucky; locality Roche Township
- interpretation: separate Kentucky/Missouri line
- identity_status: THOMAS-H-BOONE-KENTUCKY
- evidence_status: image-verified
- last_verified: 2026-09-15

### US-1860-MO-BATES-WILLIAM-01

- claim_ids: C055
- year: 1860; reference_date: 1860-08-09
- state: Missouri; county: Bates; locality: Lebanon Township, PO Fair Point
- head_as_written: Wm. Caton
- source_citation: 1860 federal census, Bates County, Missouri
- page_or_image: p.60, dwelling/family 416/416; source_image: not retained; image_inspected: not recorded
- source_layer: derivative_transcription; transcription_confidence: high
- raw_observation: William 50, farmer, Maryland; Ann 38, Virginia; Aaron 20, Missouri; S.A. 16, L.B. 12, Richard 6, Missouri
- normalized_observation: person rows; head_age_as_written 50; head_birthplace_as_written Maryland; occupation_as_written farmer
- interpretation: Aaron F. / Maryland-born William cluster, not AARON-1820; birth state conflicts with 1850 Virginia reading and stays visible
- identity_status: WILLIAM-BATES-MARYLAND
- evidence_status: derivative transcription
- last_verified: 2026-09-15

### US-1860-MO-BATES-JH-01

- claim_ids: C055
- year: 1860; reference_date: 1860-08-09
- state: Missouri; county: Bates; locality: Lebanon Township, PO Fair Point
- head_as_written: J. H. Caton
- source_citation: 1860 federal census, Bates County, Missouri
- page_or_image: p.60, dwelling/family 415/415; source_image: not retained; image_inspected: not recorded
- source_layer: derivative_transcription; transcription_confidence: high
- raw_observation: J. H. 27, farmer, Virginia; S. G. 24, Virginia; W. A. 2, Kansas
- normalized_observation: person rows; head_age_as_written 27; head_birthplace_as_written Virginia
- interpretation: adjacent Bates household; no demonstrated relationship to AARON-1820
- identity_status: JH-CATON-BATES-1860
- evidence_status: derivative transcription
- last_verified: 2026-09-15

### US-1870-MO-COOPER-JULIA-SAWTELL-01

- claim_ids: C041, C042, C115
- year: 1870; reference_date: 1870-06-06
- state: Missouri; county: Cooper; locality: City of Boonville, PO Boonville
- head_as_written: S. G. Sawtell
- source_citation: 1870 federal census, City of Boonville, Cooper County, Missouri
- page_or_image: p.5, stamped p.348, dwelling/family 25/25; source_image: not retained
- image_inspected: yes per C041; local image not retained; source_layer: primary_image_plus_index
- transcription_confidence: high for names/ages; medium for occupation abbreviation
- raw_observation: S. G. Sawtell 29, painter, Tennessee; Julia A. 24, keeping house; infant 4/12; Caton H. 11, Missouri; Aaron Caton 55, “Ret. Laborer” or “R.R. Laborer,” Virginia; Charles J. Ingersoll 32, merchant, Maryland
- normalized_observation: person rows; head_as_written S. G. Sawtell; Aaron age_as_written 55; Aaron birthplace_as_written Virginia; occupation_as_written Ret. Laborer, possibly R.R. Laborer
- interpretation: Julia is the direct-line daughter identified by C037/C042; Aaron lived in his married daughter's household and no wife is present. Railroad laborer is a qualified project normalization only.
- identity_status: AARON-1820; JULIA-SAWTELL
- evidence_status: image reading reported in claim; source image path not retained
- last_verified: 2026-09-15

### US-1880-MO-COOPER-AARON-F-01

- claim_ids: C052
- year: 1880; reference_date: 1880-06-01
- state: Missouri; county: Cooper; locality: Otterville
- head_as_written: Aaron Caton
- source_citation: 1880 federal census, Otterville, Cooper County, Missouri
- page_or_image: not recorded; source_image: not retained; image_inspected: not recorded
- source_layer: claim_summary; transcription_confidence: medium
- raw_observation: Aaron 44, Missouri, laborer; wife Nancy; children L. Alice, Jennie E., Henry, Georgie A., Sarah E., William T., Gillie Lee, Evie L.
- normalized_observation: person rows; head_age_as_written 44; head_birthplace_as_written Missouri; occupation_as_written laborer
- interpretation: Aaron F. Caton, son of WILLIAM-FAUQUIER, not AARON-1820
- identity_status: AARON-F-COOPER
- evidence_status: claim-level household summary; image/citation incomplete
- last_verified: 2026-09-15

### US-1880-MO-BATES-HARRISON-01

- claim_ids: C050
- year: 1880; reference_date: 1880-06-01
- state: Missouri; county: Bates; locality: Walnut Township, ED 148
- head_as_written: Harrison Caton
- source_citation: 1880 federal census, Bates County, Missouri
- page_or_image: dwelling 49/51; source_image: not retained; image_inspected: not recorded
- source_layer: claim_summary; transcription_confidence: medium
- raw_observation: Harrison 55, farmer, Ohio; father Maryland; mother Ohio; niece Nancy B. 17
- normalized_observation: person rows; head_age_as_written 55; head_birthplace_as_written Ohio; occupation_as_written farmer
- interpretation: not the 1850 Ohio County Harrison, who was 14 and Virginia-born
- identity_status: HARRISON-BATES-1880
- evidence_status: claim-level household summary
- last_verified: 2026-09-15

## Bounded census coverage checks

These are not household transcriptions. They record the scope of a no-hit or completeness test so an unexamined schedule is not mistaken for negative proof.

| coverage_id | claim_ids | year/jurisdiction | result | source_layer | status |
|---|---|---|---|---|---|
| US-1820-VA-PRINCE-WILLIAM-C-BLOCK-NO-CATON-01 | C155 | 1820, Prince William County, VA | C block pages read; no Caton head | primary_image | bounded negative |
| US-1830-VA-PRINCE-WILLIAM-C-BLOCK-NO-CATON-01 | C167 | 1830, Prince William County, VA | C block images read; no Caton head | primary_image | bounded negative |
| US-1820-VA-CULPEPER-STAFFORD-C-BLOCK-NO-CATON-01 | C188 | 1820, Culpeper and Stafford Counties, VA | C blocks read; no Caton/Cayton/Caten head; Mildred Catlett is not Caton | primary_image | bounded negative |
| US-1850-OH-DELAWARE-CATON-INDEX-COVERAGE-01 | C102 | 1850, Delaware County, OH | FamilySearch surname export returned Aaron's household only | index_only | bounded indexed coverage |
| US-1830-VA-FAIRFAX-CATON-COVERAGE-01 | C166 | 1830, Fairfax County, VA | name-column scan found Moses, William G., and John R.; no other Caton head located | primary_image | bounded image coverage |

## Known normalization conflicts

| subject | raw readings | canonical treatment |
|---|---|---|
| Julia's 1850 birthplace | image read as Mo; USGenWeb derivative reads Mass | preserve both in raw_observation; normalize project value to Missouri only in normalized_observation and interpretation, supported by 1860 and 1916 |
| 1850 enumeration date | current transcription says 2 August; older handoff says 22 August | retain both until image header is rechecked |
| 1860 Livingston locality | C043 says Jackson Township; another handoff said Richland | use Jackson from the indexed locator/page-header reading; keep Richland as an open discrepancy |
| Aaron's 1870 occupation | Ret. Laborer or R.R. Laborer | preserve source abbreviation; narrative may say railroad laborer only as qualified normalization |
| 1840 Cooper brackets | earlier notes use inclusive shorthand such as 5-9/10-14 | use printed labels 5_10 and 10_15; retain raw shorthand in claims where relevant |
