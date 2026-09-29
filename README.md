# Authentication & Authorization Concepts

A simple Python challenge that maps fundamental cybersecurity concepts to their correct definitions.

Completed as part of the **Santander Bootcamp** on [DIO](https://www.dio.me/).

## Overview

In cybersecurity, understanding authentication and authorization is essential to protect data and control access to systems. This program receives the name of a concept as input and returns its matching definition.

## Supported Concepts

| Input (Concept) | Output (Definition) |
|---|---|
| Authentication | Verification of a user's identity |
| Authorization | Permission to access specific resources |
| MFA | Verification using multiple security factors |
| OAuth | Open standard for delegating access without sharing a password |

## How It Works

The program reads a concept name from standard input and passes it to a function that returns the corresponding definition using conditional logic (`if` / `elif`).

## Usage

```bash
python main.py
```

Example:

```text
Input:  MFA
Output: Verification using multiple security factors
```

## Test Results

All 3 open test cases passed on the DIO platform.

| Test | Input | Expected Output | Result |
|---|---|---|---|
| #1 | Authentication | Verification of a user's identity | Passed |
| #2 | Authorization | Permission to access specific resources | Passed |
| #3 | MFA | Verification using multiple security factors | Passed |

## Key Concepts

- **Authentication (AuthN):** proves *who you are* (e.g., password, biometrics).
- **Authorization (AuthZ):** defines *what you can do* after being authenticated.
- **MFA (Multi-Factor Authentication):** combines two or more factors: something you know, something you have, something you are.
- **OAuth:** an open standard that lets an app access resources on your behalf without ever seeing your password.

## Screenshots

![Challenge description](challenge-description.png)
![All open tests passed](test-1-2.png)

## Tech Stack

- Python 3

## Author

**Nicolas Borges Ocampos**
Cybersecurity student | Aspiring SOC / Blue Team analyst
[LinkedIn](https://www.linkedin.com/in/nicolas-borges-ocampos/)
