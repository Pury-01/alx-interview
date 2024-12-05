# 0x03. Log Parsing

## Description
This project focuses on real-time log parsing using Python. The program reads log entries from standard input, extracts metrics, and computes statistics such as total file size and status code counts. These statistics are output after every 10 lines or upon a keyboard interrupt (CTRL + C).

---

## Learning Objectives
- How to read and process input streams in Python.
- Parsing structured data in real-time.
- Gracefully handling exceptions and signal interruptions.
- Aggregating data using dictionaries.
- Writing clean, PEP 8-compliant Python code.

---

## Requirements
- **Interpreter:** Python `3.4.3` running on **Ubuntu 20.04 LTS**.
- **Shebang:** `#!/usr/bin/python3` at the beginning of each file.
- **Code Style:** PEP 8 (checked using `pycodestyle 1.7.x`).
- **Executables:** All files must be executable.
- **Input Format:** 

---

## Input and Output Format

### Input
- **IP Address:** A valid IPv4 address.
- **Date:** Timestamp of the request.
- **HTTP Method:** `"GET /projects/260 HTTP/1.1"`.
- **Status Code:** One of `200, 301, 400, 401, 403, 404, 405, 500`.
- **File Size:** An integer.

### Output
Every 10 lines or on a keyboard interrupt:
