# 0x06. Star Wars API

## Table of Contents
- [Description](#description)
- [Concepts](#concepts)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Author](#author)

---

## Description

This project involves fetching and displaying Star Wars characters using the Star Wars API based on a movie ID provided as an argument. The characters are displayed in the same order as listed in the `characters` array from the `/films/` endpoint.

---

## Concepts

### HTTP Requests in JavaScript
- Learn how to make HTTP requests using the `request` module or other alternatives like `fetch`.
- Parsing JSON responses from APIs.

### Working with APIs
- Understand RESTful APIs and how to interact with them using HTTP methods.

### Asynchronous Programming
- Use callbacks, promises, or `async/await` syntax for managing asynchronous operations.

### Command Line Arguments in Node.js
- Parse arguments passed to a script using `process.argv`.

### Array Manipulation and Iteration
- Use JavaScript array methods to manipulate and format data.

---

## Requirements

- **Editor**: `vi`, `vim`, `emacs`
- Files are interpreted on Ubuntu 20.04 LTS using Node.js (version 10.14.x).
- Code must follow `semistandard` style guidelines with semicolons.
- Files must be executable and end with a newline.
- First line of each file: `#!/usr/bin/node`
- No use of `var` (use `let` or `const`).

---

## Installation

### Install Node.js (version 10)
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
