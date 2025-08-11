## Application Security for Developers and DevOps Professionals Summary

* Focus: Application security for software engineers, not infrastructure security.
* Security issues from decades ago still persist today (many appear in OWASP Top 10).
* IBM report:

  * Average breach detection time: **212 days** (7+ months).
  * Average breach cost: **\$9.4M (US)**, **\$4.3M (global)**.
* Many breaches result from poorly implemented security features.
* Goal: Practice **security by design**.
* Topics covered:

  * **DevSecOps**: Proactive integration of security into development.
  * **Network security**: TLS, OpenSSL.
  * **Security planning**: Mapping security into the development process to recover and prevent attacks.
  * **Vulnerability scanning**, **threat modeling**, **threat monitoring**.
  * **Security testing**: Tools and procedures to mitigate risks.
* Hands-on labs:

  * Static & dynamic analysis tools.
  * OWASP Top 10 vulnerabilities & exploitation.
  * Vault secrets manager (UI & programmatic access).
  * Checking/testing code, dependencies, and environments.
* Outcome:

  * Understand common risks and vulnerabilities.
  * Learn defensive coding practices.
  * Be prepared to secure applications before deployment.
* Emphasis on **collaboration**, **team-based learning**, and **practical exercises**.

## Security by Design Summary

* **Security by Design**: Integrating security from the start rather than treating it as an afterthought.
* **Collaboration**: Involve security teams early and regularly to ensure secure coding practices.

### Secure Software Development Lifecycle (SDLC)

Stages:

1. **Requirements** – Understand customer expectations.
2. **Design** – Make design decisions based on requirements.
3. **Develop** – Implement the design.
4. **Test** – Verify functionality and quality.
5. **Deploy** – Release the tested product to production.

### Secure SDLC Enhancements

* Integrates security practices into each SDLC phase.
* Activities:

  * Risk assessment
  * Threat modeling & design review
  * Static analysis
  * Security testing & code review
  * Security assessment & configuration

### Mapping DevOps to Secure SDLC

* **Requirements**: Risk assessment, define security requirements, identify sensitive data, attack profiling.
* **Design**: Threat modeling, identify vulnerabilities in architecture, secure design, secure CI/CD pipeline setup, automate security tests.
* **Develop**: Static analysis, validate automated data, apply secure scrum, integrate security tasks.
* **Test**: Vulnerability scans, security testing, risk assessment before launch, break testing, parallelize tests using scanners with unit and functional tests.
* **Deploy**: Automated deployment scripts, deploy & rollback processes, production security testing simulating real-world attacks.

### Key Takeaways

* Collaboration with security teams enhances feature implementation.
* Secure SDLC embeds security best practices into all development phases.
* Risk assessment and proactive threat analysis reduce vulnerabilities.

## What is DevSecOps Summary

* **Definition**:
  DevSecOps integrates security practices across the **entire SDLC**—from design to delivery—embedding security into DevOps workflows to reduce risks and align with enterprise IT goals.

* **Core Components**:

  * **Development** – New releases and updates
  * **Security** – Accessibility, integrity, confidentiality
  * **Operations** – Performance, reliability, scalability

* **Key Benefits**:

  1. **High-quality, cost-effective software delivery** – Reduces delays, avoids redundant reviews/rebuilds, lowers development costs.
  2. **Proactive security** – Detect and remediate vulnerabilities early; improves compliance; allows security teams to focus on higher-value tasks.
  3. **Faster vulnerability patching** – Integrates scanning and patching into release cycles to reduce exposure time.
  4. **Modern automation** – Security tests (static/dynamic), CI/CD integration, automated dependency checks, immutable infrastructure for stronger protection.
  5. **Repeatable & adaptable processes** – Uniform security application across evolving environments; supports orchestration, containers, serverless computing for faster recovery after incidents.

* **Key Takeaway**:
  DevSecOps = DevOps with **security built-in at every step**, enabling continuous, automated, and adaptive protection from development to production.

Summary & Highlights - Introduction to DevSecOps

* The secure software development lifecycle (SDLC) is a process that involves security testing and its best practices in the existing development model. 

* SDLC stages are requirements, design, development, testing, and deployment. You can map secure SDLC to these stages by undertaking risk assessments and looking at how individuals may attack your code. 

* DevSecOps automates security integration throughout the concept, implementation, testing, deployment, and delivery SDLC process. 

* DevSecOps provides higher-quality software, improved security, vulnerability fixings, and faster recovery after a security incident. 

## **The OSI Model Overview**

* **Purpose**: A standardized 7-layer framework for sending and receiving data globally.
* **Goal**: Enable consistent, interoperable communication for present and future technologies.

---

### **The Seven Layers** (bottom to top):

1. **Physical Layer**

   * Transmits raw bits over a physical channel.
   * Example: Cables, connectors, voltage signals.

2. **Data Link Layer**

   * Converts raw bits into **error-free frames**.
   * Uses acknowledgments to confirm correct reception.
   * Example: Ethernet, MAC addresses.

3. **Network Layer**

   * Handles routing and delivery of packets.
   * Determines optimal path from source to destination.
   * Example: IP addressing, routing tables.

4. **Transport Layer**

   * Splits data into smaller packets and ensures correct order and delivery.
   * Example: TCP (ordered, reliable) and UDP (faster, no ordering guarantee).

5. **Session Layer**

   * Manages sessions between devices.
   * Provides dialog control, token management, and synchronization for long transmissions.

6. **Presentation Layer**

   * Translates, compresses, encrypts, and decrypts data.
   * Example: JPEG, ASCII, TLS encryption.

7. **Application Layer**

   * Interface for user applications and network services.
   * Example: HTTP, HTTPS, FTP, email.

---

### **Developer Focus** – Top 3 Layers:

* **Session Layer** – Manages client-server sessions.
* **Presentation Layer** – Secure socket encryption, data format handling.
* **Application Layer** – Use HTTPS (port 443) for secure communication, avoid unsecured HTTP.

---

### **Key Takeaways**

* OSI = **Physical → Data Link → Network → Transport → Session → Presentation → Application**.
* Developers should **prioritize security** at layers 5–7 to protect against threats like man-in-the-middle attacks.
* HTTPS, encryption, and secure session handling are essential for user trust.

## Securing Layers for Application Development

* Importance: Securing each layer is essential for protecting applications.

* Four security layers:

  1. **Web Application Layer** – Includes front end (JavaScript, CSS, HTML with HTTPS), middle layer (API in Python, Java, Ruby), and back end (databases). Secure by running vulnerability scanners, tests, and audits before production.
  2. **Cloud Infrastructure Layer** – Protect cloud databases (usernames, passwords, confidential info). Avoid storing admin credentials in code. Use security groups to restrict access, implement two-factor authentication, and apply strong authentication measures.
  3. **Communications Layer** – Secure connections with SSH, HTTPS, SSL/TLS to prevent man-in-the-middle attacks. Use SSH for safe remote server connections when uploading, deploying, and testing code.
  4. **Security Code Delivery Pipeline Layer** – Restrict code repositories (e.g., GitHub) with permissions, periodic audits, and two-factor authentication. Configure IAM for cloud assets based on roles and needs. Store secrets (passwords, certificates, encryption keys) in services like HashiCorp Vault.

* **Logging** – Collect and store logs to identify anomalies (e.g., unauthorized admin login attempts). Restrict log access to trusted reviewers.

* **Intrusion Detection** – Detect ongoing threats through:

  * Endpoint security (protect systems, servers, devices).
  * Network security (monitor with tools like Nmap, Snort).
  * System-call auditing (analyze kernel-level calls, e.g., Linux kernel).

## What is OpenSSL

* **Confidentiality** – Keeps data secret from unauthorized users, even on insecure networks, using cryptographic keys (private/public). Ensures e-commerce transactions remain secure.
* **Integrity** – Guarantees data has not been altered during or after transmission. Methods like file checksums verify data authenticity and prevent tampering.
* **OpenSSL** – An open-source toolkit implementing the SSL protocol to provide secure communications.

  * Features: Symmetric & public key cryptography, message digests, hash algorithms, pseudorandom number generator, key management, and support for common certificate formats.
  * Usage: Can be integrated into applications or run via command line (`openssl` on Linux/Mac, `openssl.exe` on Windows). Offers configuration files for defaults and customization.
* **Message Digest Algorithms** – Cryptographic hash functions that compute checksums of data blocks, sign data, and verify signatures.
* **Symmetric Ciphers** – Encryption using the same key for both encryption and decryption.
* **Public Key Cryptography** – Uses public and private keys.

  * **RSA**: Popular implementation providing secrecy, authentication, encryption, and prime number generation for private keys with various key lengths.

## Summary and Highlights - Understanding the Role of Network Security

* OSI model is a system that allows for present and future types of communication to be used by everyone globally.

* The OSI model consists of seven layers for sending and receiving data. The first layer is the physical layer, then the data link layer, the network layer, the transport layer, the session layer, the presentation layer, and finally the application layer.

* Securing the communications layer is important to manage using SSH, HTTPS, SSL/TLS, or the secure sockets layer.

* When application developers need to commit code to an application project, the security code delivery pipeline layer should be secured and restricted.

* Security patterns are a set of rules that represent and define a reusable solution to recurring security threats or issues.

* Transport Layer Security (or TLS) and Secure Sockets Layer (or SSL) are protocols for establishing secure connections or communications between networked computers, specifically a server and a client.

* TLS works effectively when the server has an up-to-date certificate and TLS version support.

* OpenSSL is an open-source toolkit that uses a command line and software libraries to ensure secure communication with cryptography for all types of communication, from personal to commercial and e-commerce transactions.

## Vulnerability Scanning and Threat Modeling

Vulnerability scanning is the search for security vulnerabilities from within the code and from the outside of an application. Scanners search in code languages such as C, C++, Java, Python, and PHP, targeting vulnerabilities like SQL injection, cross-site scripting, and path traversal. Scans should be based on platform configuration, patch levels, or application composition, and may require user credentials to analyze the full application flow across the stack and supporting platforms. Popular scanning tools include:

* **Coverity** – incremental analysis for C, C++, Java, Python.
* **CodeSonar** – uses abstraction to model code and find weaknesses.
* **Snyk Code** – integrated semantic analysis tool for coding and security bugs.
* **Static Reviewer** – eliminates known vulnerabilities, compliant with OWASP, CVEs, and NIST.

Threat modeling is identifying, categorizing, and enumerating security threats, analyzing ongoing threats, and eliminating potential software weaknesses. It uses diagrams to represent data flows in applications and is best applied during the design phase of the SDLC to reduce vulnerabilities. Common models include:

* **PASTA** – risk-based, linking business objectives with technical requirements.
* **VAST** – agile, with application and operational threat models using process-flow diagrams.
* **STRIDE** – identifies Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privileges.

Vulnerability scanning ensures complete coverage of the application flow, while early threat modeling helps eliminate weaknesses in applications.
