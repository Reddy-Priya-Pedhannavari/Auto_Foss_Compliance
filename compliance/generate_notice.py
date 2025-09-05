#!/usr/bin/env python3
import json, sys
from collections import defaultdict

def main():
    if len(sys.argv) < 3:
        print("Usage: generate_notice.py <scancode_json> <output_notice_path>")
        sys.exit(2)

    scancode_json, out_path = sys.argv[1], sys.argv[2]
    with open(scancode_json, 'r', encoding='utf-8') as f:
        data = json.load(f)

    by_license = defaultdict(list)
    for f in data.get("files", []):
        path = f.get("path")
        for lic in f.get("licenses", []):
            spdx = lic.get("spdx_license_key") or lic.get("license_expression") or "UNKNOWN"
            by_license[spdx].append(path)

    with open(out_path, "w", encoding="utf-8") as out:
        out.write("NOTICE\nGenerated from ScanCode results\n\n")
        for spdx, files in sorted(by_license.items()):
            out.write(f"License: {spdx}\n")
            for p in files[:20]:
                out.write(f"  - {p}\n")
            if len(files) > 20:
                out.write(f"  ... and {len(files)-20} more files\n")
            out.write("\n")
    print(f"NOTICE generated at {out_path}")

if __name__ == "__main__":
    main()
