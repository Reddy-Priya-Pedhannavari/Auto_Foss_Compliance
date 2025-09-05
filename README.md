# Auto FOSS Compliance - Advanced Sample Repo

This repository includes:
- ~25 third-party source files under `third_party/*` with varied license headers (MIT, Apache-2.0, BSD, GPL, LGPL, MPL, Dual-licensed, and multi-historical headers)
- ~12 src files which call into specific third-party functions (so only used third-party files are linked/used)
- CMake build files to demonstrate static and shared linking of third-party code
- Compliance scripts in `compliance/` (validate_licenses.py, generate_notice.py, etc.) which will be used by CI to detect licenses
- Goal: In CI, run ScanCode and then match detected licenses only for files *used* in the build (by following the CMake linking) rather than every file in third_party/

## How to build locally (Linux)
mkdir build && cd build
cmake ..
make -j4
./app_main

## How to use for compliance scanning
- Run `scancode` from repo root to generate `reports/scancode.json`
- Use `compliance/validate_licenses.py` to check policy (this repo includes many license variations)
- The sample CMake demonstrates how src files depend on a subset of third_party files (libA_1, libB_1, etc.).
