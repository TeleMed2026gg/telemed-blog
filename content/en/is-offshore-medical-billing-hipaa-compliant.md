---
title: "Is Offshore Medical Billing HIPAA Compliant? What a BAA Covers"
description: "Is offshore medical billing HIPAA compliant? Yes, with a BAA and a real risk analysis. What the BAA covers, what it doesn't, and the state laws to check."
slug: is-offshore-medical-billing-hipaa-compliant
lang: en
date: 2026-10-20
keyword: is offshore medical billing HIPAA compliant
category: Compliance
author: rod
status: published
faq:
  - q: "Does HIPAA prohibit sending PHI outside the United States?"
    a: "No. HIPAA has no rule that bans offshore access or storage. HHS says covered entities can use vendors outside the U.S. if they sign a business associate agreement and account for the added risks in their Security Rule risk analysis."
  - q: "Is a signed BAA enough to make an offshore billing vendor compliant?"
    a: "No. The BAA sets the legal obligations. Compliance depends on how the vendor actually controls access, devices, networks and subcontractors, and on whether your own risk analysis covers the arrangement."
  - q: "Do state laws restrict offshore handling of patient records?"
    a: "Some do. Florida requires certain providers to keep electronic patient records physically in the continental U.S., U.S. territories or Canada. Texas SB 1188 requires covered entities to physically maintain EHRs in the U.S. starting January 1, 2026."
  - q: "Can an offshore vendor be sued or penalized under HIPAA?"
    a: "Business associates are directly liable to HHS for certain HIPAA violations, such as Security Rule failures and impermissible disclosures. Enforcing that against a foreign company is harder, which is why the vendor's legal structure matters."
---

Yes, offshore medical billing can be HIPAA compliant. HIPAA does not ban sending protected health information (PHI) outside the United States. It requires a business associate agreement (BAA), safeguards that match the risk, and a risk analysis that accounts for where the work happens. A BAA alone doesn't make a vendor compliant, though, and a few states now add rules of their own.

## What HIPAA actually says about offshore vendors

The HIPAA Rules contain no specific offshore prohibition. The clearest statement comes from HHS itself. In its guidance on cloud vendors that store data abroad, the [HHS Office for Civil Rights says](https://www.hhs.gov/hipaa/for-professionals/faq/2083/do-the-hipaa-rules-allow-a-covered-entity-or-business-associate-to-use-a-csp-that-stores-ephi-on-servers-outside-of-the-united-states/index.html) this is allowed as long as a BAA is in place and the parties otherwise comply with HIPAA.

The same guidance adds a condition that practices often skip. Where the data sits or who touches it affects the risk, so it has to show up in your Security Rule risk analysis. If a country has documented hacking or malware problems, HHS expects you to address those threats with appropriate safeguards.

The concern isn't new. A 2014 HHS Office of Inspector General review, [summarized by Becker's Hospital Review](https://www.beckershospitalreview.com/healthcare-information-technology/oig-outsourcing-administrative-functions-offshore-places-phi-at-risk/), warned that other countries may have weaker privacy laws and less ability to enforce a BAA. That warning is still the right starting point for any evaluation.

## What a BAA covers

A BAA is a contract with required content. According to [HHS's guidance on business associate contracts](https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html), it must:

- Define the permitted and required uses and disclosures of PHI.
- Prohibit any other use or disclosure.
- Require appropriate safeguards, including Security Rule compliance for electronic PHI.
- Require the vendor to report unauthorized uses, disclosures and breaches.
- Require support for patient access, amendment and accounting requests.
- Make the vendor's practices and records available to HHS.
- Require return or destruction of PHI at the end of the contract, where feasible.
- Flow the same restrictions down to subcontractors.
- Allow you to terminate if the vendor violates a material term.

Business associates are also [directly liable under HIPAA](https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/factsheet/index.html) for failures such as not complying with the Security Rule, impermissible disclosures, and not signing BAAs with their own subcontractors.

## What a BAA doesn't cover

This is where offshore arrangements fail in practice. The contract sets obligations. It doesn't create controls. A BAA won't tell you:

| Question | Why the BAA doesn't answer it |
|---|---|
| Can agents download, print or screenshot PHI? | Device and desktop controls are operational, not contractual |
| Who else in the building can see the screens? | Physical security depends on the facility |
| Are there unnamed subcontractors? | The BAA requires flow-down, but you still need the list |
| Which legal entity can you actually sue? | A BAA signed by a foreign company with no U.S. presence is hard to enforce |
| Where is PHI stored, even temporarily? | State storage laws care about location, and HIPAA risk analysis does too |
| How fast will you hear about an incident? | "Without unreasonable delay" is the legal floor; your contract can set a shorter window |

The legal-entity question matters more than most practices expect. If the vendor contracts through a U.S. company, under U.S. law, your remedies are far more practical. Telemed, for example, contracts with U.S. clients through its Florida LLC, and we sign a Business Associate Agreement (BAA) with healthcare clients.

## State laws to check before you sign

Federal law is the floor. Two states with large patient populations have added rules about where records live.

**Florida.** Amendments to Fla. Stat. § 408.051, effective July 1, 2023, require many licensed providers that use certified EHR technology to keep patient information "physically maintained in the continental United States, U.S. territories or Canada," including data held by cloud or subcontracted vendors, according to [Polsinelli's summary](https://www.polsinelli.com/publications/florida-imposes-a-ban-on-offshoring-storage-of-medical-information). AHCA-licensed providers attest to compliance on their license applications.

**Texas.** SB 1188 requires covered entities to physically maintain EHRs only within the United States, with the storage requirement in effect since January 1, 2026. [Goodwin's analysis](https://www.goodwinlaw.com/en/insights/publications/2025/08/alerts-otherindustries-hltc-new-texas-law-regulates-use) notes that the law is unclear on whether remote access from outside the U.S. is restricted, and that civil penalties range from $5,000 to $250,000 per violation.

Both laws focus on **storage**. An offshore team that works inside your U.S.-hosted EHR and practice management system, without copying data locally, is a different setup from a vendor that exports files to servers abroad. Ask your healthcare attorney how your state's rule applies to your specific workflow. We're not lawyers, and this isn't legal advice.

## A due-diligence checklist for offshore and nearshore billing vendors

Use these questions in your vendor review. Ask for evidence, not just answers.

1. **Contracting entity.** Which legal entity signs the contract and the BAA, and in which jurisdiction?
2. **Data location.** Does PHI stay in your U.S.-hosted systems, or is anything stored, exported or cached elsewhere?
3. **Access model.** Do agents work through a virtual desktop with copy, print, download and USB disabled?
4. **Minimum necessary.** Can workflows be designed so agents see less PHI? Tokenization and bots that complete lookups without exposing full records to a person are options worth asking about.
5. **Workforce.** Background checks, HIPAA training at hire and annually, signed confidentiality agreements, and prompt access removal at termination.
6. **Dedicated staff.** Are agents assigned only to your account, or shared across clients?
7. **Facility.** Clean-desk policy, no personal phones on the floor, controlled entry.
8. **Subcontractors.** A complete list, and a copy of the downstream BAA.
9. **Incident response.** A named contact and a notification window written into the contract.
10. **Audit rights.** Your right to review policies, access logs and training records.

## When offshore or nearshore billing isn't the right fit

Sometimes the answer is no. If your state's law or a major payer contract restricts non-U.S. access, keep that work domestic. The same goes if your compliance team can't support a risk analysis for a foreign location, or if your systems can only be reached by exporting data. If the vendor can't explain its controls in writing, walk away.

For many practices, a split model works: nearshore agents handle work inside your U.S.-hosted systems, and anything that involves local storage stays with the U.S. team. Our comparison of [nearshore vs. offshore medical billing](/blog/nearshore-vs-offshore-medical-billing/) covers how time zones, oversight and legal structure differ between the two.

## Key takeaways

- HIPAA doesn't prohibit offshore billing. It requires a BAA, appropriate safeguards and a risk analysis that reflects the vendor's location.
- A BAA is necessary but not sufficient. Verify the operational controls behind it.
- Check the contracting entity. A U.S. entity under U.S. law gives you practical remedies.
- Florida and Texas regulate where electronic patient records are stored. Map your data flow before you sign.
- Ask for evidence: access logs, training records, subcontractor lists and incident procedures.

If you're evaluating a partner for billing, coding or prior authorizations, you can review [Telemed's services](https://telemed.com.co/us/#services) and how we approach [security](https://telemed.com.co/us/#security).
