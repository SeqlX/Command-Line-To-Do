# 📝 Command-Line To-Do List (Python)

A simple yet functional command-line task manager built in Python.  


---

## 🚀 Features

- ✅ Add new tasks via terminal
- ✅ View numbered task list every session
- ✅ Mark tasks as `[COMPLETED]`
- ✅ Color-coded display using `colorama`
- ✅ Persistent file storage via `todo_list.txt`
- ✅ Robust loop-based menu system (Add / Complete / Quit)

---

## 🧠 Concepts Demonstrated

This project puts into practice all of the following core Python skills:

| Python Concept          | Used in...                     |
|------------------------|--------------------------------|
| Variables              | Storing user input & tasks     |
| Conditionals (`if`)    | Menu logic, task status checks |
| Loops (`for`, `while`) | File reading, task menu loop   |
| Functions              | Modular, reusable task actions |
| Lists                  | Task storage and indexing      |
| File I/O               | Reading/writing `.txt` files   |
| String Methods         | `.strip()`, formatting tags    |
| External Libraries     | `colorama` for terminal colors |

---

## 🖥️ How It Works

1. On running the script, the user sees their current tasks listed with numbers.
2. The user chooses an action:
   - **Add** a new task
   - **Mark** a task as completed
   - **Quit** the program
3. Completed tasks are labeled `[COMPLETED]` and displayed in green.
4. All changes are saved to `todo_list.txt`.

---

## 📂 File Structure

```
📁 project/
├── __main__.py           # Main Python script
├── todo_list.txt         # Persistent task storage
└── README.md             # This file
```

---

## 🛠️ Requirements

- Python 3.x
- `colorama` package  
  Install with:
  ```bash
  pip install colorama
  ```

---

## 📌 Future Ideas (Optional Upgrades)

- Delete a task by number
- Archive completed tasks to a separate file
- Sort tasks by completion status
- Add due dates or priority levels
- Export task list to CSV

---

## 📚 Author & Purpose

This project was created by **"CallMe_Ghost" AKA "Seql" AKA "Killabyte"** as a portfolio piece and personal learning milestone to:
- Demonstrate Python fundamentals
- Practice clean, modular coding
- Create a practical tool with real-world value

---

## ✅ Status

**✅ Project Complete** — Fully functional, well-commented, and extensible.

---
