# SAML Identity Federation Demo (1 IdP, 2 SPs)

This project demonstrates a simple **SAML identity federation** setup consisting of:

- **One Identity Provider (IdP)** → `idp.example.com` (localhost:8000)  
- **Two Service Providers (SPs)** → `sp1.example.com` (localhost:8001) and `sp2.example.com` (localhost:8002)  

The flow:
1. A user visits **SP1** and clicks "Login via IdP".  
2. The user is redirected to the **IdP**.  
3. If not logged in yet, the IdP asks for a username.  
4. Once authenticated, the IdP generates a **SAML Response** and sends it to SP1.  
5. The user can then visit **SP2**, where SSO happens automatically (no login form is shown again).  
6. Both SPs display the decoded SAML Response.  
7. A **logout endpoint** is provided at the IdP to clear the session.

---

## ⚙️ Requirements

- Python 3.8+  
- Flask  

Install dependencies:

 ```bash
  pip install flask
```
📂 Project Structure
```bash
saml-project/
│
├── idp/
│   └── run_idp.py      # Identity Provider
│
├── sp1/
│   └── run_sp1.py      # Service Provider 1
│
└── sp2/
    └── run_sp2.py      # Service Provider 2

```
▶️ How to Run

Start the IdP (port 8000):
```bash
cd idp
python run_idp.py
```
Start SP1 (port 8001):
```bash
cd sp1
python run_sp1.py
```
Start SP2 (port 8002):
```bash
cd sp2
python run_sp2.py
```
🌐 Access the Services:</br>
  - Open [SP1](http://localhost:8001) → SP1 Home  
  - Open [SP2](http://localhost:8002) → SP2 Home

🔑 Flow Demonstration
 - Go to SP1 and click Login via IdP.
 - You will be redirected to the IdP login form.
 - Enter a username (e.g. alice@example.com).
 - You are redirected back to SP1, which shows the decoded SAML Response.
 - Now visit SP2.
 - You will not see the login form again → the IdP session is reused (SSO).
 - SP2 shows the decoded SAML Response.

🚪 Logout

 - To log out and clear the IdP session:
 - Go to [logout](http://localhost:8000/logout)
 - Or click the Logout link from SP1/SP2 home page.
 - After logging out, revisiting an SP will ask for username again.
 



