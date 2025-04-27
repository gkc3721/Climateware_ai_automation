# 🌍 Climateware AI Automation Prototype

**Multi-agent workflow automation for sustainability operations**  
*Jira + HubSpot + GPT-4 + Zapier Integration | Case Study Submission*

---

## 📌 Case Study Overview

This prototype showcases an **agentic AI workflow** designed to automate Climateware’s internal operations, focusing on:

- Automated project closure through Jira
- AI-generated sustainability impact reports
- Stakeholder communications via HubSpot
- Deadline reminders and escalation mechanisms

> *"How might we leverage multi-agent systems to reduce manual tasks and enhance visibility into climate impact?"*

---

## 🛠️ Tech Stack

| Component              | Technology                | Purpose                                     |
|------------------------|---------------------------|---------------------------------------------|
| Workflow Orchestration | Zapier                    | Low-code automation across systems          |
| AI Content Generator   | GPT-4 (OpenAI API)        | Sustainability-focused report generation    |
| CRM Integration        | HubSpot                   | Email notifications and engagement tracking |
| Project Management     | Jira                      | Issue tracking and task management          |
| Data Storage           | Google Sheets             | Project metadata archiving                  |
| Document Generation    | PDF.co                    | Automated PDF report creation               |
| Custom Processing      | Python (Zapier Code Step) | JSON parsing and error handling             |

---

## 🔥 Key Features

### 1. Multi-Agent Workflow

- **Trigger Agent:** Detects when Jira Issue status changes to `Done`.
- **Report Generator Agent:** GPT-4 generates structured sustainability closure reports.
- **Parser Agent:** Python code extracts and formats JSON outputs.
- **PDF Creator Agent:** Converts the structured report into a professional PDF.
- **CRM Notifier Agent:** HubSpot sends closure emails to stakeholders.
- **Logger Agent:** Archives project data (title, assignee, CO₂ savings) into Google Sheets.
- **Follow-up Agent:** Sends a reminder email after 2 days if no feedback is received.
- **Escalation Agent:** Manages deadline alerts and overdue project escalations.

### 2. Sustainability Integration

- **Energy Projects:** `0.85 kg CO₂/kWh`
- **Transportation Projects:** `0.12 kg CO₂/km`
- **Other Projects:** Low/Medium/High estimation tiers

The report generation transparently explains the CO₂ saving formula or assumptions used.

### 3. Blind Follow-up System

- Automatically sends a follow-up email 2 days after the first mail.
- Includes a polite disclaimer: *"If you have already responded, please disregard this message."*

### 4. Deadline Management

- **T-1 Day:** Reminder email sent to the project assignee.
- **On Deadline (if incomplete):** Escalation alert sent to both assignee and manager.

---

## 📊 Business Impact

| Metric                     | Result                        |
|----------------------------|-------------------------------|
| Time Saved                 | ~23 hours/month               |
| Error Reduction            | ~70% fewer manual errors      |
| Process Acceleration       | ~5× faster project closures   |
| Sustainability Reporting   | ~95% CO₂ estimation coverage  |

**Estimated ROI:**

- **Automation Cost:** ~$69/month (Zapier + GPT-4 API)
- **Time Value Saved:** ~$1,150/month
- **Calculated ROI:** ~**1,565%**

---

## 📂 Repository Structure

```bash
/climateware-ai-automation
├── README.md
├── LICENSE
├── /assets
│   ├── zapier-flow.png
│   └── project-architecture.png
├── /docs
│   └── climateware-architecture.md
├── /demo-video
│   └── prototype-demo.mp4
├── /workflows
│   └── zapier-export.json
├── /prompt-design
│   └── gpt4-prompt-climateware.txt
├── /templates
│   └── project-report-template.html
├── /sample-outputs
│   ├── sample-project-log.xlsx
│   └── sample-final-pdf.pdf
└── .gitignore
```

---

## 📻 Demo Video

📹 **[Click here to watch the prototype demonstration](demo-video/prototype-demo.mp4)**  
(*Video is stored inside `/demo-video/` folder in this repository.*)

---

## 🔮 Future Roadmap

| Enhancement                                     | Priority |
|-------------------------------------------------|:--------:|
| API retry mechanisms                            | High     |
| Dynamic HubSpot reply tracking                  | Medium   |
| Direct PDF attachment in HubSpot emails         | Medium   |
| CO₂ Impact custom fields in Jira                | Medium   |
| Advanced Sustainability Dashboard (Data Studio) | High     |

---

## 💚 Built with urgency, innovation, and a passion for sustainability.

