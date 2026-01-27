---
category:
  - Networking
tags:
  - ssl
  - ssl_certificate
  - csr
published: false
date: 2024-10-16T16:53:00
excalidraw-plugin: parsed
excalidraw-open-md: true
---

### **1. Create a Self-Signed Certificate**

#### **Step 1: Generate the Private Key**

`openssl genpkey -algorithm RSA -out privatekey.key -pkeyopt rsa_keygen_bits:2048`

- `openssl`: Calls the OpenSSL command-line tool.
- `genpkey`: This command generates a private key.
- `-algorithm RSA`: Specifies that the RSA algorithm will be used for key generation.
- `-out privatekey.key`: Specifies the output file name for the private key, `privatekey.key`.
- `-pkeyopt rsa_keygen_bits:2048`: Defines the length of the key in bits, in this case, 2048 bits.

This command generates a 2048-bit RSA private key and saves it as `privatekey.key`.

#### **Step 2: Create the Certificate Signing Request (CSR)**

`openssl req -new -key privatekey.key -out request.csr`

- `req`: Tells OpenSSL to generate or process a certificate request (CSR).
- `-new`: Indicates that a new CSR is being created.
- `-key privatekey.key`: Uses the private key (`privatekey.key`) that was generated in Step 1.
- `-out request.csr`: Specifies the output file for the CSR (`request.csr`).

During this step, OpenSSL will prompt you for information such as Country, State, Organization, Common Name (FQDN), etc. This data will be included in the CSR.

#### **Step 3: Generate a Self-Signed Certificate**

`openssl req -x509 -nodes -days 365 -key privatekey.key -in request.csr -out certificate.crt`

- `req`: Again, this indicates the request processing operation.
- `-x509`: Specifies that a self-signed certificate (X.509) will be created instead of a regular CSR.
- `-nodes`: Ensures that the private key will not be encrypted.
- `-days 365`: Defines the validity of the certificate, in this case, 365 days.
- `-key privatekey.key`: Uses the private key generated earlier.
- `-in request.csr`: Uses the CSR that was created in Step 2.
- `-out certificate.crt`: The final self-signed certificate will be output to `certificate.crt`.

This command generates a self-signed certificate (`certificate.crt`) that is valid for 365 days.

### **2. Create a CSR for CA-Signed Certificate**

#### **Step 1: Generate the Private Key**

`openssl genpkey -algorithm RSA -out privatekey.key -pkeyopt rsa_keygen_bits:2048`

Explanation: Same as in the self-signed certificate process. This creates a private key named `privatekey.key`.

#### **Step 2: Create the Certificate Signing Request (CSR)**

`openssl req -new -key privatekey.key -out request.csr`

Explanation: Same as in the self-signed certificate process. This generates a CSR (`request.csr`).

#### **Step 3: Submit the CSR to a Certificate Authority (CA)**

After creating the CSR, you would send `request.csr` to a CA (e.g., Let's Encrypt, DigiCert). The CA will sign the CSR and issue a certificate, which you'll typically receive as a `.crt` or `.pem` file.

#### **Optional Step 4: Verify the CSR**

You can inspect the contents of the CSR to verify the details:

`openssl req -noout -text -in request.csr`

- `-noout`: Suppresses the output of the encoded CSR.
- `-text`: Displays the CSR in human-readable format.
- `-in request.csr`: Specifies the CSR file to inspect.

This will display the details of the CSR you generated, like the Subject (organization, FQDN), public key information, and extensions.




%%
# Excalidraw Data
## Text Elements
%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebTiADho6IIR9BA4oZm4AbXAwUDAiiBJuCAAxAEYeAFEAGSEAaQAlTShiAC0ASQBrAHkAYQoARyFiADZkoshYRDKAM0CETyp+

YsxuHgB2AGZtLYBWNcgYbmcdhK3jiAoSdW4ABm0Hl8rryQRCZWlH59fr6zKYKPa7MKCkNg9BADNj4NikMoAYkqCBRKKmxU0uGwPWUEKEHGIMLhCIk4OszDguECmQxkHmhHw+AAyrBgRJBB46RAwRCoQB1O6STag8GQhCsmDs9Cc0rXfHfDjhbJoN75SBsKnYNSnVUva544RwLrEFWoHIAXWui1w6RN3A4QiZ10IhKwZVwD25+MJSuYZsdzvVPIQy

24lUOCQALJUdgdKuNrowWOwuGgjsHk6xOAA5ThiTZRqM7ACcWwjfGDhGYABFUlAw2hwUIENdNMJCTVgulMgGnfhrkI4MRcA3iOGtjxYwl41txlGHmrphAiBweg7+9c4TjG6h5gQwtc4GxXVlcuqwHlpkUHscbxerRer9eni9F3ewK/Xg/1Y/l3BAn9ERwlyP9ilYfQnVHBAAAVAOYYDuGbVtg3wUIoBhfR9DUMcYJPWk0GfG8/nfC8v0XX98gAXz

WQpilKCQhB4DpnAAQXGYZWNwHgowAITEGBmQACQADWcGoAH1uVmcR0EWUMVm5DY0C2BJxn2DNl11VBnCjA4EmuW5iHuNByKXYoPi+H5TJI8zIEBaVb2DXlxWJeEkTRVEkDbbFcR9IlYXcslyA4SlqQyKBuQZJlJWlHlYTlZyxQFIURSSvkJTZWT4q5eVhEVZVw2uTVsR1cN9WDQ0hxNM1LWtcg7XHNBAwHKs3WU9BcEqb0O2IP0+yDZcwl3HgHhL

KNxhLA4Sx4pMmGzNNUE04os1TPMOALNAdkqB4EkqGddpdWt613ZC216rs0gigbWuXIcRzHCcpwueMEh2csdi3V112azdULYHcmr3A8UP/fCz0Ip8L0/D8HgfO8iOIt87KR79rwtX8j3g4DarAgRCEgtCGzg5VEKbUgWy3dDMOwmRljw09zxfWy7zMyiiio8A/wgXA4DgVloO4OjoA+dIyiIb5IrWBhCAQCheN8qrCTc0l0EReYNc1jEIGwEQaSgL

oG30VkMpVjyvPRaXddIfXDbSBWcSVgKSTKclQqpfXtet22jfKRkWSyspZXHK29Yiu3jeShBBWM4U0ErYpvfDo2TfFWLsuDr2w8yCPmnyyR+qK/Idezg2jb6LUyr1JzE9LiPyk4KByltRltPMkubeTtIG8yZlCCMWTRtDzuc6NgAVLAoFYiXFpXBB5il4uk9HtIBdIKebbYCgPlwIGWuHn20hqQlWM37eQiBnmz+15hsAhJkRO4VT1MOaXb/v/AAE

1uAmgzi6MNgBghaZgIC2cM1ED5d30HnAkfVCoSH8trPEJA+4Dw3INSAyDnZBVQHRSAvFYSX0RAMEsJCSHlHKNyZoCBlBQVVhARENQaxMKYRQiAECl6l1TlCCuUBUw3WlgBBAZhhDMAAOKkBQf3WS+9i42nSNQt0kiODKGAcuDIuBNDBCBmdYM2AiBwCQhTUGxQOC2lkro5cwgoCrgscYjhxQ7AACsEDYCyMyMxcAACybBiAIGPpo7R3B9z4DCOAG

idBoogTQMATmVEgA
```
%%