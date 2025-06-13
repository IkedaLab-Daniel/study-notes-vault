# Module 5: Authenticate and authorize user identities on GitHub

## Unit 1: Introduction
User authentication has traditionally been achieved using a User ID and password. A password is a single-factor form of authentication. The fundamental issue with single-factor authentication is that it's easier for any bad actor with knowledge of the sign-on information to impersonate the valid user. To prevent a breach of security for a user account, GitHub has authentication tools available to promote security best practices. You can even enforce a security policy for all GitHub users within the organization.

Controlling access to your company's data is foundational for a secure GitHub Enterprise. GitHub is committed to helping enterprises on their security journey with authentication methods to allow for more secure account access and a better user experience. In a GitHub Enterprise, most organizations want to require extra levels of authentication for better security. Enterprise System Administrators can enforce authentication and authorization security policies across an organization. These security features allow you to ensure that users are required to sign on securely to access the correct permissions in repositories. These features also include access and tools for auditing user access and activity, identity maintenance, and authentication compliance. As an administrator, you should work with your internal resources to identify what type of authentication and authorization is appropriate. This module provides an overview of the authentication and authorization options available to you in your GitHub organization or GitHub Enterprise.

## Unit 2: User identity and access management
Authentication is the gateway to your enterprise's software development ecosystem. Every user's interaction with GitHub begins with identity verification. While individual accounts can rely on usernames and passwords, strong enterprise security mandates two-factor authentication (2FA) or more advanced methods like passkeys and biometric login. Balancing usability with security is key—especially in a fast-paced development environment.

### Modern Authentication in GitHub Enterprise
To ensure a secure and streamlined authentication experience, GitHub supports multiple modern methods that integrate with your identity management systems:

#### Passkeys and WebAuthn
- Passkeys are a passwordless login method, tied to a physical device, and resistant to phishing.
- WebAuthn supports biometric factors and hardware tokens like YubiKey.
- These methods significantly reduce credential-based attacks and improve login UX.

#### GitHub Mobile for 2FA
Users can authenticate with GitHub Mobile, which supports push notifications for quick, secure approval—enhancing 2FA without disrupting workflows.

#### OAuth and GitHub Apps
- OAuth Apps use GitHub's OAuth 2.0 flow to authenticate users and grant scoped access to external applications.
- GitHub Apps authenticate as individual installations with fine-grained permissions and are ideal for CI/CD and automation pipelines.

#### Enterprise Managed Users (EMU)
In GitHub Enterprise Cloud, EMUs ensure that authentication happens strictly through your Identity Provider (IdP). This model:
- Restricts access to enterprise-managed accounts only.
- Enforces centralized control over identity, credentials, and session policies.

Organization Management with SAML SSO
One foundational capability for enterprise-grade authentication is SAML Single Sign-On (SSO). SAML links your IdP with GitHub, enabling users to sign in across services using one set of credentials. GitHub uses the IdP to verify user identity before granting access to organization or enterprise resources.

When users log into GitHub, they can see the enterprises they belong to—but access to repository data requires SAML reauthentication via the IdP.

## Unit 3: User authentication
When it comes to user authentication, security should be the number one consideration that comes to mind. Strong security is essential. It seems like every month or so, a company reports a data breach. Credentials are stolen because of inefficient security processes, or simply because of a lack of up-to-date security features within the company. Establishing secure user authentication can be a difficult task if user adoption requires long and frustrating steps to authenticate.

GitHub Enterprise supports two recommended methods for secure user authentication:
- SAML Single Sign-On(SSO)
- Two-Factor Authentication(2FA)

### SAML SSO Authentication
SAML(Security Assertion Markup Language) SSO integrates GitHub with your organization’s identity provider (IdP), allowing centralized access control, and improved compliance. When enabled, GitHub redirects users to the IdP for authentication before granting access to organization resources.

### Two-Factor Authentication (2FA)
2FA adds a second verification step beyond username and password. You can require 2FA for organization members, outside collaborators, and billing managers.

When you require the use of two-factor authentication for your organization, all accounts that don't use 2FA is removed from the organization and lose access to its repositories. Accounts that are affected include bot accounts.

## Unit 4: User authorization
After a user successfully authenticates through your identity provider (IdP) by using SAML single sign-on (SSO), the next critical step is authorization—granting tools like personal access tokens (PATs), SSH keys, or OAuth apps with the ability to access organization resources.

### Automating User Authorization with SAML SSO and SCIM
Security assertion markup language (SAML) SSO enables enterprise and organization owners to control access to GitHub resources like repositories, issues, and pull requests. Integrating SCIM (System for Cross-domain Identity Management) enhances access control by automating user provisioning and deprovisioning.

With SCIM, new employees added to your IdP are granted access to GitHub automatically, while departing users are removed, reducing manual steps and improving security.

SCIM also revokes stale tokens after a session ends, reducing security risks. Without SCIM, revoking stale tokens must be done manually.

### Managing SSH Keys and PATs with SAML SSO
SAML SSO and SCIM work together to reflect identity changes in GitHub. To support this cohesion:
- NameID and userName must match between the SAML IdP and SCIM client.
- Group changes in your IdP trigger SCIM updates in GitHub.
Users accessing APIs or Git must use an authorized PAT or SSH key. These methods are auditable and securely tied to SAML SSO.

To simplify onboarding, provision users using: https://github.com/orgs/ORGANIZATION/sso/sign_up. Display this link in your IdP dashboard.

When users first authenticate, GitHub links their account and SCIM data to your organization. Admins can later audit or revoke sessions and credentials to automate offboarding.

### SCIM Integration with GitHub
SCIM streamlines identity management in GitHub Enterprise Cloud by supporting both native integrations and custom configurations.

#### Supported SCIM Providers
- Okta
- Microsoft Entra ID
- OneLogin
- Ping Identity
- Google Workspace

### Managing Identities and Access

#### SAML SSO Configuration
1. Configure your SAML SSO URL.
2. Provide your public certificate.
3. Add IdP metadata.

### Credential Management
PATs and SSH keys must be explicitly authorized and linked to IdP identities to access organization resources securely.

## Unit 5: Team synchronization
If your company uses Microsoft Entra ID or Okta as your identity provider (IdP), you can manage GitHub team membership through team synchronization. When enabled, team sync automatically reflects changes in IdP groups on GitHub—reducing the need for manual updates or custom scripts. This centralized approach simplifies onboarding, permissions management, and access revocation.

### Team Synchronization Use Cases
Team sync is ideal for enterprises looking to streamline membership management within GitHub organizations. Admins can map GitHub teams to IdP groups and manage memberships automatically. This is useful for:

- Onboarding new employees
- Adjusting access as users move between teams
- Removing users who leave the organization

### Enterprise Managed Users
If you're using Enterprise Managed Users in GitHub Enterprise Cloud, all members are provisioned through your IdP. Users don't self-manage GitHub accounts and can't access resources outside the enterprise.

With this model, you can:
- Manage organization/team membership directly through your IdP
- Ensure GitHub users are enterprise-scoped and isolated

### Team Synchronization vs. SCIM for GHES
In GitHub Enterprise Server (GHES), managing user access and team memberships can be achieved through various methods, including team synchronization and System for Cross-domain Identity Management (SCIM). Understanding these methods is essential for effective administration.

#### Team Sync in GHES
Team synchronization allows you to link GitHub teams with groups in your Identity Provider (IdP). This integration ensures that any changes in the IdP group—such as adding or removing members—are automatically reflected in the corresponding GitHub team. This approach streamlines team management by centralizing user access control within the IdP.

However, it's important to note that team synchronization isn't a user provisioning service and doesn't invite non-members to join organizations in most cases. Therefore, a user will only be successfully added to a team if they're already an organization member.

Consider the following scenario to understand how team synchronization works in practice:

### Team Sync Configuration
1. Enable Security Assertion Markup Language(SAML) Single Sign-On(SSO) and SCIM in your IdP.
2. Map GitHub teams to IdP groups via GitHub UI or API.
3. Changes in group membership sync automatically to GitHub.
Supported IdPs:

1. Microsoft Entra ID: Requires permissions for profile reading and directory access.
2. Okta: Requires SAML SSO, SCIM, tenant URL, and Single Sign-on for Web Systems(SSWS) token with read-only admin access.

### Disable Team Sync
To disable:

1. Navigate to Settings > Organization security
2. Click Disable team synchronization

### SCIM in GHES
SCIM is an open standard protocol designed to automate the exchange of user identity information between identity domains and IT systems. In the context of GHES, SCIM enables administrators to provision, update, and deprovision user accounts directly through the GitHub API. This means you can create, update, and delete user accounts, and sync group information to map GitHub team memberships.

SCIM is useful for managing user lifecycles at scale, ensuring that user data remains consistent across systems.

Consider the following scenario to understand how SCIM works in practice:
- Okta SCIM integration provisions GitHub users automatically
- Bob is added to Okta → GitHub account is provisioned
- Bob changes roles → access and teams update
- Bob leaves → account is deprovisioned

### Team Sync vs. Group SCIM
GitHub supports two primary identity integration approaches:

- Team Sync: Focused on syncing group membership to GitHub teams
- Group SCIM: Focused on full lifecycle management of users and groups

### Usage Limits
When using team synchronization, observe these limits:

- Max members per team: 5,000
- Max members per organization: 10,000
- Max teams per organization: 1,500

Exceeding these may result in performance issues or sync failures.