# Claims index — generated 2026-09-24 from `claims.jsonl` (233 claims)

Census household composition is canonical in `CATON_CENSUS_LEDGER.md`; use its stable IDs for row-level readings.

Regenerate with `python3 tools/make-claims-index.py`. **Do not edit by hand.**

Type and lifecycle are read from explicit `claim_type` and `status` fields. Legacy classifications marked `legacy_text_migration` require source-level review; no status is inferred here.

Each row also carries `kind` (METHOD.md §4), kept equal to the mapping of `claim_type` + `status` by `tools/check-claims.py`; `fact`/`negative`/`do-not-merge` are the `kind` spellings of `observation`/`negative_search`/`identity_constraint`, and `void` covers `superseded`/`reversed`.

| claim type | n | | lifecycle | n |
|---|---:|---|---|---:|
| fact | 168 | | active | 221 |
| hypothesis | 14 | | superseded | 3 |
| negative | 26 | | reversed | 5 |
| do-not-merge | 4 | | void | 1 |
| method | 20 | | moot | 1 |
| other | 1 | | review | 2 |

| evidence grade | n |
|---|---:|
| A | 128 |
| B | 68 |
| C | 37 |

## The load-bearing ones

| id | grade | type | lifecycle | what |
|---|---|---|---|---|
| **C038** | A | fact | active | REVERSES C016. JULIA WAS BORN IN MISSOURI, NOT MASSACHUSETTS. Three independent sources converge: the 1850 census image (blotted cell, reads 'Mo', NOT… |
| **C058** | A | method | active | GAP CLOSED. Through eight passes this project did ZERO 1840 census work - 9 claims touched 1850, 6 touched 1860, 4 touched 1880, none touched 1840. Th… |
| **C062** | B | fact | active | UPGRADED C->B on 11 Sep 2026 by C110 (1898 newspaper: Joseph was 'the guest of his niece, Mrs. Sawtell' in Boonville). STRONGEST SIBLING CANDIDATE YET… |
| **C069** | A | method | active | SECOND STRUCTURAL GAP, LARGER THAN THE 1840 ONE. An audit of claims.jsonl on 10 Sep 2026 found ZERO American probate work across nine passes: no will,… |
| **C075** | A | method | active | THE LARGEST UNEXAMINED ASSUMPTION IN THE PROJECT. 'WHEELING' IS UNSOURCED. Every record that states Aaron's birthplace says only 'VIRGINIA': C006 (185… |
| **C077** | B | hypothesis | active | CORROBORATED - UPGRADED C TO B. The obituary's 'FORKWARE county, Va.' (C076) is read as FAUQUIER COUNTY, VIRGINIA: the letter-groups map onto a compos… |
| **C098** | A | fact | active | THE FAUQUIER CLUSTER, TRANSPLANTED INTACT TO COOPER COUNTY, MISSOURI - verified against the transcription page image (evidence/1850_CooperCo_MO_p23_Ca… |
| **C099** | C | fact | active | THE STRONGEST STRUCTURAL CASE THE PROJECT HAS HELD - STILL GRADE C, BECAUSE NO DOCUMENT NAMES AARON'S FATHER. What is now established at A/B: (1) an e… |
| **C107** | C | hypothesis | active | THE FORK, STATED PLAINLY. Two coherent origin stories now stand, each with real evidence, and they are NOT compatible. (A) FAUQUIER: Aaron b. 1820 is … |
| **C108** | A | fact | active | AARON'S DEATH, FROM A CONTEMPORARY NEWSPAPER. Boonville Weekly Advertiser, 18 Jan 1878: 'Aaron Caton, an old and industrious citizen of Boonville, die… |
| **C110** | A | fact | active | THE STRONGEST EVIDENCE YET THAT JOSEPH IS AARON'S BROTHER - A CONTEMPORARY NEWSPAPER STATEMENT OF KINSHIP. Boonville newspaper, 1898: 'JOSEPH CATON, a… |

## All claims

| id | grade | type | lifecycle | pass | person | summary |
|---|---|---|---|---|---|---|
| C001 | A | fact | active | 4 | Theophilus Kitton | transported to Maryland 1675, one of 35 persons, by two London merchants |
| C002 | A | fact | active | 4 | Catherine Kitton | named in the will of John Acton |
| C003 | A | fact | active | 4 | Theophilus Kitton | planter; bought 'Grays Luck', 361 acres; Edward Kitton stated to be his son |
| C004 | A | fact | active | 5 | Thomas Kitten; Theophilus Kitten | adjacent households, recorded as Caton within a few years — documents the KITTEN->CATON name change |
| C005 | A | fact | active | 1 | Aaron Caton | IMAGE READ 12 Sep 2026 (first time in eleven passes). Delaware Co. marriage record book p.291: 'Aaron Caton & … |
| C006 | A | fact | active | 6 | Aaron Caton | household 1160/1163, Town of Delaware: Aaron 30 tailor b.Virginia; Sarah 26 b.Ohio; Julia 7 b.Missouri by the … |
| C007 | A | fact | active | 6 | Aaron Caton | enlisted Chillicothe MO, Co. E 2nd Missouri Volunteer Cavalry (Merrill's Horse); mustered out 19 Sep 1865. DAT… |
| ~~C008~~ | C | fact | superseded | 6 | William Bramwell Caton | DOWNGRADED A->C, see C026. Compiled service record index card retrieved. The claim that father Aaron gave writ… |
| C009 | B | fact | active | 6 | William Bramwell Caton | published biography; b.1847 Delaware Co. OH; founded Caton Marble Works, Winfield KS |
| ~~C010~~ | C | fact | reversed | 2 | Thomas Caton | EXCLUSION WITHDRAWN, SEE C073. Household on 1830 Ohio Co. VA p.209: 1 male 5-10, 1 male 30-39, 1 female <5, 1 … |
| C011 | A | fact | active | 6 | Harrison Caton | age 14, b. Virginia, in the Wheeling household of John Boring, bricklayer — apprentice or boarder, not a son. … |
| C012 | B | fact | active | 1 | Elizabeth Caton | married Alexander Gosney — proves adult Caton presence in Ohio Co. shortly before Aaron's birth. Gosney gone f… |
| C013 | A | negative | active | 6 | Aaron Caton | NEGATIVE: phrase search returns 0 results in all US newspapers digitised to 1963 |
| C014 | A | negative | active | 6 | Aaron Caton | NEGATIVE: not among the 12 'Caton' entries in the Missouri Union Provost Marshal index. One unresolved: 'Caton… |
| ~~C015~~ | C | fact | reversed | 6 | 1860 census, Livingston Co., MO | WRONG, SEE C043. Asserted that no free index exists for the 1860 Livingston Co. census and that NARA M653 roll… |
| ~~C016~~ | C | fact | reversed | 7 | Julia Caton | REVERSED, SEE C038 - Julia was born in MISSOURI, not Massachusetts. This claim asserted Massachusetts on the s… |
| C017 | A | fact | active | 7 | Nancy Caton | age 9/12 (b. c.Nov 1849), born Ohio, line 1 of p.179b. CORROBORATES the compiled claim of Nancy Roseman Caton … |
| C018 | A | fact | active | 7 | Mary E. Caton | age 5, born Ohio, attending school — b. c.1845. NEW daughter, absent from the ledger entirely. Brackets the re… |
| ~~C019~~ | C | fact | superseded | 7 | Aaron Caton | SUPERSEDED BY C039. The 'Massachusetts window c.1842-1844' does not exist; the window is MISSOURI. Retained as… |
| C020 | A | do-not-merge | active | 7 | Thos. H. / Theo. H. Caton | DO NOT MERGE. Age 35, b. Kentucky; wife Sarah E. 23, William 4, Henrietta 2, all b. Missouri. Roche Twp, PO Ro… |
| C021 | A | negative | active | 7 | Thos. F. Patton | NEGATIVE: line previously suspected as a young Caton reads PATTON, age 5, b. Missouri. Resolved, not a Caton |
| C022 | A | fact | active | 7 | 1860 census Boone Co., MO | REEL LOCATED: NARA M653 roll 608 (Bollinger and Boone). Boone begins ~image n200: n200 Rocky Fork Twp, n240-26… |
| C023 | A | fact | active | 8 | Aaron Caton | SERVICE CARD READ IN FULL. Pvt., Co. E, 2 Reg't Cav. Vols. (Merrill's Horse), Capt. Norville. Enlisted 15 Aug … |
| C024 | A | fact | active | 8 | William Bramwell Caton | SERVICE CARD READ IN FULL. Age 17, Pvt., Co. E, 2 Reg't Cav. Vols., Capt. Norville - same company and captain … |
| C025 | B | fact | active | 8 | Aaron Caton household | Direct line tied to BOONE COUNTY, MO by Oct 1862 - William enlisted at Sturgeon, which is in Boone Co. Bridges… |
| C026 | A | fact | active | 8 | William Bramwell Caton | REVISION TO C008. C008 asserted at grade A that 'father Aaron gave written consent for underage enlistment', c… |
| C027 | A | method | active | 8 | Massachusetts State Archives | ACCESS ROUTE, not a genealogical claim. Holds births, marriages and deaths for all Massachusetts cities and to… |
| C028 | C | negative | active | 8 | Julia Caton | NEGATIVE, WEAK - DOES NOT CLOSE T01. Open-web search for a Massachusetts birth record c.1842-1844 under Caton/… |
| C029 | C | negative | active | 8 | Aaron Caton | NEGATIVE, WEAK. No Caton/Catton/Caten/Cation/Eaton/Cason/Kitten tailor found in 1842-1844 city directories for… |
| C030 | A | negative | active | 8 | Roseman | NEGATIVE, SCOPED (T09 step 3). No Roseman/Rosman appears in either local 1850 transcription. SCOPE IS NOT COUN… |
| C031 | A | negative | active | 8 | Sarah Ann (Gardner) Caton | NEGATIVE, SCOPED (T03). No Gardner or Gardiner in the Delaware Township slice (file 3 of 5, households 1153-12… |
| C032 | A | fact | active | 8 | Harrison Caton | HOUSEHOLD COMPOSITION IN FULL, household 2253/2329, Ohio Co. (W)VA 1850: John Boring 34 b.Pa bricklayer $3,000… |
| C033 | C | hypothesis | active | 8 | Eliza Ann Boring | HYPOTHESIS, C-LEVEL, UNTESTED. Eliza Ann Boring (b. c.1819 Virginia) may be a CATON BY BIRTH and Harrison's si… |
| C034 | A | fact | active | 8 | Harrison Caton | REVISION TO C011. C011 asserts at grade A that Harrison is 'the ONLY Caton in the whole of Ohio County in 1850… |
| C035 | B | negative | active | 8 | Aaron Caton | DEAD END, RECORDED SO IT IS NOT RE-RUN. The two households immediately adjacent to Aaron's in 1850 both contai… |
| C036 | A | method | active | 8 | grep/ugrep on evidence/ files — po | MOVED TO METHOD.md s.1 ON 16 SEP 2026 - THIS CLAIM IS NOW A POINTER. Headline retained for the index and for t… |
| C037 | A | fact | active | 8 | Julia A. (Caton) Sawtell | DEATH CERTIFICATE, Missouri State Board of Health no. 36313, St. Louis City. Widow. DATE OF BIRTH 15 Dec 1843;… |
| C038 | A | fact | active | 8 | Julia Caton | REVERSES C016. JULIA WAS BORN IN MISSOURI, NOT MASSACHUSETTS. Three independent sources converge: the 1850 cen… |
| C039 | A | fact | active | 8 | Aaron Caton | REVISES C019. MIGRATION TIMELINE CORRECTED: m. Delaware Co. OH 8 Aug 1841; JULIA b. MISSOURI 15 Dec 1843; Mary… |
| C040 | A | fact | active | 8 | Aaron Caton | BIRTHPLACE VIRGINIA CONFIRMED BY A FAMILY INFORMANT. His daughter's 1916 death certificate states the father's… |
| C041 | A | fact | active | 8 | Aaron Caton | 1870 CENSUS, City of Boonville, Cooper Co., MO, enum. 6 June 1870, page 5 (stamped 348), PO Boonville, Ass't M… |
| C042 | A | fact | active | 8 | Julia A. Caton | IDENTITY LINK. Aaron's eldest daughter married S. G. Sawtell and remained in Cooper Co.; widowed by 1916; died… |
| C043 | A | fact | active | 8 | 1860 census, Livingston Co., MO | CORRECTS C015. A FREE INDEX DOES EXIST - FamilySearch indexes the 1860 federal census including Livingston Co.… |
| C044 | A | fact | active | 8 | Caton, H. / James Caton | RESOLVED BY C109: the child is HENRY CATON, d. 7 Nov 1880 at his sister Mrs. Sawtell's. UNRESOLVED IDENTITY. T… |
| C045 | A | other | moot | 8 | Massachusetts research thread | MOOT, NOT WRONG. C027 (MA State Archives holdings and its free five-image request route), C028 and C029 (negat… |
| C046 | A | hypothesis | active | 8 | Aaron Caton | STRATEGIC REFRAME. Aaron was in MISSOURI by December 1843 - twenty years earlier than any previously documente… |
| C047 | A | method | active | 8 | Caton surname, Missouri | FULL SWEEP of Missouri Death Certificates 1910-1975, surname Caton, all counties: 139 results retrieved and re… |
| C048 | B | hypothesis | active | 8 | Harrison Caton | LEAD FOR T06, IDENTITY UNCONFIRMED. Death certificate of CHARLEY CATON (cert 15118, Gentry Co., d. 11 May 1955… |
| C049 | B | fact | active | 8 | Cooper Co. Caton cluster | CONTEXT from the same sweep, for the do-not-merge work. Cooper Co. death certificates name two distinct 19th-c… |
| C050 | A | do-not-merge | active | 8 | Harrison Caton (Bates Co.) | DO NOT MERGE - RULED OUT FOR T06. 1880 census, Walnut Twp., Bates Co., MO, ED 148, dwelling 49/51: Harrison Ca… |
| C051 | A | negative | active | 8 | Harrison Caton (Gentry Co.) | NEGATIVE, AND IT DOES NOT REFUTE C048. No Caton household appears in Gentry Co., MO in the 1880 census. This i… |
| C052 | A | do-not-merge | active | 8 | Aaron F. Caton | DO NOT MERGE - IDENTIFIED. 1880 census, Otterville, Cooper Co., MO: Aaron Caton, head, AGE 44, b. c.1836 MISSO… |
| C053 | B | fact | active | 8 | Aaron Caton / Nancy Johnson marria | RESTORED 14 Sep 2026 (evening) - SEE C172: probably Aaron F.'s, as first held. The C151 reversal is withdrawn.… |
| C054 | B | fact | active | 8 | Aaron Caton | NARROWED BY C108: died Thursday 17 Jan 1878 at his residence on Sixth Street, Boonville (Boonville Weekly Adve… |
| C055 | A | fact | active | 9 | William Caton (Bates Co.) | 1860 census, Lebanon Twp., Bates Co., MO, enum. 9 Aug 1860, PO Fair Point, p.60. TWO ADJACENT CATON HOUSEHOLDS… |
| C056 | C | hypothesis | active | 9 | Aaron Caton | HYPOTHESIS, C-LEVEL, NOT IN THE WORKING TREE. A Maryland-born Caton kin-group may sit behind Aaron. Birth-stat… |
| C057 | C | fact | review | 9 | John Caton | REVIEW — NOT VERIFIED FROM THE PAGE. FamilySearch locates a John Caton household on 1840 Cooper County p.141 a… |
| C058 | A | method | active | 9 | 1840 census — a whole enumeration  | GAP CLOSED. Through eight passes this project did ZERO 1840 census work - 9 claims touched 1850, 6 touched 186… |
| C059 | A | fact | active | 9 | Jonas Caton; Joshua Caton | 1840 census, RIVES COUNTY, MISSOURI, p.367, division of William Lane. Two adjacent Caton heads of household: J… |
| C060 | B | method | active | 9 | Missouri Caton cluster | CLUSTER MAP, first time assembled. Missouri held MULTIPLE Caton households before Aaron arrived c.1843. 1840: … |
| C061 | A | fact | active | 9 | Joseph Caton | 1850 census, BRUNSWICK CITY, CHARITON CO., MISSOURI, p.236. Household: JOSEPH CATON, age 28 (b. c.1822), male,… |
| C062 | B | fact | active | 9 | Aaron Caton; Joseph Caton | UPGRADED C->B on 11 Sep 2026 by C110 (1898 newspaper: Joseph was 'the guest of his niece, Mrs. Sawtell' in Boo… |
| C063 | A | fact | active | 9 | Joseph Caten (Caton) | MARRIAGE RECORD. 'State of Missouri, County of Chariton. This is to certify that I B.H. Spencer a preacher of … |
| C064 | C | hypothesis | active | 9 | Aaron Caton | BEST CANDIDATE COUNTY FOR T10, grade C. CHARITON COUNTY, MISSOURI is now the leading place to look for the fam… |
| C065 | B | fact | active | 9 | Joseph Caton | CORROBORATED IN TWO COUNTY HISTORIES, independently of the census. (1) 'History of Howard and Chariton Countie… |
| C066 | A | negative | active | 9 | Caton surname at Wheeling | NEGATIVE, AND INFORMATIVE. Full-text search of the major county histories for the Wheeling area returns ZERO o… |
| C067 | A | fact | active | 9 | A. S. Caton | A SECOND CATON FAMILY IN AARON'S OHIO COUNTY. 'A. S. CATON, Secretary' of the Delaware Gaslight and Coal Oil C… |
| C068 | C | hypothesis | active | 9 | Andrew Caton | UNSOURCED ASSERTION IN BRIEF s.6 - FLAGGED, NOT REFUTED. BRIEF states 'Andrew Caton / New York line. Emma J. C… |
| C069 | A | method | active | 9 | American probate, guardianship, de | SECOND STRUCTURAL GAP, LARGER THAN THE 1840 ONE. An audit of claims.jsonl on 10 Sep 2026 found ZERO American p… |
| C070 | C | method | active | 9 | WikiTree Caton profiles | ASSESSED AND FOUND NOT USABLE AS EVIDENCE. Profiles Caton-5 (Aaron), Caton-8 (William Bramwell), Caton-14 (Tho… |
| C071 | B | fact | active | 9 | Thomas Caton | C010'S EXCLUSION SHOULD BE REOPENED. C010 rules Thomas Caton out as Aaron's father because his 1830 Ohio Co., … |
| C072 | C | fact | active | 9 | Aaron Caton family | THREE TESTABLE LEADS EXTRACTED FROM THE WIKITREE GEDCOM (all C-level until tested). (1) SARAH ANN GARDNER died… |
| C073 | A | fact | active | 9 | Thomas Caton | 1830 PAGE RE-READ - C010'S EXCLUSION IS UNSOUND. Ohio Co., VA, p.209, division of 'Timothy ___'. THE PAGE IS A… |
| C074 | A | fact | active | 9 | Thomas Caton (1820, county unknown | 1820 CENSUS PAGE, PRINCESS ANNE COUNTY, VIRGINIA - a Tidewater family, NOT the Wheeling Thomas. Household of T… |
| C075 | A | method | active | 9 | Aaron Caton | THE LARGEST UNEXAMINED ASSUMPTION IN THE PROJECT. 'WHEELING' IS UNSOURCED. Every record that states Aaron's bi… |
| C076 | A | fact | active | 9 | Joseph Caton | FULL OBITUARY, Marshall Republican (Marshall, Saline Co., MO), 27 May 1910, p.1, 'DEATHS' column. VERIFIED AGA… |
| C077 | B | hypothesis | active | 9 | Joseph Caton; Aaron Caton | CORROBORATED - UPGRADED C TO B. The obituary's 'FORKWARE county, Va.' (C076) is read as FAUQUIER COUNTY, VIRGI… |
| C078 | A | negative | active | 9 | Joseph Caton | NEGATIVE. No Missouri death certificate exists for Joseph Caton despite his dying 21 May 1910, after statewide… |
| C079 | B | negative | active | 9 | Caton in Fauquier Co., VA | WEAK NEGATIVE, SCOPED. 'Fauquier County, Virginia: Historical Notes' (1914) contains NO occurrence of Caton, C… |
| C080 | A | fact | active | 9 | Thomas Caton (1820, county pending | [RESTORED TO A, 18 Sep 2026 - the reel image is in evidence/ (1820_FauquierCo_VA_census_p46_ThosCaton_househol… |
| ~~C081~~ | C | fact | superseded | 9 | Aaron Caton | PREDICTION FAILED - SEE C082/C083. This claim proposed that the 1830 Fauquier census would show Thos. Caton wi… |
| C082 | A | fact | active | 9 | Caton households, Fauquier Co., VA | [RESTORED TO A, 18 Sep 2026 - the reel image is in evidence/ (1830_FauquierCo_VA_census_p471_Caton_households.… |
| C083 | B | hypothesis | active | 9 | Aaron Caton; Joseph Caton | REFRAMED QUESTION, replacing C081's failed prediction. ESTABLISHED: (a) Joseph Caton was born in Fauquier Co. … |
| C084 | A | method | active | 9 | Caton surname in Virginia | COMPLETE STATEWIDE MAP - Library of Virginia Chancery Records Index swept for the surname CATON across all 107… |
| C085 | A | method | active | 9 | 1840 Delaware Co., OH census — eve | 1840 DELAWARE CO., OHIO (T11) - ALL FREE TEXT ROUTES ARE CLOSED; DO NOT RE-DERIVE THIS. (1) Internet Archive p… |
| C086 | A | method | active | 9 | FamilySearch access on Spencer’s m | MOVED TO METHOD.md s.3 ON 16 SEP 2026 - THIS CLAIM IS NOW A POINTER. Headline retained for the index and for t… |
| C087 | A | fact | active | 10 | Fauquier Caton cluster | DIRECT PRIMARY COURT RECORD. A 4 Dec 1830 Fauquier County road order assigns the male road hands of Daniel Law… |
| C088 | C | hypothesis | active | 10 | Thomas Caton and Elizabeth Ann Law | [NOTE 18 Sep 2026: the AFH article was read in full - it adds that Benjamin Franklin Caton was born 1 Mar 1842… |
| C089 | A | negative | active | 9 | John Boring; Eliza Ann Boring | NEGATIVE, LIMITED. The West Virginia Vital Research Records Project's Ohio County marriage index contains no r… |
| C090 | A | fact | active | 10 | Thos Caton | COMPLETE IMAGE TRANSCRIPTION: 1840 Ohio County, Virginia, Thos. Caton. FamilySearch index p.46; original sched… |
| C091 | A | negative | active | 10 | Caton/Caten surname in the indexed | BOUNDED NEGATIVE. FamilySearch image group 007637475, Church Records, 1785-1954, Wheeling, West Virginia, cont… |
| C092 | A | fact | active | 10 | Fauquier Caton family | DIRECT PRIMARY MARRIAGE PAPERS DEFINE THE 1828-35 FAUQUIER CLUSTER. (1) In the William Caton–Ann F. Lawrey mar… |
| C093 | A | fact | active | 10 | Moses Caton | A NEW FAUQUIER CATON ADULT, c.1805-1819. Fauquier chancery 1820-011 (Exr. of John F. Carter v. John Evans; LVA… |
| C094 | A | fact | active | 10 | John N. Caton; Lawrey/Lawrie famil | THE CATON-LAWREY KIN NETWORK IN FAUQUIER. Chancery 1861-012 (Caton & wife & als. v. Bussey's Exor.; 40 scans r… |
| C095 | B | fact | active | 10 | John Caton (Cooper Co., MO) | 1850 RECORD: John Caton, 53, farmer, Cooper County, Missouri, District 23, p.268, household 902, enumerated 9 … |
| C096 | A | fact | active | 10 | Caton households, Cooper Co., MO,  | THREE CATON HOUSEHOLDS OF THREE DISTINCT ORIGINS. From the Cooper Co. MOGenWeb typed transcription of the 1850… |
| C097 | C | fact | active | 10 | William Caton (Cooper/Bates); Aaro | WILLIAM CATON OF COOPER 1850 = WM. CATON OF BATES 1860, AND HE IS AARON F. CATON'S FATHER. Cooper 1850: Willia… |
| C098 | A | fact | active | 10 | Fauquier Caton-Lawrey-Payne cluste | THE FAUQUIER CLUSTER, TRANSPLANTED INTACT TO COOPER COUNTY, MISSOURI - verified against the transcription page… |
| C099 | C | fact | active | 10 | Aaron Caton | THE STRONGEST STRUCTURAL CASE THE PROJECT HAS HELD - STILL GRADE C, BECAUSE NO DOCUMENT NAMES AARON'S FATHER. … |
| C100 | A | fact | active | 10 | Jesse Caton (Delaware Co., OH) | T11 RESULT - A NEW MAN, NOT THE MISSOURI JESSE. FamilySearch index of the 1840 census, Delaware Co., Ohio, sur… |
| C101 | C | fact | review | 10 | James Cayton (Delaware Co., OH) | REVIEW — SOURCE NOT LOCATED. The 11 Sep 2026 T11 summary reported a James Cayton household in Delaware County,… |
| C102 | B | fact | active | 10 | Caton households, Delaware Co., OH | 1850 Delaware County, Ohio FamilySearch index export (retained): the only Caton household indexed there is Aar… |
| C103 | B | fact | active | 10 | Phineas Caton | [CONFIRMED BY THE STONE 14 Sep 2026 - C185: the gravestone reads 'son of Aaron & Sarah Caton', died 17 Mar 184… |
| C104 | A | fact | active | 10 | James Caton (Delaware Co., OH) | The 1846 Delaware County, Ohio marriage return records James Caton and Tabitha Bockover: license 25 Aug, marri… |
| C105 | C | fact | active | 10 | Jesse Katon / Caton (Delaware Co.  | IDENTIFICATION WITHDRAWN 12 Sep 2026 - SEE C119. The Fairfield Co. Jesse Katon had a 15-year-old son in 1850, … |
| C106 | B | fact | active | 10 | James Cayton (Clayton County, Iowa | 1850 FamilySearch index export (retained) identifies James Cayton, indexed as Cazton, age 46 and born Pennsylv… |
| C107 | C | hypothesis | active | 10 | Aaron Caton | THE FORK, STATED PLAINLY. Two coherent origin stories now stand, each with real evidence, and they are NOT com… |
| C108 | A | fact | active | 10 | Aaron Caton | AARON'S DEATH, FROM A CONTEMPORARY NEWSPAPER. Boonville Weekly Advertiser, 18 Jan 1878: 'Aaron Caton, an old a… |
| C109 | A | fact | active | 10 | Henry Caton | RESOLVES C044 - THE 1860 'JAMES' AND 1870 'H.' IS HENRY CATON, AND HE DIED IN 1880. Obituary, Boonville, Nov 1… |
| C110 | A | fact | active | 10 | Joseph Caton; Julia A. (Caton) Saw | THE STRONGEST EVIDENCE YET THAT JOSEPH IS AARON'S BROTHER - A CONTEMPORARY NEWSPAPER STATEMENT OF KINSHIP. Boo… |
| C111 | A | fact | active | 10 | Julia A. (Caton) Sawtell; Solomon  | JULIA'S MARRIAGE AND WIDOWHOOD. Married 30 MARCH 1869, Cooper Co., MO, to SOLOMON GIBSON SAWTELL/SAWTELLE - th… |
| C112 | A | fact | active | 10 | Joseph Caton (tailor) | JOSEPH'S FULL DOCUMENTED PROFILE, extending C061/C065/C076. 1850 SLAVE SCHEDULE, Chariton Co.: Joseph Caton ow… |
| C113 | C | hypothesis | active | 10 | WikiTree GEDCOM '124-DeCoursey.ged | LEAD, C-LEVEL, POSSIBLY IMPORTANT. The WikiTree profiles for Aaron, Sarah Ann, William B. and Thomas Caton all… |
| C114 | B | fact | active | 10 | Sue (Caton) Dumm | ARCHIVAL TARGET - JOSEPH'S DAUGHTER LEFT FAMILY-HISTORY MATERIAL. Susan Caton (b. c.1859, C112) married a Dumm… |
| C115 | A | method | active | 10 | Conflicts between the two threads | THREE DISCREPANCIES BETWEEN THE CHATGPT HANDOFF AND THE FILE, RECORDED NOT RESOLVED. (1) 1860 LIVINGSTON TOWNS… |
| C116 | B | method | active | 10 | Collateral Missouri Catons | COLLATERAL FROM THE HANDOFF, QUARANTINED. (a) 1866 LAMINE TWP VOTER LIST, Cooper Co.: 'Aaron Caton' and 'Josep… |
| C117 | A | method | active | 10 | ChatGPT handoff of 11 Sep 2026 — r | THE CHATGPT HANDOFF WAS WRITTEN WITHOUT READING THE CURRENT FILE. It still carries 'reportedly Wheeling' as th… |
| C118 | A | fact | active | 10 | Sue (Caton) Dumm papers — request | RECORDS REQUEST SENT 12 Sep 2026 by Spencer to the Carnegie Library for Local History, Boulder Public Library,… |
| C119 | A | fact | active | 10 | Jesse Katon (Fairfield Co., OH) | 1850 census, Rush Creek Twp, FAIRFIELD CO., OHIO, 17 Sep 1850, p.428, dwelling 289 (image retained): JESSE KAT… |
| C120 | A | fact | active | 11 | “The Alexandria Catons” import, 12 | OUTSIDE-WORKSPACE COMPILATION RECONCILED. A research file 'The Alexandria Catons' (PDF, compiled 12 Sep 2026, … |
| C121 | B | fact | active | 11 | Nathan T. Caton; George W. Caton;  | PUBLISHED BIOGRAPHY, VERIFIED AGAINST THE OCR TEXT. 'Hon. Nathan T. Caton', An Illustrated History of the Big … |
| C122 | A | fact | active | 11 | George W. Caton (Boonville tailor) | GEORGE W. CATON WAS THE TAILOR OF BOONVILLE IN THE 1830s, AND A CHARTER MASON THERE IN 1841 BESIDE A LAURIE. H… |
| C123 | B | fact | active | 11 | George W. Caton household, 1850 | 1850 CENSUS, ST. CLAIR CO., MISSOURI, AS TRANSCRIBED IN THE IMPORT (C120) - IMAGE NOT YET SEEN HERE, so B pend… |
| C124 | C | fact | active | 11 | Aaron Caton - origin hypotheses | THE ALEXANDRIA THREAD IS NOT A THIRD FORK; IT IS A CANDIDATE EXTENSION OF STORY A. Put C121-C123 beside the Fa… |
| C125 | A | negative | active | 11 | Irish Revolutionary grandfather (u | NEGATIVE, BOUNDED. The 1841 'Census of Pensioners for Revolutionary or Military Services' (the 1840 census pen… |
| C126 | A | fact | active | 10 | Daniel Laurie — 1840 search | MISDIRECTED SEARCH, RECORDED SO IT IS NOT REPEATED. FamilySearch 1840, Ohio, 'Daniel Laurie' returned only fuz… |
| C127 | B | fact | active | 10 | BRIEF s.5 England-Maryland chain | IMPLICATION OF C121/C124 NOT YET STATED: IF THOMAS CATON SR. OF FAUQUIER WAS IRISH-BORN, THE ENTIRE ENGLAND-MA… |
| C128 | A | fact | active | 11 | William Caton; Thomas Caton; N. La | 1840 CENSUS, COOPER CO., MO, p.145 - IMAGE READ AGAINST THE PRINTED HEADER (evidence retained). WM CATON: male… |
| C129 | A | fact | active | 11 | George W. Caton household, Cooper  | 1840 CENSUS, COOPER CO., MO, p.135 - 'GEO W CATON', IMAGE READ AGAINST THE PRINTED HEADER (evidence retained; … |
| C130 | A | negative | active | 11 | Irish Revolutionary grandfather (C | BOUNDED NEGATIVE FOR GEORGE W. CATON'S OWN HOUSEHOLD ONLY. The retained 1840 Cooper County p.135 image (C129) … |
| C131 | A | fact | active | 11 | Jesse Caton, Delaware Co., OH, 184 | IMAGE NOW RETAINED for the 1840 Delaware Co., Ohio Jesse Caton household reported from the index in C100: enum… |
| C132 | A | negative | active | 11 | Thomas Caton Sr. (Fauquier) - prob | NEGATIVE. FamilySearch collection 'Probate & Court, Virginia, Wills and Deeds, ca. 1700s-2017', searched Thoma… |
| C133 | A | fact | active | 11 | Michael Caton household, Washingto | 1820 CENSUS, THIRD WARD, WASHINGTON CITY, D.C. (M33 roll 5; James Carlon's division) - IMAGE READ 12 Sep 2026.… |
| C134 | A | fact | active | 11 | George W. Caton; Michael Caton; Ed | GEORGE W. CATON, TAILOR, LIVED IN WASHINGTON CITY, NOT ALEXANDRIA, IN 1827-1830 - and the Alexandria import se… |
| C135 | B | fact | active | 11 | Aaron Caton - the 1820 test across | THE 1820 CENSUS HAS NOW BEEN READ IN EVERY JURISDICTION EITHER STORY NAMES, AND ONLY ONE HOUSEHOLD HOLDS A CAT… |
| C136 | A | fact | active | 11 | Thomas Caton, printer; Patrick Cat | THE WASHINGTON CATONS WERE A PRINTING-TRADES FAMILY, AND THEY PERSIST. 1850 Washington Directory (archive.org … |
| C137 | A | fact | active | 11 | CORRECTION to C093 / evidence Fauq | THE 'MR. CATON WHO RECEIVED THE MARES' IN FAUQUIER CHANCERY 1820-011 IS A MISREADING OF CARTER, AND THERE IS N… |
| C138 | B | negative | active | 11 | Thomas Caton Sr. (Fauquier) - prob | NEGATIVE, REPORTED (no image retained). Spencer paged the volume indexes of Fauquier Co. Will Books v.13-14 (1… |
| C139 | B | fact | active | 11 | Thomas Caton (1767-1838), Tyler/We | A THOMAS CATON, b. Oct 1767, d. 8 Jan 1838, IS BURIED AT WILLIAMS CEMETERY, NEW MARTINSVILLE, WETZEL CO., WV (… |
| C140 | A | negative | active | 11 | Caton households, Tyler Co., VA, 1 | NEGATIVE, FROM THE IMAGES. 1820 census, Tyler Co., Virginia (NARA M33 reel 140, images 147-163 on archive.org;… |
| C141 | B | negative | active | 11 | Caton - Delaware Co., Ohio probate | NEGATIVE, REPORTED. FamilySearch 'Ohio, Probate Records, 1789-1996' > Delaware > 'Probate records 1808-1851 Ab… |
| C142 | B | negative | active | 11 | Caton - Delaware Co., Ohio Common  | NEGATIVE, REPORTED. Delaware Co., Ohio, General Index to Common Pleas judgments (film 505926 / DGS 7712046; pl… |
| C143 | B | fact | active | 11 | New Martinsville Catons - 1830 cen | THE NEW MARTINSVILLE CATON FAMILY (C139) HAS NO 1830 CENSUS HOUSEHOLD UNDER THE SURNAME. FamilySearch 1830 ind… |
| C144 | A | fact | active | 11 | Aaron Caton; Sarah (Gardner) Caton | AARON'S FIRST DEED, FOUND BY FAMILYSEARCH FULL-TEXT SEARCH. Delaware Co., Ohio, Recorder (DGS 007842562, image… |
| C145 | A | fact | active | 11 | Aaron Caton; James A. Asher; Hecto | AARON IN THE TOWN OF DELAWARE, MAY 1846, A RENTER IN DEBT. Delaware Co., Ohio, Recorder (DGS 008140352, image … |
| C146 | A | fact | active | 11 | Aaron Caton - Delaware Co., Ohio c | AARON'S DELAWARE COUNTY COURT FOOTPRINT, FOUND BY FAMILYSEARCH FULL-TEXT SEARCH (five images retained). (1) AP… |
| C147 | C | method | active | 11 | Abel Caton family, Dorchester Co., | COLLATERAL LEAD, NOT CONNECTED TO AARON. Washington City newspaper notice, Nov 1851 (Spencer's clipping, 14 Se… |
| C148 | A | method | active | 11 | J. J. Caton (b. c.1837); Daniel R. | COLLATERAL. Missouri Adjutant General, Enrolled Missouri Militia enrollment list, Cooper Co., 1862 (DGS 008723… |
| C149 | A | fact | active | 11 | William Caton & Ann F. (Lawrey) Ca | THE DOCUMENT THAT NAMES WILLIAM CATON'S CHILDREN - AND IT DOES NOT INCLUDE OUR AARON. Cooper Co., MO, Circuit … |
| C150 | A | method | active | 11 | Aaron F. Caton and children Henry, | COLLATERAL - AARON F., NOT OURS. Cooper Co. Circuit Court, February term, 12 Feb 1875, p.444 (DGS 008483715 im… |
| ~~C151~~ | B | fact | reversed | 11 | Aaron Caton; Nancy (Johnson) Caton | REVERSED 14 Sep 2026 (evening) - SEE C172: Nancy Jane (Johnson) Caton's 1936 obituary shows she married Aaron … |
| C152 | B | fact | active | 11 | Nancy Caton (prob. Aaron's daughte | MARRIAGE: 'Married in Cooper County, Mo., on the 20th day of August 1869, Mr. TAYLOR O'NEAL and Miss NANCY CAT… |
| C153 | B | fact | active | 11 | Aaron Caton (fl. 1795), Prince Wil | AN AARON CATON, ADULT, IN PRINCE WILLIAM CO., VIRGINIA, IN 1795 - A GENERATION BEFORE OURS AND TWENTY MILES FR… |
| C154 | B | fact | active | 11 | Aaron Caton and Moses Caton - Prin | [FATHER-AND-SON READING WITHDRAWN 14 Sep 2026 - SEE C157: Aaron was 26-45 in 1810, so of Moses's generation; b… |
| C155 | A | negative | active | 11 | Caton households, Prince William C | NEGATIVE, FROM THE IMAGES. 1820 census, Prince William Co., Virginia (NARA M33 reel 130, images c.440-500 on a… |
| C156 | B | fact | active | 11 | Caton tithables, Fauquier Co., VA, | THE FAUQUIER TAX RUN, 1800-1832, FROM THE FAMILYSEARCH FULL-TEXT RESULT LIST (17 hits, 'Caton', Fauquier, tax … |
| C157 | B | fact | active | 11 | Aaron Caton (the elder) - 1810 cen | 1810 CENSUS, PRINCE WILLIAM CO., VA, p.[52]6 (image retained; Spencer via FamilySearch 14 Sep 2026): 'AARON CA… |
| C158 | B | method | active | 11 | William Caton of Annapolis, keeper | COLLATERAL, FOR T14 (George W. Caton's father), NOT FOR AARON. Chronicling America, Alexandria Daily Gazette: … |
| C159 | B | fact | active | 11 | Thomas Caton Sr. - 1810 census, Fa | [NOTE 18 Sep 2026: reading (3) - the death and remarriage between 1810 and 1820 - is one of two readings; C207… |
| C160 | B | method | active | 11 | Jackson Caton (d. c.1845) and Some | COLLATERAL - MORE CATONS ACROSS THE RIVER FROM BOONVILLE IN THE 1840s. Chronicling America, Boon's Lick Times … |
| C161 | B | fact | active | 11 | 'Moses Caton Chapline' of Wheeling | RED HERRING RESOLVED. Chronicling America, Wheeling Times and Advertiser, 16/22/27 Mar 1848: Ohio Co. chancery… |
| C162 | B | fact | active | 11 | Moses B. Caton (1767-1839), Rosevi | [RAISED C->B 14 Sep evening by C164: George Wesley Caton's wife Mildred Buckley was a Fairfax Co. heir and the… |
| C163 | B | negative | active | 11 | Thomas Caton Sr. (Fauquier) - grav | NEGATIVE + A SIDE NOTE. Find a Grave search, Thomas Caton d. 1837-1867 (all locations, 14 Sep 2026): NO Thomas… |
| C164 | B | fact | active | 11 | George W. Caton & Mildred (Buckley | THE MUSKINGUM CATONS CAME FROM FAIRFAX COUNTY, VIRGINIA - PROVED BY A CHANCERY CAUSE, AND IT PULLS MOSES B. CA… |
| C165 | A | fact | active | 11 | Moses Caton household, Fairfax Co. | 1820 CENSUS, FAIRFAX CO., VA, p.507 (district 'No. 11'; NARA M33 reel 137 image 71 on archive.org, bottom page… |
| C166 | A | fact | active | 11 | Moses, William G. and John R. Cato | 1830 CENSUS, FAIRFAX CO., VA (NARA M19 reel 201 on archive.org; name-side images 455-549 scanned by name colum… |
| C167 | A | negative | active | 11 | Caton households, Prince William C | NEGATIVE, FROM THE IMAGES. 1830 census, Prince William Co., VA (NARA M19 reel 196 on archive.org; the county i… |
| C168 | A | fact | active | 11 | William G. Caton - deponent, Fairf | THE FAIRFAX CATONS WERE STILL IN FAIRFAX, AT CENTREVILLE, IN SEPTEMBER 1835 - which dates their move to Ohio t… |
| C169 | B | fact | active | 11 | Aaron Caton - HEAD OF HOUSEHOLD in | AN 'AARON CATON' IS A HEAD OF HOUSEHOLD SOMEWHERE IN OHIO IN 1840. Internet Archive full-text search (be-api.u… |
| C170 | B | fact | active | 11 | Harriet Caton, dau. of Moses, m. P | INDEPENDENT CONFIRMATION THAT MOSES B. CATON OF MUSKINGUM WAS THE MOSES CATON OF FAIRFAX. Daughters of the Ame… |
| C171 | C | fact | active | 11 | Colonial Catons of Northern Virgin | LEADS FOR THE GENERATION ABOVE THE BROAD RUN BROTHERS, FROM ARCHIVE.ORG FULL-TEXT SNIPPETS (the books are lend… |
| C172 | A | fact | active | 11 | Nancy Jane (Johnson) Caton Blevins | THE 1869 NANCY JOHNSON MARRIAGE IS AARON F.'S AFTER ALL, AND SHE STAYED HIS WIFE UNTIL HE DIED - SO THE 1871 D… |
| C173 | B | fact | active | 11 | Caton marriage bonds, Fauquier Co. | THOMAS SR.'S SECOND MARRIAGE WAS NOT BONDED IN FAUQUIER. John K. Gott, Fauquier County, Virginia Marriage Bond… |
| C174 | B | fact | active | 11 | Rosana Caton - Reading Twp, Perry  | [MOSES'S-WIDOW READING WITHDRAWN 14 Sep, same evening: Perry County Chapter OGS, Reading Township Cemeteries v… |
| C175 | B | fact | active | 11 | Caton - Northern Virginia will abs | NEGATIVES FROM ARCHIVE.ORG FULL-TEXT SEARCH (14 Sep 2026, lending-restricted books searched by snippet): NO Ca… |
| C176 | B | fact | active | 11 | Caton Family Cemetery, Somerville, | TWO MORE NEGATIVES, ONE SMALL POSITIVE (archive.org full-text snippets, 14 Sep 2026). (1) Baird, Fauquier Coun… |
| C177 | B | negative | active | 11 | Caton - Prince William Co. will bo | NEGATIVE, DECISIVE FOR ONE TEST. Peters, Prince William County, Virginia, General Index to Wills, 1734-1951 (2… |
| C178 | B | fact | active | 11 | Rev. Titus Case, M.G. - officiant  | THE 1841 OFFICIANT IDENTIFIED (B12 closed). 'Titus Case, M.G.', who returned Aaron Caton's marriage to Sarah A… |
| C179 | C | fact | active | 11 | Thomas Caton of Frederick Co., Va. | ORIGIN HYPOTHESIS, UNTESTED (grade C) - EXTENDS C171 (Capt. Thomas Caton of Opequon Creek, Frederick Co., 1750… |
| C180 | C | fact | active | 11 | Thomas Caton - letter at the Alexa | SMALL FINDS, 14 Sep 2026 evening sweep. (1) Phenix Gazette (Alexandria), 3-5 May 1830, list of letters remaini… |
| C181 | B | fact | active | 11 | Moses B. Caton Jr. (14 Jan 1811 -  | MOSES'S 1820 HOUSEHOLD IS FULLY ACCOUNTED FOR WITHOUT AARON. Find a Grave 41210338 (Caton Cemetery, Webster Co… |
| C182 | B | fact | active | 11 | Caton - Culpeper marriages 1781-18 | THREE MORE BOUNDED NEGATIVES (archive.org full-text API, identifier-scoped, Caton and the variants Cayton/Cate… |
| C183 | A | fact | active | 11 | George W. Caton household, Newton  | 1840 CENSUS, MUSKINGUM CO., OHIO, READ FROM THE REEL (NARA M704 roll 418, archive.org populationsc18400418unit… |
| C184 | B | fact | active | 11 | Aaron Caton, Pvt., Co. E, 2nd Mo.  | THE 'DIFFERENT SOLDIER' READING OF THE PENSION CARD DOES NOT SURVIVE A UNIT CHECK. T04 (10 Sep) found one Aaro… |
| C185 | A | fact | active | 11 | Phineas Caton (c.5 Apr 1842 - 17 M | C103 CONFIRMED AND RAISED TO A: THE STONE NAMES THE PARENTS. Find a Grave 21386384, Powell Cemetery, Powell (L… |
| C186 | B | fact | active | 11 | Sarah Ann (Gardner) Caton's family | SARAH ANN'S PARENTS AND SIBLINGS IDENTIFIED (grade B - no document names her father; four independent records … |
| C187 | A | fact | active | 11 | Moses Caton at Centreville, July 1 | MOSES PLACED AT CENTREVILLE A MONTH BEFORE THE 1820 CENSUS, AMONG THE FAMILIES HIS CHILDREN MARRIED INTO. Alex… |
| C188 | A | fact | active | 11 | Caton - 1820 census of Culpeper an | THE ELDER AARON HEADED NO HOUSEHOLD IN CULPEPER OR STAFFORD IN 1820. Read from the NARA M33 reels on archive.o… |
| C189 | B | fact | active | pass12 | Daniel Laurie / Catherine Laurie | COCHRAN/JEFFRESS BOOK CONFIRMS LAURIE FAMILY'S OHIO STOP AND FAUQUIER ORIGIN. Catherine Laurie born 'probably … |
| C190 | B | fact | active | pass12 | Thomas Caton (colonial) | COLONIAL THOMAS CATON OF FREDERICK COUNTY, VIRGINIA — NORTHERN NECK LANDHOLDER, GENTLEMAN, JUSTICE, AND MILITI… |
| C191 | B | fact | active | pass12 | George W. Caton / Joseph Caton | 1883 HISTORY OF HOWARD AND COOPER COUNTIES NAMES GEORGE W. CATON 'THE TAILOR' AMONG EARLY BOONVILLE TRADESMEN … |
| C192 | A | fact | active | 13 | Thomas Caton household, Fauquier C | C080 IS ANOMALOUS ON THE 1820 FORM AND MUST BE RE-READ FROM THE IMAGE. [CORRECTED 16 Sep, same day: this claim… |
| C193 | A | fact | active | 13 | Thomas Caton Jr. and Thomas Caton  | [UPDATE 18 Sep 2026: resolution (a) is DEAD - the 1830 image shows 'Jun' in the 20-30 column beyond doubt (C20… |
| ~~C194~~ | C | hypothesis | reversed | 13 | Thomas Caton Jr. (William’s father | [DEAD AS FRAMED, 18 Sep 2026: the kill condition stated below - 'the 1830 bracket reads 20-30' - is met from t… |
| C195 | B | fact | active | 13 | Aaron and Joseph Caton - Virginia  | THE UNTRIED RECORD CLASS, AND A COUNTY-BY-COUNTY SURVIVAL SURVEY. ARGUMENT: Aaron (10) and Joseph (7) are in N… |
| C196 | A | fact | active | 13 | PARENTAGE-TESTS A1 - Fauquier pers | [CORRECTED 18 Sep 2026 - PREMISE FALSIFIED BY C201. The Fauquier tax originals show Cayton Thomas and William … |
| C197 | C | fact | active | 13 | Nancy Roseman Caton - the T09 nami | T09 RESTS ON AN UNSOURCED MIDDLE NAME, AND THE SURNAME READING POINTS THE WRONG WAY. C017 corroborates a Nancy… |
| G001 | A | fact | active | pass12 | Aaron Caton (elder; deceased by 18 | Rappahannock County Deed Book A, image 192 (printed page 305), contains an 8 April 1834 deed of release from J… |
| G002 | B | fact | active | pass12 | William Caton (unidentified; descr | Fauquier County Deed Book 25, image 55 (handwritten page 87), is part of a trust deed dated 31 August 1820 fro… |
| G003 | A | fact | active | pass12 | Fauquier Caton/Cayton tax test, 18 | Crop-first review of the FamilySearch Fauquier personal-property-tax film DGS 007849111 found separate handwri… |
| G004 | B | fact | active | pass12 | Unidentified Caton payee in Turner | Fauquier probate image 16 of DGS 007676139 contains a handwritten 1820 account headed 'The Estate of Turner Di… |
| G005 | C | fact | active | pass13 | Culpeper probate indexed-layer tes | Authenticated FamilySearch Full-Text searches of Culpeper mixed probate groups DGS 4022221, 7644389, and 76443… |
| G006 | A | fact | active | pass13 | Moses Caton, Sr., Muskingum County | The Muskingum County probate administrative-docket index, DGS 104066994 image 12 of 116 (printed page 18), lis… |
| G007 | C | fact | active | pass14 | Caton/Cayton spelling variants in  | Authenticated FamilySearch exact-surname searches in United States, Census, 1820 and 1830, place Virginia, ret… |
| G008 | C | fact | active | pass14 | Culpeper public will-abstract and  | The online FamilySearch volume Culpeper County, Virginia, will abstracts (identifier 2536133, 221 viewer pages… |
| G009 | A | fact | active | pass14 | Thomas Caton and Mary Balentine, 1 | FamilySearch record details identify a 28 June 1809 marriage of Thomas Caton and Mary Balentine, but the origi… |
| G010 | B | fact | active | pass14 | Culpeper printed marriage list, 17 | Raleigh Travers Green's public-domain *Genealogical and Historical Notes on Culpeper County, Virginia* states … |
| G011 | A | fact | active | pass15 | Mary E. Caton and John C. Foushee, | The direct FamilySearch Reel 50 surname index image 32 reads `Caton, Mary E., 37` and also gives the cross-ref… |
| G012 | C | fact | active | pass15 | Culpeper Reel 50 focused 1816–1819 | Direct review of FamilySearch Reel 50 image 194, whose printed page markers are 15–16, found the visible 1815–… |
| ~~G013~~ | A | fact | void | pass16 | Aaron Caten, pension-index card ap | VOID — the retained original T288 card was misread in the prior claim. It reads `Caten, Aaron`, service `E. 2 … |
| G014 | B | fact | active | pass16 | Prince William County marriage-adj | The Library of Virginia Prince William County microfilm inventory lists Bond Book, 1815–1826 and Bond Book, 18… |
| G015 | C | fact | active | pass16 | Fauquier post-1835 elder-generatio | The Library of Virginia Fauquier County microfilm guide lists Will Books 14–18 (1835–1844), Order Books 1836–1… |
| G016 | B | fact | active | pass16 | Sue Caton Dumm, Boulder family-his | The Carnegie Library for Local History public catalog identifies `Historical data record: Dumm family, 1932`, … |
| G017 | C | fact | active | pass16 | Delaware County, Ohio, 1835–1838 L | The targeted public Delaware County, Ohio, 1835–1838 search located no verified deed, tax duplicate, court rec… |
| G018 | C | fact | active | pass16 | Family-Bible surname tree, isolate | The supplied family-Bible surname tree independently repeats Gardner and likely Blankenmeister, both already d… |
| G019 | B | negative | active | 17 | James Cayton 1840 FamilySearch loc | On 16 Sep 2026, an exact FamilySearch Residence Place search for James Cayton in Delaware County, Ohio, in the… |
| C201 | A | fact | active | 14 | Thomas Caton Sr., Thomas Caton Jr. | FAUQUIER TAX ORIGINALS READ YEAR BY YEAR (Codex packet of 17 Sep 2026, recovered 18 Sep; images SHA-verified).… |
| C202 | A | method | active | 14 | T13 - Fauquier guardianship locato | WRONG-COUNTY LOCATOR REMOVED FROM T13. The task file cited FamilySearch catalog 642321 (film 1689208 / DGS 868… |
| C203 | B | fact | active | 14 | Thomas Caton households, Fauquier  | USGENWEB TRANSCRIPTIONS REPRODUCE C159 AND C080 AND BOUND THE 1830 GAP. (1) 1810 (Jan Carter/Sandy Onbey, 2002… |
| C204 | A | fact | active | 14 | Fauquier Co. record series - LVA R | TWO FAUQUIER SERIES CONFIRMED FROM THE LVA GUIDE, NEITHER YET OPENED. (1) Reel 44, '(Superior Court of Law) De… |
| C205 | B | fact | active | 14 | Thomas Caton (77, tailor) and Jame | TWO VIRGINIA-BORN CATONS IN THE 1850 COOPER TRANSCRIPTION WHO ARE NOT IN THE PROJECT'S CURRENT MODEL, AND ONE … |
| C206 | A | fact | active | 14 | Thos Caton Snr and Thos Caton Junr | TWO THOMAS CATONS IN COOPER COUNTY BY 1846, FROM THE IMAGES (Codex, 17 Sep 2026; recovered 18 Sep). (1) Cooper… |
| C207 | C | hypothesis | active | 14 | Thomas Caton Sr.'s wife in 1810 an | HYPOTHESIS, C-LEVEL. C159 reads the 1810 Fauquier household (M 45+, F 16-26, F 45+) as Thomas, his wife (45+) … |
| C208 | A | fact | active | 14 | Thomas Caton Sen, Thomas Caton Jun | THE RE-READ PARENTAGE-TESTS 0 ASKED FOR - DONE FROM THE RETAINED IMAGE, AND C082 IS CONFIRMED IN EVERY CELL. S… |
| C209 | A | fact | active | 14 | Thos. Caton - Fauquier 1820 p.46,  | THE SECOND RE-READ OF PARENTAGE-TESTS 0 - DONE FROM THE RETAINED IMAGE; C080 CONFIRMED CELL BY CELL, ANOMALY I… |
| C210 | A | fact | active | 14 | Thomas Caton, Wm Caton, Thos Caton | TWO COURT-BOOK PAGES FROM SPENCER'S 17 SEP CAPTURES, READ 18 SEP. (1) Fauquier County Court, continued and hel… |
| G020 | A | fact | active | pass17 | Aaron Caten / Aaron Caton | The retained original NARA T288 card reads `Caten, Aaron`; service `E. 2 Mo. Cav.`; Invalid application `23378… |
| G021 | B | hypothesis | active | pass17 | Aaron Caton | The 1876 `Aaron Caten` invalid pension application 233783 is likely the direct-line Aaron’s: `E. 2 Mo. Cav.` m… |
| G022 | A | fact | active | pass17 | Thomas Caton, age 77, Boonville ho | The original 1850 census records Thomas Caton, male, age 77, occupation “Taylor,” born Virginia, within John P… |
| G023 | A | do-not-merge | active | pass17 | Thomas Caton, age 40, District 23  | The original 1850 Cooper County census separately records Thomas Caton, age 40, Kentucky-born farmer in Distri… |
| G024 | A | fact | active | pass17 | Joseph Caton; unidentified Mrs. Sa | The 11 March 1898 Boonville notice says Joseph Caton, a former citizen who left Boonville in 1847, was visitin… |
| G025 | A | fact | active | pass17 | Mary Sawtell; Gip Sawtell | An 18 March 1898 Boonville item identifies Gip Sawtell as the guest of his mother, Mrs. Mary Sawtell, document… |
| G026 | A | fact | active | pass17 | Joseph Caton, tailor, reported bor | Joseph’s contemporary 1910 obituaries conflict on birthplace: The Brunswicker says Fairfax County, Virginia, w… |

## Unresolved discrepancies and identity checks

Alternatives and claim/source links are canonical in `discrepancies.jsonl`. Identity checks are not automatically conflicts between one person's records.

| id | status | record type | topic | next action |
|---|---|---|---|---|
| D-003 | open | discrepancy | Aaron F. Caton's 1886 death report and identity | Locate and compare the original death and newspaper records; do not merge solely on name. |
| D-004 | provisional | discrepancy | Julia Sawtell's mother's birthplace | Seek an independent record naming Sarah Gardner's birthplace or family of origin. |
| D-005 | unresolved | identity_check | William Caton in the 1850 Cooper and 1860 Bates censuses | Compare the full household members, migration path, and independent records before merging. |
| D-009 | unresolved | discrepancy | 1840 Delaware County James Cayton source locator | Recover the exact index URL, source citation, or Delaware County page underlying C101; then verify head, locality, and age columns before restoring normalized counts or using the claim. |
| D-010 | open | discrepancy | 1810 Fauquier Thomas Caton household - relationship of the two women | Search Fauquier and Prince William marriage bonds for Thomas Caton BEFORE 1810 (c.1795-1809) as well as 1811-19; any bond dated 1811-19 kills C207. |
| D-012 | open | identity_check | Who is 'Thomas Caton Jr', William Caton's consenting father of 6 Dec 1828 (C092), given that the 1830 'Thomas Caton Jun' is a male 20-30 (C208)? | Find the loose original 1828 consent (Fauquier marriage bonds vol. 7 is the original-record volume per T17's catalog note) or any pre-1933 abstract; read the 1828 tax list (C201: Thomas, William, Thomas Jr all separate) for property columns; confirm the 1820 male 16-18 (C209) as the later Jun. |
| D-014 | open | identity_check | Identity and kinship route of Joseph Caton’s unnamed niece, Mrs. Sawtell (1898) | Compare Sue Caton Dumm’s 1932 record and other descendant-level records for explicit Joseph siblings or an identified niece; do not treat the notice as proof of a Joseph–Aaron sibling link. |
| D-015 | open | identity_check | Joseph Caton’s reported Virginia birthplace, 1910 obituaries | Use the 1932 Sue Caton Dumm pages or a primary birth/migration record to identify Joseph’s parents and origin. |
| D-016 | open | identity_check | Whether the 1850 Boonville Thomas Caton, age 77, is the proposed Fauquier elder | Examine Cooper County probate Inventory of Names, vol. A, 1849–1900, Missouri State Archives reel C1997, for explicit relatives or prior residence. |
