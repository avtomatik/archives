# Archives - Archive File Processing

`archives` is a Python project for processing and repacking archive files, specifically designed for handling `.rar` and `.zip` formats. This tool allows users to extract, modify, and organize archive contents in a simple and efficient way.

## Requirements

This project requires **Python 3.11 or higher**.

### Dependencies
- **black**: Code formatter, using PEP 8 standards with a line length of 79 characters.
- **pytest**: A testing framework for unit tests and other test types.
- **mypy**: A static type checker for Python, to ensure code type correctness.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/avtomatik/archives.git
cd archives
````

### 2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install the dependencies:

```bash
pip install .
```

This will install the project along with mandatory dependencies: `black`, `pytest`, and `mypy`.

## Usage

### Code Formatting (black)

To automatically format your code according to the PEP 8 style guide with a maximum line length of 79 characters, run:

```bash
black .
```

### Running Tests (pytest)

Run the test suite using `pytest`:

```bash
pytest
```

### Type Checking (mypy)

Ensure that your code is type-checked:

```bash
mypy src/archives
```

## Project Structure

```
archives/
│
├── src/
│   └── archives/               # Main package
│
├── tests/                      # Unit tests
│
├── .venv/                      # Virtual environment (not included in version control)
├── pyproject.toml              # Project metadata and dependencies
└── README.md                   # Project documentation
```

## License

MIT License. See the [LICENSE](LICENSE) file for more details.

---
