Enriched module payloads (optional)
===================================
Add one JSON file per module: modules/mNNN.json where NNN is the 3-digit module number (e.g. m007.json for "Module 7" in the blueprint).

Required key: module_num (integer, same as blueprint module #).

Optional keys: learn, steps, code, refs (strings — HTML allowed in learn/steps/refs), content_tier ("full" | "partial" | "scaffold"), blueprint_ref, coverage_notes.

After editing: run `python3 build_curriculum.py` then `python3 assemble_platform.py`.

The tracker CSV is regenerated at data/topics_coverage.csv (self_contained_on_page = yes | partial | no).
