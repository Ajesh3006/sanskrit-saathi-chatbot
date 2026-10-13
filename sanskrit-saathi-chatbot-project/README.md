# Sanskrit Saathi — Sanskrit Phrase Chatbot

A small educational chatbot built with **Python and Flask**, with a responsive web interface, GitHub version control, Jenkins CI, and Docker containerization.

## Features
- Browser-based chat UI with quick prompt buttons
- Phrase-based replies for greetings, thanks, and help
- JSON chat endpoint (`POST /chat`)
- Health endpoint (`GET /health`)
- Jenkins pipeline: checkout → install → validate/test → Docker build
- Docker image: `sanskrit-saathi-chatbot:latest`

> This is a phrase-matching demo, not a generative AI model or a reliable Sanskrit translation system.

## Run locally
Python 3.10+ recommended.

```bash
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Test endpoints
```bash
curl http://127.0.0.1:5000/health
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message":"thanks"}'
```

## Run with Docker
```bash
docker build -t sanskrit-saathi-chatbot:latest .
docker run --rm -p 5000:5000 sanskrit-saathi-chatbot:latest
```
Then open http://127.0.0.1:5000

## GitHub setup
Create an empty repository on GitHub (for example `sanskrit-saathi-chatbot`), then run these commands from this folder:

```bash
git init
git add .
git commit -m "Initial Sanskrit Saathi chatbot"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/sanskrit-saathi-chatbot.git
git push -u origin main
```
Replace `YOUR-USERNAME` with your GitHub username. Do not use another student's credentials or claim their repository as your own.

## Jenkins setup
1. Install Jenkins and ensure the machine has Git, Python 3, pip, and Docker installed.
2. Add the current repository as a **Pipeline** job source.
3. Set the repository URL and branch to `*/main`.
4. Select **Pipeline script from SCM**, SCM **Git**, and script path `Jenkinsfile`.
5. Run **Build Now** and inspect each stage. The Jenkins agent must have permission to run Docker.
6. On Linux, this Jenkinsfile uses `sh`; on a Windows-only Jenkins agent, convert commands to `bat` or use a Linux agent.

## Meaningful version-control update
After the first commit, change a response in `app.py` (for example, improve the reply for `thanks`), then:

```bash
git add app.py
git commit -m "Improve thank-you response"
git push
```
Run the Jenkins job again to show that the latest GitHub commit is checked out and validated.

## CI flow
GitHub → Jenkins checkout → dependency installation → Python validation and Flask endpoint tests → Docker image build.
