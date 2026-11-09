---
title: "Texas SB 1188 and Offshore Access to Patient Records"
description: "Texas SB 1188 offshore rules explained: U.S. storage of EHRs, what the law says about remote access, penalties, and a vendor checklist for practice owners."
slug: texas-sb-1188-offshore
lang: en
date: 2026-11-09
keyword: Texas SB 1188 offshore
category: Compliance
author: rod
status: published
faq:
  - q: "Does Texas SB 1188 ban offshore staff from accessing patient records?"
    a: "The law doesn't say so. It requires EHRs to be physically maintained in the U.S. or a U.S. territory and limits access to people who need the information for treatment, payment or health care operations. Law firms differ: some say offshore access is allowed with safeguards, others call view-only access an open question. Confirm your setup with Texas counsel."
  - q: "When did the Texas SB 1188 storage rule take effect?"
    a: "The act took effect September 1, 2025. The storage requirement in Section 183.002 applies to EHRs stored on or after January 1, 2026, regardless of when the record was created."
  - q: "What are the penalties under Texas SB 1188?"
    a: "The attorney general can seek civil penalties of up to $5,000 per violation for negligence, up to $25,000 for knowing or intentional violations, and up to $250,000 when protected health information is knowingly or intentionally used for financial gain. Each cap is applied per year."
  - q: "Does SB 1188 apply to practices outside Texas?"
    a: "It may. The covered entity definition comes from Texas Health and Safety Code Section 181.001, and Goodwin notes it may reach out-of-state entities that process Texas residents' protected health information. Ask counsel if you treat Texas patients from another state."
---

Texas SB 1188 requires covered entities to keep electronic health records physically in the United States or a U.S. territory, and that rule has applied since January 1, 2026. It does not explicitly ban offshore staff from viewing records, but it limits access to people who need the information for treatment, payment or health care operations. So the question for a practice isn't only "Is my vendor offshore?" It's "Where do the records sit, and who can reach them?"

This article is a practical summary, not legal advice. Take your specific setup to Texas health care counsel.

## What Texas SB 1188 requires

SB 1188 added Chapter 183 to the Texas Health and Safety Code. The [enrolled bill text](https://capitol.texas.gov/tlodocs/89R/billtext/html/SB01188F.htm) sets out three duties that matter most for outsourcing:

| Provision | What it requires | Why it matters when you outsource |
|---|---|---|
| Sec. 183.002(a) | EHRs with patient information must be physically maintained in the U.S. or a U.S. territory | Applies to third-party, subcontracted and cloud storage |
| Sec. 183.002(b) | Texas residents' non-open-data EHR information is accessible only to people who need it for treatment, payment or health care operations | Every vendor login needs a job-based reason |
| Sec. 183.002(c) | Reasonable administrative, physical and technical safeguards | Covers confidentiality, integrity and availability |

The act took effect September 1, 2025. The storage rule has a later date: it applies to EHRs stored on or after January 1, 2026, whenever the record was created. That means older charts are covered too.

The law also has rules on AI disclosure and on parent and guardian access to minors' records. The [Texas Medical Association's summary](https://www.texmed.org/Template.aspx?id=66759) is a good starting point for those.

## Who SB 1188 covers

"Covered entity" takes its meaning from Section 181.001, and Chapter 183 adds that it includes a health care practitioner. In plain terms, that's a business that assembles, collects, analyzes, uses, evaluates, stores or transmits protected health information.

That's broader than the HIPAA definition. It can pull in vendors, and [Goodwin notes](https://www.goodwinlaw.com/en/insights/publications/2025/08/alerts-otherindustries-hltc-new-texas-law-regulates-use) it may reach out-of-state entities that process Texas residents' PHI.

The enrolled text excludes certain facilities and programs, including nursing facilities, assisted living facilities, intermediate care facilities and continuing care facilities. A physician practice, specialty group or billing company should assume it needs to review the law.

## Storage vs. offshore access: what's settled and what isn't

The storage side is clear. The access side isn't, and law firms don't read it the same way.

- **The statute:** Section 183.002(a) speaks to where records are physically maintained. Section 183.002(b) limits who can access them by job duty. Neither uses the word "offshore," and neither sets a geographic limit on access.
- **More permissive reading:** [McDonald Hopkins](https://www.mcdonaldhopkins.com/insights/news/s-b-1188-texas-ehr-law-data-localization-ai-and-access-requirements) says offshore access is still allowed with safeguards, as long as it doesn't result in EHR data being stored, copied or cached on non-U.S. servers or devices.
- **More cautious reading:** Goodwin and [Hall Render](https://hallrender.com/2025/08/19/new-texas-law-on-ehr-data-localization-and-ai/) say it's unclear whether offshore read-only access violates the storage rule. Goodwin advises being able to limit processing to the U.S. if needed.

Both readings point to the same operating rule: **no copy of the record should land outside the U.S.** That includes the parts people forget, such as backups, disaster recovery, local caches, exported reports, screenshots and downloaded PDFs. [Buchalter](https://www.buchalter.com/insights/from-phi-to-ai-what-texas-sb-1188-means-for-healthcare-entities-and-vendors/) flags caching, backup, replication and disaster recovery specifically.

Texas isn't alone here. We cover a similar question in our guide to [Florida's offshore PHI law](/blog/florida-offshore-phi-law-408-051/).

## Penalties under SB 1188

Enforcement sits with the Texas attorney general, who can seek injunctive relief and civil penalties. The enrolled text caps penalties at the following amounts per violation, applied per year:

| Violation | Civil penalty cap |
|---|---|
| Negligent | $5,000 |
| Knowing or intentional | $25,000 |
| Knowing or intentional use of PHI for financial gain | $250,000 |

Civil penalties aren't the only exposure. According to the Texas Medical Association, agencies including the Texas Medical Board may discipline a covered entity that violates the law three or more times in the same manner, up to suspending or revoking a license.

## A vendor checklist for Texas practices

Ask these questions of every vendor that touches your EHR or billing system, whether it's in Dallas, Medellín or anywhere else:

1. **Where is the EHR physically hosted?** Get the data center locations in writing, including backup and disaster recovery sites.
2. **Does your cloud provider or any subcontractor hold a copy?** Storage by a third party still counts.
3. **How do agents reach the system?** Working inside your U.S.-hosted EHR through a controlled session is very different from pulling files into the vendor's own platform.
4. **Can anything be saved locally?** Ask about download, print, clipboard and screenshot controls.
5. **What's stored in the vendor's own tools?** Ticketing systems, call recordings, QA notes and email can all hold patient information.
6. **Is access role-based and logged?** You should be able to show why each user can see what they see.
7. **What happens if the law is read more strictly?** Ask whether the work can be restricted to U.S.-based staff.
8. **Do the contract terms back all this up?** Your Business Associate Agreement covers HIPAA, but it won't resolve state storage rules by itself. For more on that gap, see [what a BAA does and doesn't cover](/blog/is-offshore-medical-billing-hipaa-compliant/).

Also map any AI tools in the workflow. A voice agent or transcription service that processes chart data has its own storage path.

## How to reduce PHI exposure in an offshore or nearshore model

If you use a team outside the U.S., design the workflow so the agent needs as little data as possible.

- Keep work inside the practice's own systems rather than in shared drives or spreadsheets.
- Use the minimum necessary role for each task. A scheduler rarely needs the full chart.
- Disable local downloads and copy-paste where the task doesn't require them.
- Audit a sample of access logs each month.

In our operations, we've found tokenization and bots can also keep agents from seeing PHI on some tasks. Telemed signs a Business Associate Agreement with healthcare clients, and you can review how we approach data protection on our [security page](https://telemed.com.co/us/#security).

## When to keep the work in the U.S.

Offshore or nearshore support isn't right for every Texas practice. Keep a task with U.S.-based staff if:

- Your counsel takes the conservative view on read-only access.
- The task requires saving files locally or working from exports.
- Your EHR vendor can't confirm U.S.-only hosting and backups, because that problem needs fixing first.
- You can't produce a clear record of who accessed what.

A mixed model often works: a U.S. team handles the records-heavy tasks, and a nearshore team handles scheduling or calls with limited access.

## Key takeaways

- Since January 1, 2026, SB 1188 has required EHRs to be physically maintained in the U.S. or a U.S. territory, including older records.
- The law limits access by job need. It doesn't explicitly address access from abroad, and law firms read that differently.
- Treat any offshore copy, cache or backup as the main risk.
- Penalties run up to $250,000 per violation, depending on intent and financial gain.
- Get hosting, access controls and fallback options in writing, then have Texas counsel review them.
