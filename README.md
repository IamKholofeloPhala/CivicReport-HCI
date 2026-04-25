🏙️ CivicConnect Pro
Billion-Dollar Infrastructure Recovery Portal
Redefining Citizen-Government Interaction for Kimberley

🚀 The Vision
CivicConnect Pro is a high-fidelity HCI prototype built to bridge the trust gap between the Kimberley Municipality and its residents. Moving beyond simple form-filling, this platform implements Emotional Design and Real-Time Transparency to turn frustrated citizens into empowered stakeholders.

🛠️ Problem Statement (Based on User Research)
Our research identified two critical failure points in existing systems:

The Trust Gap: Residents reported tickets being falsely marked as "Resolved" by technical teams.

The Communication Void: A total disconnect between the app's status and the actual physical progress of municipal repairs.

✨ Key Features & HCI Principles
This prototype utilizes several Nielsen Heuristics to ensure a "Universal" user experience:

Citizen Verification Loop (Heuristic #7: Flexibility & Efficiency): To stop "False Resolutions," a ticket only closes when the citizen clicks "Verify Fix." If the work is incomplete, the user can trigger a "Dispute Resolution" which escalates the ticket.

Visibility of System Status (Heuristic #1): Using Glassmorphism UI and Animate.css, the interface provides constant feedback. Status-coded cards (Yellow for Pending, Red for Disputed, Green for Resolved) ensure users know exactly where they stand at a glance.

Aesthetic & Minimalist Design (Heuristic #10): Built with Bootstrap 5 and Google Fonts (Outfit), the UI reduces cognitive load by focusing on the "Critical Path"—Reporting and Tracking.

💻 Tech Stack
Backend: Django (Python)

Database: SQLite3

Frontend: HTML5, CSS3, JavaScript

UI Framework: Bootstrap 5.3

Animations: Animate.css

Icons: FontAwesome 6 (Pro-Kit)

🔧 Installation & Setup
To run this billion-dollar prototype locally, follow these steps:

Clone the repository:

Bash
git clone https://github.com/IamKholofeloPhala/CivicReport-HCI.git
cd CivicReport-HCI
Initialize the Database:

Bash
python manage.py makemigrations
python manage.py migrate
Launch the Portal:

Bash
python manage.py runserver
Access the UI: Open http://127.0.0.1:8000/ in your browser.

📈 HCI Prototype Evolution
"In HCI, the interface is the product."
