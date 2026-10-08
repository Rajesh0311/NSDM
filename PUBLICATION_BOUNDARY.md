# Public research / private implementation boundary

Recorded 8 October 2026.

## Public scope
Website source, released manuscripts with their real status, approved benchmark fixtures/results, reproducible experiment code, scientific primers, diagrams and curated learning plans may remain public. Research drafts already released publicly retain their disclosed draft status; this is not peer-review approval.

## Private scope
Commercial implementation, customer/participant data, credentials, client engagements, proposals, pricing/negotiations, unpublished proprietary methods, daily operations and unapproved editorial drafts belong in a private repository. Use the existing private MetaForge development repository; do not stage these inside this checkout.

## Operational records
Six operational/editorial records across NSDM and ACE were preserved byte-for-byte as a reconstructable JSON archive in the private development repository before their current public copies were replaced by pointers. SHA-256 values accompany the original UTF-8 contents. Private archive: `00-command-center/private-source-archives/2026-10-08-public-boundary.json`.

The public pointer is not the private record. Edit the private working record, not the pointer. Papers, registered experiment data and their reproducibility links remain intact.

## Release workflow
1. Work on proprietary or sensitive material in a private checkout.
2. Prepare a separate public release candidate with valid data rights and appropriate anonymization.
3. Review every new file and every changed byte. Do not assume a previously public path makes new contents safe.
4. Add reviewed paths to `.public-release.json`; run `python scripts/check_public_release.py`.
5. Check the website and evidence links, then publish the approved candidate.

The inventory records the current public surface, including legacy files. It is not a claim that all legacy content has had a complete confidentiality review. CI rejects unlisted tracked paths, edits to private-record pointers and selected credential signatures. Ignore rules only protect untracked files; they are not access control. CI runs after push and does not itself prevent an initial public exposure. Review locally before pushing.

## Historical exposure
Current-tree removal is not erasure. Prior public commits, clones, caches and detached public forks may retain these records. No history rewrite or claim of recalled copies is made. Rotate any exposed credentials; assess personal/client data separately. A full history/secret scan and authenticated collaborator/app-permission audit are separate work.

## Public links
Website links grant no private-repository access. Keep evidence links pointing to public released artifacts; verify access anonymously. Never publish authentication tokens in links.

## Limits
This change establishes a publication boundary and a limited automated check. It is not a full security certification, a repository-wide history purge, or proof of domain/platform security.
