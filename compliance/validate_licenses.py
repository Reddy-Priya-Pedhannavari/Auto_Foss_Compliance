#!/usr/bin/env python3
import json, sys

def main():
    if len(sys.argv) < 3:
        print("Usage: validate_licenses.py <scancode_json> <allowlist_json>")
        sys.exit(2)

    scancode_json, allowlist_json = sys.argv[1], sys.argv[2]
    with open(scancode_json, 'r', encoding='utf-8') as f:
        scan = json.load(f)
    with open(allowlist_json, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    allowed = set(cfg.get("allowed_spdx_ids", []))
    denied = set(cfg.get("denied_spdx_ids", []))
    problems = []
    found = set()

    for f in scan.get("files", []):
        for lic in f.get("licenses", []):
            spdx = lic.get("spdx_license_key") or lic.get("license_expression") or ""
            spdx = str(spdx).strip()
            if not spdx:
                continue
            tokens = [t.strip() for t in spdx.replace("(", " ").replace(")", " ").replace("OR", " ").replace("AND"," ").replace("WITH"," ").split() if t]
            for t in tokens:
                found.add(t)
                if t in denied:
                    problems.append(f"Denied license {t} in {f.get('path')}")
                elif allowed and t not in allowed:
                    problems.append(f"Unapproved license {t} in {f.get('path')}")

    print("Detected SPDX IDs:", ", ".join(sorted(found)) or "None")
    if problems:
        print("❌ License validation failed:")
        for p in problems:
            print(" -", p)
        sys.exit(1)
    else:
        print("✅ License validation passed (allowlist).")
        sys.exit(0)

if __name__ == "__main__":
    main()
