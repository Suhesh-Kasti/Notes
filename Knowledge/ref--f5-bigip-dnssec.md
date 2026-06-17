---
category: knowledge
tags:
  - dns
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Understanding [[DNSSEC]]
---

# Understanding [[DNSSEC]]
### [[DNSSEC]]  Refresher
[[DNSSEC]] stands for Domain Name System Security Extensions. It is a security protocol used to protect the Domain Name System (DNS) from attacks such as DNS cache poisoning and man-in-the-middle attacks. DNSSEC uses a system of digital signatures and public key cryptography to verify the authenticity of DNS responses. When a domain is signed with DNSSEC, it publishes a digital signature along with its DNS records. When a user requests a DNS record from a DNSSEC-enabled domain, the server responds with the digitally signed record and a public key. The user can then verify the authenticity of the record by using the public key to check the digital
signature.
In summary, [[DNSSEC]] is an important security protocol that ensures the integrity of DNS responses and helps prevent DNS-based attacks.
## DNSSEC record types
There are several types of DNSSEC records, each with a specific purpose. The most common
DNSSEC record types include:
1. DNSKEY: This record contains the public keys (KSK/ZSK) used to verify DNS signatures.
2. DS: This record is used to securely delegate a DNS zone to a child zone. It stores the hash value of the DNSKEY record containing the public Key Signing Key (KSK) from the child zone. This record is important in forming the chain of trust.
3. RRSIG: This record contains the digital signature for a specific DNS record and the public key of the signing zone. Note that RRset contains DNS records like A records. RRset is the one which gets signed and not individual DNS records.
4. NSEC: This record is used to provide authenticated denial of existence for DNS records.
5. NSEC3: This record is similar to the NSEC record, but also includes a hash of the previous and next domain names in the zone. This provides additional protection against zone enumeration attacks.
## DNSSEC Keys
DNSSEC works by digitally signing DNS records with cryptographic keys. These keys are used to validate the authenticity and integrity of DNS records, ensuring that they have not been tampered with or modified.
There are two types of DNSSEC keys:
- Zone Signing Keys (ZSKs)
- Key Signing keys (KSKs)
ZSKs are used to sign the DNS records for a particular zone, while KSKs are used to sign the ZSKs themselves. This creates a chain of trust, where the validity of the ZSKs can be tracedback to the KSKs.
DNSSEC keys are typically stored in a secure location and accessed only by authorized personnel. They must be periodically changed and updated to maintain the security of the DNS system.
On F5 BIG-IP DNS you can use the automatic key management feature to generate and periodically change the keys. The feature uses an automatic key rollover process that uses overlapping generation of a key to ensure that BIG-IP DNS can always respond to queries with DNSSEC-compliant responses. The keys are stored securely on the BIG-IP system itself.
*Note: For KSKs rollover, it requires interaction with the parent zone. Therefore, the end user’s DNS administrator must update the DS record on the parent zone timely, during the rollover period. This has to be highlighted to the end user.*

### Overview on Keys
![[images/DNSSEC_keys.png]]

# Configuring DNSSEC on BIG-IP DNS
**Step 1: Generate Keys**
Determine the values you want to configure for the rollover period, expiration period, and TTL of the keys, using the following criteria:
- The amount of time required to send the DS records for the zone to which this key is associated to the organization that manages the parent zone.
- The value of the rollover period must be greater than half the value of the expiration period, as well as less than the value of the expiration period.
- The difference between the values of the rollover and expiration periods must be more than the value of the TTL.

**A. Generate Zone Signing Key (ZSK)**
1. On the Main tab, click DNS > Delivery > Keys > DNSSEC Key List .
2. Click Create.
3. In the Name field, type a name for the key.
4. From the Type list, select Zone Signing Key.
5. From the State list, select Enabled.
6. From the Hardware Security Module list, select None.
7. From the Algorithm list, select the digest algorithm the system uses to generate the key signature. Your options are RSA/SHA1, RSA/SHA256, and RSA/SHA512.
8. From the Key Management list, select Automatic.
9. In the Bit Width field, type 1024.
10. In the TTL field, accept the default value of 86400.
11. For the Rollover Period setting, in the Days field, type 21.
12. For the Expiration Period setting, in the Days field, type 30.
13. For the Signature Validity Period setting, accept the default value of 7 days.14. For the Signature Publication Period setting, accept the default value of 4 days and 16 hours.
15. Click Finished.
16. To create a standby key for emergency rollover purposes, repeat these steps using a similar name, and select Disabled from the State list.

**B. Generate Key Signing Key (KSK)**
The steps for KSK are the same as creating for ZSK but differs in values for some attributes. The KSK rollover is not as frequent as ZSK. Do note on value differences.
1. On the Main tab, click DNS > Delivery > Keys > DNSSEC Key List .
2. Click Create.
3. In the Name field, type a name for the key.
4. From the Type list, select Key Signing Key.
5. From the State list, select Enabled.
6. From the Hardware Security Module list, select None.
7. From the Algorithm list, select the digest algorithm the system uses to generate the key signature. Your options are RSA/SHA1, RSA/SHA256, and RSA/SHA512.
8. From the Key Management list, select Automatic.
9. In the Bit Width field, type 2048.
10. In the TTL field, accept the default value of 86400
11. For the Rollover Period setting, in the Days field, type 340.
12. For the Expiration Period setting, in the Days field, type 365.
13. For the Signature Validity Period setting, accept the default value of 7 days.
14. For the Signature Publication Period setting, accept the default value of 4 days and 16 hours.
15. Click Finished.
16. To create a standby key for emergency rollover purposes, repeat these steps using a similar name, and select Disabled from the State list.

**Step 2: Create DNSSEC zone**
1. On the Main tab, click DNS > Zones > DNSSEC Zones.
2. Click Create.
3. In the Name field, type the domain name which need be secure by DNSSEC. In my example, I’m using my domain: wip.latzndapz.com
4. From the State list, select Enabled.
5. For the Zone Signing Key setting, assign at least one enabled zone-signing key to the zone.
6. For the Key Signing Key setting, assign at least one enabled key-signing key to the zone.
7. Click Finished.
8. Even if you selected Enabled from the State list, if there are not at least one zone-signing and one key-signing key in the Active column, the status of the zone changes to offline.

**Step 3: Establish chain of trust**
Similar to SSL certificate chaining, DNSSEC needs establish a chain of trust with the parent zone and the parent zone has to establish trust with its own parent zone and so on till the root zone.
This final configuration step is import, because If any part of the chain is broken, the DNSSEC validation fails.
In our scope, we only need establish trust with our immediate parent zone only. The chain after is handled by the respective zone owners.

*Copy DS record from F5 BIG-IP DNS*
1. On the Main tab, click DNS > Zones > DNSSEC Zones.
2. Click on DNSSEC zone you created in the previous step.
3. Click on SEP Records tab
4. Copy the value stated in DS Record section

*Upload DS record to parent zone*
Note: In my lab simulation, I’m using AWS Route 53 to host my parent zone.
The following tasks may not involve you as a F5 implementation engineer as it is usually performed by the end user’s DNS administrator. Therefore, in actual deployments, we are
likely to just send the DS Record details to the end user’s DNS administrators and they would create a DS record using the value we provided in their DNS server.
In this example I’m creating a DS record in my parent zone “latzndapz.com”.
I have now established trust between my child zone “wip.latzndapz.com” and my parent zone
“latzndapz.com”

Next, my parent zone “latzndapz.com” need establish trust with its parent zone “.com”. All we got to do register my parent zone DS record details (not the child zone DS record fromprevious step) with the respective DNS service provider/ Domain name registrar.
In this example AWS Route 53 is my Domain Registrar as well; all I need to do is add my public KSK value. Note other Domain Registrars, typically requests for DS record Digest value
instead of public key so just follow the method provided by your DNS service provider.
