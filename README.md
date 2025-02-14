# python-jenkins
this is my jenkins project
# Python GitHub Actions CI/CD

A simple Python project with **GitHub Actions** for CI/CD, running **pytest** for testing and deploying on `staging` and `main` branches.

## Tech Stack
- **Python 3.x**
- **GitHub Actions** (CI/CD)
- **Pytest** (Testing)

## Setup Instructions

### 1️⃣ Clone the Repo & Install Dependencies
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

python app.py

CI/CD Workflow
Located at .github/workflows/ci-cd.yml, the workflow:

Runs on: push to main or staging
Jobs: Install dependencies → Run Tests → Deploy
Deployment:
Staging: Push to staging branch
Production: Release tagged on main branch
