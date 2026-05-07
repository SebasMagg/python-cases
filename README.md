# Python Cases — Boot.dev Learning Journey

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-9.0.3-green?style=for-the-badge&logo=pytest&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![GitHub commits](https://img.shields.io/github/commit-activity/m/SebasMagg/python-cases?style=for-the-badge&logo=github)

> A structured collection of Python cases and exercises from the **Boot.dev** course — built with clean architecture, professional Git workflow, and pytest testing.

---

## About This Repository

This repository documents my Python learning journey through the **Boot.dev** course. Each case is a real coding exercise solved from scratch, refactored following professional Python standards, and tested using **pytest** with parametrized test cases.

The goal is not just to solve exercises — but to practice:
- Clean code structure and naming conventions
- Professional Git workflow (branches, pull requests, signed commits)
- Test-driven thinking with pytest
- Real-world project organization

---

## Project Structure

```
python-cases/
│
├── cases/                        # Core logic — pure Python functions
│   ├── case1.py                  # Calculate total XP
│   ├── case2.py                  # Unlock achievement system
│   ├── case3.py                  # Calculate damage
│   ├── case4.py                  # Binary string to int
│   ├── case5.py                  # Player health status
|   └── ...
│
├── tests/                        # Original test files (manual runner)
│   ├── Case1_tests.py
|   ├── Case2_tests.py
|   ├── Case3_tests.py
|   ├── Case4_tests.py
|   ├── Case5_tests.py
│   └── ...
│
├── pytest_practice/              # Professional pytest test suite
│   └── tests/
│       ├── test_case1.py         # Parametrized tests — total XP
│       ├── test_case2.py         # Parametrized tests — achievements
│       ├── test_case3.py         # Parametrized tests — calculate damage
│       ├── test_case4.py         # Parametrized tests — binary string to int
|       ├── test_case5.py
│       └── ...                   # Parametrized tests — player health
│
├── conftest.py                   # Pytest root configuration
├── .gitignore                    # Ignored files (pycache, venv, etc)
└── README.md                     # You are here
```

---

## Cases Overview

| # | File | Description | Concepts |
|---|------|-------------|----------|
| 1 | `case1.py` | Calculate total XP based on level and XP gained | Functions, arithmetic |
| 2 | `case2.py` | Unlock achievement system with XP reward | Functions, tuples, f-strings |
| 3 | `case3.py` | Calculate total and average damage across 5 weapon types | Functions, arithmetic operators, tuples, average calculation |
| 4 | `case4.py` | Convert binary strings to integers for servers, players and admins | Functions, tuples, type conversion, binary to integer (base 2) |
| 5 | `case5.py` | Player health status checker | if / elif / else, conditionals |

---

## Getting Started

### Prerequisites
- Python 3.10+
- pip or venv

### 1. Clone the repository
```bash
git clone git@github.com:SebasMagg/python-cases.git
cd python-cases
```

### 2. Create and activate virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install pytest
```

---

## Running Tests

### Run all tests at once
```bash
pytest pytest_practice/tests/ -v
```

### Run a specific case
```bash
pytest pytest_practice/tests/test_case1.py -v
```

### Run with short error detail
```bash
pytest pytest_practice/tests/ -v --tb=short
```

### Expected output
```
pytest_practice/tests/test_case1.py::test_total_xp[1-200-300]        PASSED
pytest_practice/tests/test_case1.py::test_total_xp[2-50-250]         PASSED
pytest_practice/tests/test_case1.py::test_total_xp[0-0-0]            PASSED
pytest_practice/tests/test_case2.py::test_unlock_achievement[...]    PASSED
pytest_practice/tests/test_case5.py::test_player_health[...]         PASSED
```

---

## Testing Architecture

Tests are written using **pytest** with `@pytest.mark.parametrize` — the professional standard for Python testing used in major frameworks like Django, Flask and FastAPI.

```python
@pytest.mark.parametrize("level, xp, expected", [
    (1, 200, 300),
    (2, 50,  250),
    (0, 0,   0  ),
])
def test_total_xp(level, xp, expected):
    assert total_xp(level, xp) == expected
```

**Why parametrize?**
- Each test case runs and reports **individually**
- Adding new cases = one line in the list
- Zero code duplication
- Clean, readable output

---

## Git Workflow

This project follows a professional Git branching strategy:

```
main (protected)
 │
 ├── feature/case5-player-health-status   ← new features
 ├── fix/case1-edge-cases                 ← bug fixes
 └── refactor/split-cases-and-tests       ← code improvements
```

- Every change goes through a **Pull Request**
- All commits are **GPG signed** (Verified ✅ badge on GitHub)
- Branches are deleted after merging — clean history

---

## Progress

- [x] Case 1 — Calculate total XP
- [x] Case 2 — Unlock achievement system
- [x] Case 3 — Calculate damage
- [x] Case 4 — Binary string to int
- [x] Case 5 — Player health status
- [x] Refactor — Split cases and tests into separate folders
- [x] Pytest — Parametrized test suite for all cases
- [ ] Case 6 — Coming soon
- [ ] CI/CD — GitHub Actions to run tests automatically on push

---

## Author

**Sebastian Ernesto Magaña Ramirez**
- Product Owner | Project Manager | Scrum Master | QA Tester
- Python | Vercel | Docker | n8n | Supabase
- GitHub: [@SebasMagg](https://github.com/SebasMagg)
- LinkedIn: [linkedin.com/in/sebastianmagg](https://linkedin.com/in/sebastianmagg)
- sebastianramirez.99@gmail.com

---

## Learning Resources

- [Boot.dev](https://www.boot.dev) — The course driving this repository
- [pytest docs](https://docs.pytest.org) — Official pytest documentation
- [PEP 8](https://pep8.org) — Python style guide followed in this project

---

## License

This project is licensed under the MIT License — feel free to use it as a reference for your own learning journey.

---

<p align="center">
  <i>Built with 👾 while learning Python the right way.</i>
</p>
