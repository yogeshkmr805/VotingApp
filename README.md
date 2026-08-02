# VotingApp

## Project Description
VotingApp is a simple web app for collecting votes for different candidates. It lets a user submit a vote, view the latest results, and reset the count when needed. The app is easy to run for small demos, classroom activities, or practice projects. It keeps everything in memory while the app is running, so it is quick and lightweight.

## Installation and Setup
Follow these steps to download and run the app on your computer.

1. Open a terminal and go to the project folder:
   ```bash
   cd C:\Users\$Env:USERNAME\
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:
   ```bash
   python app.py
   ```

6. Open the app in your browser:
   ```text
   http://127.0.0.1:5000
   ```

7. To stop the app, press Ctrl + C in the terminal.

## API Endpoint Reference

| Endpoint | Method | What it does | Example response |
| --- | --- | --- | --- |
| /vote/<candidate> | POST | Adds one vote for the candidate you provide. Replace <candidate> with a name such as Alice. | `Vote recorded for Alice!` |
| /results | GET | Shows the current vote counts for all candidates. | `{"Alice": 2, "Bob": 1}` |
| /reset | POST | Clears all saved votes and starts a new round. | `Vote counts have been reset!` |

### Example requests
- Cast a vote for Alice:
  ```bash
  curl -X POST http://127.0.0.1:5000/vote/Alice
  ```

- View the latest results:
  ```bash
  curl http://127.0.0.1:5000/results
  ```

- Reset the votes:
  ```bash
  curl -X POST http://127.0.0.1:5000/reset
  ```

## Git Workflow
I used two branches during this project:
- `main` was used for the stable version of the app.
- `dev` was used for ongoing work and testing before changes were moved to `main`.

A simple flow looked like this:
```text
Start work on dev
   ↓
Test and improve the app
   ↓
Merge approved changes into main
```

## Version History

| Version | What was added |
| --- | --- |
| Version 1 | The first working version of the app with vote casting and result viewing. |
| Version 2 | The second version is added with a feature to reset Vote counts. |

## Screenshots of Application

Endpoint /results
<img width="1916" height="966" alt="image" src="https://github.com/user-attachments/assets/bbec1a71-2486-40ab-8017-4c0e8fb4dbec" />

Branches
<img width="1882" height="965" alt="image" src="https://github.com/user-attachments/assets/e7d45a7b-08cf-447f-9edc-f31f473cc114" />

Version 1 Release
<img width="1891" height="963" alt="image" src="https://github.com/user-attachments/assets/7f1510de-4ab0-4eab-9461-0e8e6ecf2292" />

Version 2 Release
<img width="1881" height="962" alt="image" src="https://github.com/user-attachments/assets/51313c36-01b6-48d2-831d-ca9c5cade439" />

Comparison of v2.0 and v1.0
<img width="1886" height="947" alt="image" src="https://github.com/user-attachments/assets/48f79dc8-9412-48aa-93b9-c11d2276474b" />

