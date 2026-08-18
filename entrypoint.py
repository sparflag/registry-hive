#!/usr/bin/env python3
"""Registry Hive — real mini-challenge (registry-hive)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", 'run-key')


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    key = CHALLENGE_KEY or "reg-key"
    reg = f"""Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run]
"Updater"="{key}"
"""
    with open("/challenge/NTUSER.reg", "w") as f:
        f.write(reg)
    print("Registry Hive: Run value in NTUSER.reg is the key.")


if __name__ == "__main__":
    main()
