#!/usr/bin/env python3
"""Canonical clinical content for Marva Lydell.

All values here are placeholders until Phase A substrate ratification.
Do not build uploadable artifacts while any `<<PHYSICIAN: ...>>` marker remains.
"""

PT = dict(
    name="<<PHYSICIAN: patient name>>",
    sex="<<PHYSICIAN: sex>>",
    dob="<<PHYSICIAN: DOB>>",
    age="<<PHYSICIAN: age>>",
    mrn="<<PHYSICIAN: synthetic MRN>>",
    allergies="<<PHYSICIAN: allergies>>",
    code="<<PHYSICIAN: code status>>",
    language="<<PHYSICIAN: language>>",
    insurance="<<PHYSICIAN: insurance>>",
)

FACILITY = "<<PHYSICIAN: synthetic facility name>>"
ENC = dict(
    csn="<<PHYSICIAN: synthetic CSN>>",
    fin="<<PHYSICIAN: synthetic FIN>>",
    unit="<<PHYSICIAN: unit>>",
    room="<<PHYSICIAN: room>>",
    admit="<<PHYSICIAN: admit date>>",
    service="Hospital Medicine",
)

ROSTER = dict(attending="<<PHYSICIAN: attending physician>>")
DERIVED = []


def encounter_pairs(dos):
    return [
        ("Patient", PT["name"]),
        ("Sex / DOB", f"{PT['sex']} / {PT['dob']}"),
        ("MRN / FIN", f"{PT['mrn']} / {ENC['fin']}"),
        ("Unit / Room", f"{ENC['unit']} / {ENC['room']}"),
        ("Code Status", PT["code"]),
        ("Allergies", PT["allergies"]),
        ("Attending", ROSTER["attending"]),
        ("Service", ENC["service"]),
        ("Date of Service", dos),
        ("Language", PT["language"]),
    ]


# Each spec returns (filename, base_key, note_type, date_of_service, blocks).
WORLD_FILES = []
SUPPLEMENTARY = []
