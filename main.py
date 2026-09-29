"""
Authentication & Authorization Concepts
Santander Bootcamp x DIO - Python challenge

Reads a cybersecurity concept name from input and prints its definition.
"""

concept_input = input().strip()


def describe_concept(concept):
    if concept == "Authentication":
        return "Verification of a user's identity"

    elif concept == "Authorization":
        return "Permission to access specific resources"

    elif concept == "MFA":
        return "Verification using multiple security factors"

    elif concept == "OAuth":
        return "Open standard for delegating access without sharing a password"


print(describe_concept(concept_input))
