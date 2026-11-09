---
title: "Florida's Offshore PHI Law (§ 408.051) for Practice Owners"
description: "Florida offshore PHI law § 408.051(3) explained: what it requires, who must attest, storage vs. remote access, and a vendor checklist for practice owners."
slug: florida-offshore-phi-law-408-051
lang: en
date: 2026-10-26
keyword: Florida offshore PHI law
category: Compliance
author: rod
status: published
faq:
  - q: "What does Florida's offshore PHI law require?"
    a: "Fla. Stat. § 408.051(3) requires health care providers that use certified EHR technology to ensure that patient information stored offsite, including with cloud and subcontracted vendors, is physically maintained in the continental United States, its territories or Canada."
  - q: "Does the Florida law ban offshore staff from accessing patient records?"
    a: "The statute speaks to where data is physically maintained. Some law firms read it as covering storage, not remote access; others flag the wording as unclear. Confirm your specific setup with Florida health care counsel."
  - q: "When did Florida's offshore storage rule take effect?"
    a: "July 1, 2023, through CS/CS/SB 264, signed in May 2023."
  - q: "Who has to sign the compliance affidavit?"
    a: "Providers licensed under Chapter 408 attest under penalty of perjury, at initial licensure and at each renewal, that they comply with § 408.051(3)."
---

Florida's offshore PHI law, Fla. Stat. § 408.051(3), requires health care providers that use certified EHR technology to keep patient information stored offsite physically in the continental United States, its territories or Canada. It applies to data held by cloud providers and subcontractors, and many licensed providers must attest to compliance under penalty of perjury. The law is about where data lives, so the first job for a practice owner is to map every place patient data is stored.

## What § 408.051(3) actually says

The rule came in with CS/CS/SB 264, signed in May 2023 and effective July 1, 2023, according to [Polsinelli](https://www.polsinelli.com/publications/florida-imposes-a-ban-on-offshoring-storage-of-medical-information). The [current statute](https://m.flsenate.gov/Statutes/408.051) says a health care provider using certified electronic health record technology "must ensure that all patient information stored in an offsite physical or virtual environment" is physically maintained in the continental U.S., its territories or Canada. That includes storage through a third party, a subcontracted computing facility or a cloud provider.

Three details matter:

- **It covers all patient information**, not only diagnoses or behavioral health records.
- **It applies to records kept with any technology** that allows information to be electronically retrieved, accessed or transmitted.
- **It adds to HIPAA.** The statute states that its requirements are in addition to the HIPAA Privacy and Security Rules. A signed BAA does not satisfy it on its own.

## Who it applies to

The list is broad. Polsinelli's summary includes AHCA-licensed providers such as clinics, hospitals, ambulatory surgery centers, home health agencies and nursing homes, plus many licensed practitioners: physicians, nurses, dentists, pharmacists, psychologists, therapists and clinical social workers.

Providers licensed under Chapter 408 also sign an affidavit at initial licensure and at each renewal, attesting under penalty of perjury that they comply with § 408.051(3), as a [March 2026 Workplace Privacy Report article](https://www.workplaceprivacyreport.com/2026/03/articles/health-information-technology/a-reminder-about-floridas-ban-on-offshore-health-data-storage-what-providers-and-vendors-should-know/) explains. That affidavit is the reason this law deserves attention. Signing it without knowing where your vendors keep data is a risk the practice owner carries personally.

## Storage vs. remote access: where firms disagree

This is the question we hear most from Florida practices considering a nearshore team. The statute focuses on where data is "physically maintained." It does not say who may view it.

- [McDermott Will & Schulte](https://www.mcdermottlaw.com/insights/guarding-the-gateway-florida-tightens-grip-on-electronic-health-records-storage/) notes that the statute's final sentence has caused confusion, and that some commentators read it to bar offshore personnel from remote access. The firm's own reading is narrower: the act "does not appear to consider accessing, processing or transmitting patient information as physically maintaining it," and the legislative bill analysis does not suggest offshore access is prohibited.
- Polsinelli and the Workplace Privacy Report piece both stop short of a conclusion on remote access and recommend reviewing the statute with counsel.

Our practical takeaway: a setup in which data stays on U.S.-hosted systems and a remote team works inside them is a different situation from a vendor that copies, downloads or caches records abroad. But "different" is not "cleared." Get a written opinion from Florida health care counsel for your specific workflow before you sign the affidavit.

## Where offshore storage hides

Most practices don't store records abroad on purpose. It happens through vendors. Check each of these:

| Data location | What to ask | Common risk |
|---|---|---|
| EHR and practice management system | Where are the primary and backup data centers? | Backups or disaster recovery in another region |
| Billing or RCM vendor | Do staff download reports, EOBs or claim files to local machines? | Local copies on laptops outside the U.S. |
| Clearinghouse and payment posting tools | Where is remittance data stored and archived? | Archives held by a subcontractor abroad |
| Call center or scheduling vendor | Are call recordings and transcripts stored? Where? | Recordings on a foreign telephony platform |
| AI tools (voice bots, transcription, chat) | Where are prompts, transcripts and logs retained? | Model or log storage in an unspecified region |
| Email, fax and file sharing | Which tenant and region? | Attachments synced to devices abroad |
| Document scanning and indexing | Where are images processed and held? | Temporary storage during processing |

Polsinelli's summary notes that vendors holding records even temporarily are included. Temporary processing deserves the same questions as permanent storage.

## A five-step compliance check for practice owners

1. **Build a data map.** List every system and vendor that stores, processes or backs up patient information. Include call recordings and AI transcripts.
2. **Ask vendors in writing.** Request each vendor's data residency statement and its subcontractors' locations. Verbal answers don't hold up when you sign an affidavit.
3. **Update contracts.** Add a clause requiring storage in the continental U.S., its territories or Canada, notice before any change, and certification of destruction for any copies held elsewhere.
4. **Lock down endpoints.** For any remote team, U.S. or not, block local downloads, USB storage and printing, and use virtual desktops so data stays on your hosted systems.
5. **Review before every renewal.** Re-run the map before each license renewal, since vendors change hosting and add subcontractors.

## How a nearshore team can fit the rule

Here is how we set up work for Florida clients. We contract through our Florida LLC, under U.S. law, and we sign a Business Associate Agreement (BAA) with healthcare clients. Our agents work inside the client's own EHR, practice management and phone systems. We design workflows so patient data stays on those U.S.-hosted systems rather than being copied to our side, and where it fits, we use architectures that limit what PHI an agent sees, such as tokenization or bots that handle identity checks before a person joins the call.

That design addresses where data is stored. It doesn't settle the remote-access debate for you, which is why we encourage every client to confirm the setup with their own counsel.

## When outsourcing isn't the right call

If your counsel takes the conservative view that any offshore viewing is restricted, or if your workflow requires staff to save files locally, keep that work with an in-house or U.S.-based team. The same applies if a vendor can't tell you, in writing, where its subcontractors store data. For background on how HIPAA and BAAs fit with state rules, see our guide on [whether offshore medical billing is HIPAA compliant](/blog/is-offshore-medical-billing-hipaa-compliant/). Texas has its own storage law, SB 1188, which works differently and deserves its own review.

## Key takeaways

- § 408.051(3) requires patient information stored offsite to be physically maintained in the continental U.S., its territories or Canada, effective July 1, 2023.
- It covers cloud and subcontracted vendors, and it adds to HIPAA rather than replacing it.
- Chapter 408 licensees attest to compliance under penalty of perjury at licensure and renewal.
- Law firms disagree on whether remote access from abroad is covered. Get a written opinion for your workflow.
- Map every place data lives, including call recordings, AI transcripts and backups, before you sign.

This article is general information, not legal advice. Telemed provides [scheduling, billing and prior authorization support](https://telemed.com.co/us/#security) for U.S. practices, working inside your systems under a BAA.
