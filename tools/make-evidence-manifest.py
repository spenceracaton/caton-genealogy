#!/usr/bin/env python3
"""Regenerate evidence/README.md: every file, which claims cite it, and a note.
   python3 tools/make-evidence-manifest.py"""
import json, pathlib, datetime, re
root = pathlib.Path(__file__).resolve().parent.parent
ev = root/"evidence"
rows = [json.loads(l) for l in (root/"claims.jsonl").open() if l.strip()]

NOTES = {
 "1840_PerryCo_OH_ReadingTwp_RosanaCaton_household.jpg": "1840 Perry Co. OH: Rosana Caton, M 20-30 x2, F 5-10, F 60-70 - Moses's widow? (C174).",
 "1936_1956_SedaliaDemocrat_NancyJane_Johnson_Caton_Blevins_and_Jennie_Baslee_obits.txt": "Nancy Jane (Johnson) Caton Blevins obit 1936 and Jennie Baslee obits 1956 - the 1869 marriage and 1871 divorce are Aaron F.'s (C172).",
 "Fairfax_1836-004_LVA_Cornwell_v_Moore_WmGCaton_deposition.zip": "LVA Fairfax chancery 1836-004: William G. Caton deposes at Centreville, 1 Sep 1835 (C168).",
 "1830_PrinceWilliamCo_VA_census_C-block_noCaton_contact_sheet.png": "1830 Prince William C block (alphabetical) - no Caton (C167).",
 "1830_FairfaxCo_VA_census_p238_MosesCaton_household.jpg": "1830 Fairfax p.238: Moses Caton M 15-20 1, 20-30 2, 60-70 1; F 15-20 1, 30-40 1 - no boy under 15 (C166).",
 "1830_FairfaxCo_VA_census_p250_WilliamG_JohnR_Caton.jpg": "1830 Fairfax p.250: William G. and John R. Caton households (C166).",
 "1820_FairfaxCo_VA_census_p507_MosesCaton_household.jpg": "1820 Fairfax p.507: Moses Caton, M<10 1, 10-16 1, 16-26 2, 45+ 1; F 1/1/1/1 - a second 1820 household with a boy of Aaron's age (C165).",
 "Fairfax_1851-009_LVA_Buckley_v_Buckley_Caton_selected.zip": "LVA Fairfax chancery 1851-009: cover, bill, summons, non-residence return, decree - George W. & Mildred (Buckley) Caton, non-residents 1851 = the Muskingum Catons (C164).",
 "1810_PrinceWilliamCo_VA_census_AaronCaton_household.pdf": "1810 Prince William: Aaron Caton, M 26-45, F 26-45, no children; under John White (C157).",
 "1810_FauquierCo_VA_census_ThomasCaton_household.pdf": "1810 Fauquier: Thomas Caton - M 45+, F 16-26, F 45+ (tallies on the line below the name; C159).",
 "1800_PrinceWilliamCo_VA_SnowdenHorton_estate_account_ThomasCaton_creditor.pdf": "Snowden Horton estate account, Jan 1800: Thomas Caton a creditor; Craven Horton the 1795 co-witness (C154).",
 "1799_PrinceWilliamCo_VA_personal_property_tax_AaronCaton_ThomasCaton_p2.pdf": "1799 list p.2: Aaron Caton (2 horses) and a bare-tithable Thomas Caton (C154).",
 "1813_PrinceWilliamCo_VA_personal_property_tax_AaronCaton.pdf": "1813 list: Aaron Caton, one tithe, no property (C154).",
 "1820_PrinceWilliamCo_VA_census_C-block_p1_noCaton.jpg": "1820 Prince William C block p.1 - no Caton (C155).",
 "1820_PrinceWilliamCo_VA_census_C-block_p2_noCaton.jpg": "1820 Prince William C block p.2 - no Caton (C155).",
 "1799_PrinceWilliamCo_VA_personal_property_tax_MosesCaton.pdf": "Prince William tax list 1799: Moses Caton; Aaron not on this page (C154).",
 "1797_PrinceWilliamCo_VA_personal_property_tax_MosesCaton_AaronCaton.pdf": "Prince William tax list 1797: Moses and Aaron Caton consecutive (C154).",
 "1798_PrinceWilliamCo_VA_personal_property_tax_AaronCaton_MosesCaton.pdf": "Prince William tax list, 1798: Aaron Caton (slave, 2 horses) and Moses Caton (1 horse) consecutive - father and son? (C154).",
 "1813-08_PrinceWilliamCo_VA_OrderBook_jury_AaronCaton_p670.pdf": "Aaron Caton juror, 4 Aug 1813 (C153).",
 "1813-08_PrinceWilliamCo_VA_OrderBook_jury_AaronCaton_p671.pdf": "Aaron Caton juror, 4 Aug 1813, continued (C153).",
 "1812-14_PrinceWilliamCo_VA_OrderBook_jury_AaronCaton_JohnWhite.pdf": "Aaron Caton on a jury with John White, 1812-14 (C153).",
 "1795_PrinceWilliamCo_VA_deed_Madison_to_White_witness_AaronCaton.pdf": "An Aaron Caton witnessing a Prince William Co. deed, proved 4 Dec 1795 - the elder Aaron, a generation before ours (C153).",
 "1871c_CooperCo_MO_CircuitCourt_NancyCaton_v_AaronCaton_divorce_decree.pdf": "Divorce decree: married 12 Oct 1869, deserted 8 Apr 1870 - probably the direct-line Aaron (C151); reverses C053.",
 "1875-11_CooperCo_MO_CircuitCourt_Carroll_v_ONeal_dower_commissioners_report.pdf": "Nov 1875 commissioners' report, O'Neal partition (C150).",
 "1875_CooperCo_MO_CircuitCourt_Carroll_v_ONeal_AaronF_Caton_children_Neal_heirs.pdf": "1875 Neal heirs suit: Aaron F. Caton and minors Henry, Elizabeth, Virginia - collateral (C150).",
 "1865_CooperCo_MO_CircuitCourt_partition_Ross_v_Caton_caption.pdf": "Caption page of the 1865 partition: Ross v. Caton et al. (C149).",
 "1865_CooperCo_MO_CircuitCourt_partition_CatharineLaurie_heirs_WilliamCaton_children.pdf": "Partition decree, Sept 1865: William & Ann F. Caton dead, heirs Joseph, Aaron [F.], Sarah A. Plumley, Daniel R. Caton (C149). Closes C097; opens the two-Josephs problem for C110.",
 "1862_CooperCo_MO_EMM_enrollment_Caton_JJ_and_DanielR.pdf": "1862 Enrolled Missouri Militia, Cooper Co.: J. J. Caton 25 and Daniel R. Caton 18, farmers - collateral (C148).",
 "1848_DelawareCo_OH_chancery_Lavender_v_Johnson_bill.pdf": "Lavender's bill: Aaron Caton's 13 May 1846 order for 20,000 brick (C146).",
 "1848_DelawareCo_OH_chancery_Lavender_v_Johnson_answer_p1_AaronCaton_brick_order.pdf": "Johnson's answer, p.1: Caton owed $100+ 'which he was unable to pay' (C146).",
 "1848_DelawareCo_OH_chancery_Lavender_v_Johnson_answer_p2.pdf": "Johnson's answer, p.2 (C146).",
 "1846_DelawareCo_OH_chancery_Hillyer_Admr_v_Breyfogle_Caton_subpoena.pdf": "Aaron Caton co-defendant in a mortgage foreclosure, subpoena 11 May 1846 (C146).",
 "1845_DelawareCo_OH_CommonPleas_docket_Graham_v_Caton_replevin.pdf": "Graham v. Caton, replevin, April term 1845, struck from docket (C146).",
 "1846_DelawareCo_OH_chattel_mortgage_AaronCaton_to_Johnson.pdf": "Aaron Caton chattel mortgage, 19 May 1846, town of Delaware - house on Pettibone lot; co-signer James A. Asher (C145).",
 "1844_DelawareCo_OH_deed_AaronSarahCaton_to_JonathanGardner_quitclaim.pdf": "Aaron and Sarah Caton quitclaim to Jonathan Gardner, 25 Jun 1844, Liberty Twp - an heir's release of Gardner land (C144). Aaron back in Ohio by mid-1844.",
 "1838_WetzelCo_WV_WilliamsCem_ThomasCaton_1767-1838_gravestone.jpg": "Find a Grave photo: Thomas Caton, b. Oct 1767, d. 8 Jan 1838, Williams Cemetery, New Martinsville (C139). Story-B candidate.",
 "1820_TylerCo_VA_census_p888_B-C_surnames_noCaton.jpg": "1820 Tyler Co. VA, alphabetical schedule, C block - no Caton (C140).",
 "1820_TylerCo_VA_census_p887_title_A-B.jpg": "1820 Tyler Co. VA, title page + A-B block (C140).",
 "1844_StaffordCo_VA_deed_index_C_Caiten-is-Calvert.jpg": "Stafford Co. deed index, C page. The FS 'Caiten 1844' hit is Calvert (C132). Negative.",
 "1840_CooperCo_MO_p145_WmCaton_ThsCaton_NLaurie.jpg": "1840 Cooper Co. MO p.145 image — Wm Caton and Ths Caton adjacent, N. Laurie six rows up; brackets in C128. No male 20-30 in either Caton household.",
 "1840_CooperCo_MO_p135_GeoWCaton_household.jpg": "1840 Cooper Co. MO p.135 image — Geo W Caton, 12 persons, oldest male 30-40 (C129). No male 70+: the Irish-grandfather prediction fails (C130).",
 "1840_DelawareCo_OH_JesseCaton_household.jpg": "1840 Delaware Co. OH image — Jesse Caton, household of one male 30-40 (C100/C131).",
 "1850_DelawareCo_OH_household_extract.md": "Aaron's 1850 household, USGenWeb-based extract. Its 'Julia b. Massachusetts' conclusion is SUPERSEDED (C038) — see the correction header.",
 "1850_DelawareCo_OH_p179_transcription.txt": "USGenWeb proofread transcription, Delaware Twp file 3 of 5 (hh 1153–1266). ISO-8859: use `command grep -a`.",
 "1850_OhioCo_VA_p160b_transcription.txt": "USGenWeb transcription, Ohio Co. (W)VA file 19 of 25 (hh 2166–2299). Harrison Caton in the Boring household.",
 "Aaron_Caton_1850_Delaware_OH_n172_w1800.jpg": "1850 census page image, Delaware Co. OH p.179a. The blotted Julia birthplace cell.",
 "1850_CooperCo_MO_p23_Caton-Laurie-Payne_households.png": "1850 Cooper Co. transcription p.23 — the Fauquier cluster in four consecutive households (C098).",
 "1850_DelawareCo_OH_FamilySearch_Caton_results.csv": "FS index export: all Catons, Delaware Co. OH 1850 — only Aaron's household; Phineas d.1845.",
 "1850_Jesse_Caton_FamilySearch_unrestricted.csv": "FS index export: every Jesse Caton 1850 → Jesse Katon b.1807 MD, Fairfield Co. OH (C105).",
 "1850_James_Cayton_FamilySearch_unrestricted.csv": "FS index export: every James Cayton 1850 → b.1804 PA, Clayton Co. IA with Tabitha (C106).",
 "1901_CowleyCo_KS_WBCaton_biography.txt": "OCR of the 1901 Winfield Courier sketches of W. B. Caton and Mrs. Caton. Does NOT mention Wheeling.",
 "1916_StLouis_JuliaACaton_Sawtell_deathcert_36313.pdf": "Julia's death certificate — father Aaron Caton b. Va, mother Sarah Gardner b. Ohio, birthplace 'Mo'. The record that settled Julia's birthplace.",
 "1955_GentryCo_CharleyCaton_deathcert_15118.pdf": "Charley Caton d.1955 — father Harrison Caton, mother Mary E. Carpenter, b. Gentry Co. 1883 (C048). Identity with the Wheeling Harrison unconfirmed.",
 "Boone_MO_1860_Header_Samples.jpg": "1860 Boone Co. reel navigation aid (parallel pass).",
 "Boone_MO_1860_Header_Transition_120_260.jpg": "1860 Boone Co. reel navigation aid (parallel pass).",
 "Boone_MO_1860_Roche_Twp_Caton_n546_w1800.jpg": "Thos. H. Caton, b. Kentucky, Roche Twp — do not merge (C020).",
 "Boone_MO_1860_Roche_Twp_Patton_n539_w1800.jpg": "Reads Patton, not Caton — resolved negative (C021).",
 "Chariton1896_p232.jpg": "Historical, Pictorial and Biographical Record of Chariton Co. (1896) p.232: 'Joseph Caton … the pioneer tailor' of Brunswick (C065).",
 "Denver1898_p659.jpg": "Imported 10 Sep; purpose not recorded in claims. Unread.",
 "Cooper_1819-1845_County_Court_Index_A-F.pdf": "Missouri State Archives, Cooper Co. Court index (49 MB). No Caton entry — bounded negative (C095). ChatGPT pass.",
 "Cooper_1845-1866_County_Court_Index_A-C.pdf": "Missouri State Archives, Cooper Co. Court index (37 MB). No Caton entry — bounded negative (C095). ChatGPT pass.",
 "Cooper_John_Caton_1840-1860.md": "ChatGPT analysis: John Caton of Cooper Co. was born in Delaware — not Fauquier (C095).",
 "Missouri_Abstract_US_Land_Sales_Vol3_p066_John_Caton.pdf": "FALSE POSITIVE — an 1894 Morgan Co. school-lands patent; does not name Caton (C095).",
 "Fauquier_1820-011_LVA_case.md": "ChatGPT reading of LVA chancery 1820-011: the Caton is MOSES, known locally since c.1805 (C093).",
 "Fauquier_1820-011_LVA_case.zip": "48 scans of the case, from LVA.",
 "Fauquier_1861-012_LVA_case.md": "ChatGPT reading of LVA chancery 1861-012: John N. Caton m. Sarah Elizabeth Lawrie (C094).",
 "Fauquier_1861-012_LVA_case.zip": "40 scans of the case, from LVA.",
 "MDPatents_Liber18_f329_full.jpg": "Theophilus Kitton's 1675 transportation record (C001).",
 "MDPatents_Liber18_f329_headright_detail.jpg": "Detail of the same.",
 "MO_ServiceCard_AaronCaton.pdf": "NARA index card, same as the jpg.",
 "MO_ServiceCard_AaronCaton_2ndMOCav_CoE.jpg": "Aaron's compiled-service index card: enlisted 15 Aug 1861, age 44, reenlisted 5 Jan 1864 (C023).",
 "MO_ServiceCard_WilliamBCaton.pdf": "NARA index card, same as the jpg.",
 "MO_ServiceCard_WilliamBCaton_2ndMOCav_CoE.jpg": "William's card: enlisted Sturgeon, Boone Co., 1 Oct 1862; Remarks BLANK — the consent claim (C008) is not on it (C024, C026).",
 "OhioCounty1830_p209_continuation.jpg": "1830 Ohio Co. VA p.209, second image.",
 "OhioCounty1830_p209_names.jpg": "1830 Ohio Co. VA p.209 — Thomas Caton: male 5–10, male 30–40; exclusion of Aaron WITHDRAWN (C073).",
 "PA1790_WashingtonCo_p192_Kitten_counts.jpg": "1790 Washington Co. PA — Kitten households (C004).",
 "PA1790_WashingtonCo_p192_Kitten_names.jpg": "Same.",
 "PA1790_WashingtonCo_p192_Kitten_page.jpg": "Same, full page.",
 "T01_massachusetts-vitals-search.md": "Return for the VOID task T01. Its negatives are MOOT (C045) — Julia was born in Missouri. Do not act on it.",
 "T03_sarah-ann-gardner-caton-death.md": "Task return, T03.",
 "T06_boring-ohio-county-marriage-index.md": "ChatGPT return: no John Boring marriage in the WV index 1834–50 (C089).",
}
def cites(fn):
    ids=[]
    for r in rows:
        if fn in (r.get("evidence") or "") or fn in r.get("fact",""):
            ids.append(r["id"])
    return ids
files=sorted(p for p in ev.iterdir() if p.is_file() and p.name!="README.md")
out=[f"# evidence/ — manifest, generated {datetime.date.today().isoformat()} ({len(files)} files)\n",
     "Regenerate with `python3 tools/make-evidence-manifest.py`. Notes are maintained in that script.\n",
     "Rules: agents write findings here as new files and edit nothing else. Files are provenance — **never edit an original**; add a correction header if a conclusion in a derived file is superseded.\n",
     "| file | size | cited by | note |","|---|---:|---|---|"]
def hs(n):
    for u in ("B","KB","MB"):
        if n<1024: return f"{n:.0f} {u}"
        n/=1024
    return f"{n:.1f} GB"
for p in files:
    c=cites(p.name)
    out.append(f"| `{p.name}` | {hs(p.stat().st_size)} | {', '.join(c) or '—'} | {NOTES.get(p.name,'')} |")
uncited=[p.name for p in files if not cites(p.name)]
out.append(f"\n**Files no claim cites ({len(uncited)}):** " + ", ".join(f"`{u}`" for u in uncited))
(ev/"README.md").write_text("\n".join(out)+"\n")
print(f"evidence/README.md: {len(files)} files, {len(uncited)} uncited")
