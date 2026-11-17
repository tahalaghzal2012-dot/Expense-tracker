# CLI Expense Tracker & AI Financial Auditor

A modular, terminal-based personal expense tracker built in Python, featuring NumPy spending analytics, a styled `Rich` CLI interface, and a local AI financial auditor powered by Ollama (`llama3.2`).

---

## Features

- **Expense Management:** Add, search, and delete expenses categorized by type with automatic timestamps and auto-incrementing IDs.
- **Persistent JSON Storage:** Safe, fault-tolerant local storage (`data.json`) with built-in error handling for missing, corrupted, or locked files.
- **NumPy Spending Analytics:** Instantly calculate total spending, average expense amount, minimum expense, and maximum expense.
- **Ruthless AI Financial Auditor:** Connects to a local Ollama LLM instance (`llama3.2:latest`) via REST API to audit your exact spending history and deliver blunt, actionable financial recommendations.
- **Rich Terminal UI:** Clean, color-coded menus and panels powered by the `rich` library.

---

## Project Structure

```text
expense_tracker/
├── main.py          # Entry point, Rich CLI menu, search, delete, and NumPy stats
├── models.py        # ExpenseTracker input handling and AI payload formatting
├── storage.py       # StorageManager class for fault-tolerant JSON persistence
├── advisor.py       # Local Ollama API integration and system prompt auditor logic
└── data.json        # Auto-generated local expense database (ignored in Git)
```

---

## Prerequisites

1. **Python 3.10+**
2. **Ollama** installed and running locally on `http://localhost:11434` with the `llama3.2` model pulled:
   ```bash
   ollama pull llama3.2
   ```

---

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tahalaghzal2012-dot/Expense-tracker.git
   cd Expense-tracker
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   # Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install rich numpy requests
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

---

## Example AI Auditor Output

```text
AUDIT:
- Unnecessary expenditure: 129 MAD spent on "wireless keyboard and mouse" under "technologie".
- Lack of budget allocation across non-essential hardware purchases.

RECOMMENDATIONS:
- Freeze all non-essential technology spending for the next 30 days.
- Establish a strict monthly discretionary spending cap before making further purchases.
```
