# Creditor-reference claim audit

This offline tool compares documentation claims with Python call evidence. It parses source without executing it. Review findings in context.

## Usage

```sh
python3 -m iso11649_validation_claim_audit audit .
iso11649-validation-claim-audit audit . --fail-on medium --json
iso11649-validation-claim-audit --version
```

Use `--ignore PREFIX` repeatedly to exclude paths. The default threshold is high; medium includes test-only evidence. Exit codes are 0 for pass, 2 for findings at the threshold, and 1 for usage or input errors.

```text
documented-iso11649-validation-claim-false
documented-no-iso11649-validation-claim-false
```

## Limitations

A compact call only strips separators and surrounding whitespace and changes case.

A format call only regroups characters into blocks of four.

A mod-97 check call on the rearranged string is not recognised.

An IBAN call judges a bank account number and is not recognised.

The validators package does not provide the relevant route.

The idutils package does not provide the relevant route.

Strings, comments, imports and bare references do not establish a call.

Syntax errors prevent source evidence.

Calls split across modules do not combine into evidence.

A subprocess invocation does not count.

Roadmap, changelog and TODO prose can produce claims without implemented code.

A single-character substitution can still pass: RF0953900754K034123456789 is valid.

The library does not establish registration with any creditor.

Separators are stripped before judging.

A tab character is not stripped: embedded tabs are rejected.

An underscore is not stripped: RF18_539007547034 is rejected.

An empty string raises instead of validating.

A regular expression checks a pattern rather than the full library judgement.

A length check alone omits the check-digit leg.

A prefix check alone omits the check-digit leg.

A short number fails: RF18 is rejected.

A long number fails: a 26-character string is rejected.

Letters are accepted in the body: RF185390075470Y validates.

The maximum length is 25 characters: RF09539007547034123456789 validates.

The minimum length is 5 characters: RF180 fails the check.

The check is the ISO 13616 mod 97-10 check of the rearranged string.

```text
validate rf creditor reference
```

The bare phrase above can describe a manual runbook step.

```text
rf creditor reference validation
```

The bare phrase above can describe a roadmap feature.

```text
rf creditor reference validator
```

The bare phrase above can describe a hosted web page.

```text
rf creditor reference check
```

The bare phrase above can describe a field-presence lint rule.

```text
check rf creditor reference
```

The bare phrase above can describe a manual runbook step.

```text
verify rf creditor reference
```

The bare phrase above can describe a visual account confirmation.

```text
rf creditor reference validation check
```

The bare phrase above can describe a field-presence check.

```text
valid rf creditor reference
```

The bare phrase above can appear as example output.

```text
rf creditor reference is valid
```

The bare phrase above can appear as example output.

```text
rf creditor reference is invalid
```

The bare phrase above can appear as example error text.

```text
rf creditor reference validity
```

The bare phrase above can name a configuration flag or column.

```text
rf creditor reference format validation
```

The bare phrase above can describe a format without code.

```text
validate rf creditor reference format
```

The bare phrase above can describe a shape-only check.

```text
iso 11649 validation
```

The bare phrase above can name a specification section.

```text
validate iso 11649
```

The bare phrase above can describe a manual runbook step.

```text
check iso 11649
```

The bare phrase above can describe a manual runbook step.

```text
verify iso 11649
```

The bare phrase above can describe a manual runbook step.

```text
iso 11649 check
```

The bare phrase above can name a specification section.

```text
rf reference check
```

The bare phrase above can name an invoicing checklist item.

```text
rf reference validation
```

The bare phrase above can describe a result from an external platform.

```text
rf creditor reference
```

The bare phrase above alone names a creditor reference without judging it.

```text
rf reference
```

The bare phrase above alone names a reference without judging it.

```text
creditor reference
```

The bare phrase above alone does not claim a judgement.

```text
iso 11649
```

The bare phrase above alone does not claim a judgement.

```text
check digit
```

The bare phrase above alone does not claim a judgement.

```text
mod 97
```

The bare phrase above alone does not claim a judgement.

```text
creditor
```

The bare phrase above alone does not claim a judgement.

```text
sepa
```

The bare phrase above alone does not claim a judgement.

## Differentiation

Neighbouring families include generic validation, ISBN-validation, ISSN-validation, IBAN-validation, UUID-validation, semver-validation, MAC-address-validation, BIC-validation, cron-expression-validation, cron-expression-description, scheduled-execution, date-validation, timeout, payment-processing, credit-card-extraction, auth, password-hashing, password-generation, PDF-encryption, email-sending, SMS-sending, document-extraction, barcode-scanning, email-validation, phone-validation, password-strength, JSON-Schema-validation, credit-card-validation, domain-validation, URL-validation, IP-validation, JSON-parsing, regex, URL-parsing, URL-fetching, DNS, barcode-generation, account-extraction, VIN-extraction, VIN-decoding, VIN-history-lookup, hex-color-validation, ORCID-validation, ISNI-validation, DOI-validation, CASRN-validation, SEDOL-validation, ISIN-validation, ISIN-record-query, ISIN-extraction, CUSIP-validation, IMEI-validation, MEID-validation, ESN-validation, ISMN-validation, ISAN-validation, GRid-validation, EAN-validation, generic-serial-number, FIGI-validation, FIGI-record-query, FIGI-extraction, ISRC-validation, Ethereum-address-validation, Binance-Smart-Chain-address-validation, Tron-address-validation, Litecoin-address-validation, Dogecoin-address-validation, bitcoin-address-validation, transaction-hash-validation, private-key-validation, block-explorer, address-generation, address-extraction, payment-receipt, spreadsheet-reading, spreadsheet-generation, Word-reading, Word-generation, presentation-reading, presentation-generation, PDF-extraction, PDF-generation, PDF-merging, PDF-splitting, PDF-rotation, PDF-form-filling, PDF-watermarking, PDF-redaction, PDF-compression, PDF-annotation, table-extraction, OCR, document-data-extraction, e-signature, screen-recording, video-generation, QR-generation, audio-mixing, audio-generation, audio-editing, audio-source-separation, speech-recognition, speech-synthesis, noise-reduction, music-generation, music-transcription, InChI, SMILES, EC-number, UN-transport-number, PubChem-query, chemical-structure-validation, other-chemical-identifiers, container-number-reading, carrier-registry, BIC-shipowner-code, container-size-type, container-number-generation, ISO-6346-validation, library-record-fetching, library-identifier-registration, cataloguing, OCLC-WorldCat, library-agency-listing, ISIL-validation, IMO-validation, MMSI-validation, HIN-validation, ENI-validation, vessel-registry-lookup, AIS-tracking, ship-name-lookup, IMSI-validation, VIES-lookup, VAT-rate-lookup, tax-calculation, invoice-generation, VATIN-validation, SEPA-creditor-reference, invoice-reference-extraction, payment-lookup, creditor-reference-generation.

## Matched phrases

```text
validate rf creditor reference
validates rf creditor reference
validating rf creditor reference
rf creditor reference validation
rf creditor reference validations
rf creditor reference validator
rf creditor reference validation check
rf creditor reference check
check rf creditor reference
verify rf creditor reference
rf creditor reference verification
rf creditor reference is valid
rf creditor reference is invalid
valid rf creditor reference
invalid rf creditor reference
rf creditor reference validity
rf creditor reference format validation
validate rf creditor reference format
rf creditor reference length validation
rf creditor reference character validation
is valid rf creditor reference
is rf creditor reference valid
rf creditor reference validation library
rf creditor reference validation function
rf creditor reference validation tool
checks rf creditor reference
checking rf creditor reference
verifies rf creditor reference
verifying rf creditor reference
validate iso 11649
validates iso 11649
validating iso 11649
iso 11649 validation
iso 11649 validations
iso 11649 validator
iso 11649 validation check
iso 11649 check
check iso 11649
verify iso 11649
iso 11649 verification
iso 11649 is valid
iso 11649 is invalid
valid iso 11649
invalid iso 11649
validate rf reference
validates rf reference
validating rf reference
rf reference validation
rf reference validator
rf reference check
no rf creditor reference validation
does not validate rf creditor reference
no rf creditor reference validator
no rf creditor reference validation check
does not support rf creditor reference validation
without rf creditor reference validation
rf creditor reference validation not supported
rf creditor reference validation not available
cannot validate rf creditor reference
cannot check rf creditor reference
does not check rf creditor reference
no rf creditor reference check
does not verify rf creditor reference
no rf creditor reference verification
rf creditor reference validation not implemented
does not validate rf creditor reference format
no iso 11649 validation
does not validate iso 11649
no iso 11649 validator
iso 11649 validation not supported
cannot validate iso 11649
does not verify iso 11649
no iso 11649 verification
iso 11649 validation not implemented
```
