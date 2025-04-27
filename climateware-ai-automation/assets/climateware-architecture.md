# 📃 Climateware AI Automation Prototype — System Architecture

## 🔍 1. Overview

This system automates Climateware's project closure and communication workflows using agentic AI principles. It integrates Jira, HubSpot, GPT-4, Zapier, Google Sheets, and PDF generation services into a simple, functional prototype.

---

## 🛠️ 2. Core Components

| Layer                   | Tool/Service           | Purpose                                           |
|-------------------------|------------------------|---------------------------------------------------|
| Workflow Orchestration  | Zapier                 | Event-driven automation across systems            |
| Trigger System          | Jira                   | Detect project status changes and due dates       |
| AI Content Generator    | GPT-4 (OpenAI API)     | Generate sustainability-focused project reports   |
| CRM Integration         | HubSpot                | Email notifications and engagement tracking       |
| Data Processing         | Python (Zapier Code)   | Simple JSON parsing                               |
| Document Management     | PDF.co                 | Convert structured reports into downloadable PDFs |
| Data Logging            | Google Sheets          | Archive project metadata and outcomes             |

---

## 🔄 3. System Workflow

- **Trigger:** Jira issue status changes to `Done`.

- **AI Report Generation:**
  - Zapier sends project metadata to GPT-4 via OpenAI API.
  - GPT-4 returns a structured JSON sustainability report.

- **Data Parsing:**
  - Python code in Zapier extracts necessary fields (e.g., project summary, CO₂ savings).

- **PDF Generation:**
  - PDF.co service creates a professional project closure report.

- **Email Notification:**
  - HubSpot finds the project manager and sends the PDF link via email.

- **Logging:**
  - Google Sheets logs project name, assignee, CO₂ savings, and completion date.

- **Follow-up Mechanism:**
  - If no feedback within 2 days, a polite reminder email is sent via HubSpot.

- **Deadline Monitoring:**
  - 1 day before the due date, Jira automation sends a reminder email to the assignee.
  - On the due date, if not completed, a second reminder email is sent.
  - If the due date is passed and status is still incomplete, an escalation email is sent to both the assignee and the manager.

---

## 🧑‍💻 4. Agents Involved

| Agent               | Task                                          |
|---------------------|-----------------------------------------------|
| Trigger Agent       | Monitor Jira for status changes to `Done`     |
| Report Generator    | Generate structured sustainability report     |
| Parser Agent        | Extract specific data from JSON               |
| PDF Generator       | Create downloadable PDF documents             |
| CRM Notifier        | Send project closure emails via HubSpot       |
| Logger Agent        | Archive project data into Google Sheets       |
| Follow-up Agent     | Send reminder emails after a delay            |
| Escalation Agent    | Manage overdue project alerts and escalations |

---

## 🌱 5. CO₂ Impact Calculation Methodology

- **Energy Projects:**  
  Formula: `Energy Saved (kWh) × 0.85 kg CO₂/kWh`

- **Transportation Projects:**  
  Formula: `Distance Reduced (km) × 0.12 kg CO₂/km`

- **General Projects:**  
  Estimation based on Low, Medium, or High impact scaling.

---

## 🔥 6. Current Limitations

- No error handling or retry logic is implemented yet.
- No dynamic email reply tracking.
- Basic fallback options (manual intervention required if major failures occur).

---

## 🔮 7. Future Enhancements

| Improvement                                     | Priority | Description                                                                                  |
|-------------------------------------------------|:--------:|----------------------------------------------------------------------------------------------|
| API retry mechanisms (Zapier, OpenAI API)       | High     | Add automatic retries for failed API calls to improve flow reliability.                      |
| Webhook JSON Validation (enhanced robustness)   | Medium   | Implement stricter JSON schema checks to prevent flow failures from malformed data.          |
| Direct PDF attachment in HubSpot emails         | Medium   | Attach the generated PDF file directly in the email instead of sending a link.               |
| CO₂ Impact custom fields inside Jira            | Low      | Add a custom field in Jira tickets to manually or automatically log estimated CO₂ savings.   |
| Dynamic response tracking for follow-ups        | High     | Track email replies automatically and cancel blind follow-up emails if response is detected. |
| Advanced Sustainability Dashboard (Data Studio) | Medium   | Create a dynamic dashboard to visualize CO₂ impact, project status, and automation metrics.  |

---

## 🚀 Conclusion

This prototype marks a foundational step towards Climateware's digital transformation and operational excellence with sustainability-driven agentic AI systems.

