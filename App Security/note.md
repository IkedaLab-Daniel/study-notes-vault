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
