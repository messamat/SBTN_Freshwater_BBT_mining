
## Dependency among scripts

- src/active/assess_search_match_with_testlist.ipynb
        Calls set_up.py
        Calls lit_utility_functions_2025.ipynb

- src/active/create_api_call.ipynb
        Calls set_up.py
        Calls lit_utility_functions_2025.ipynb
        Calls create_search_strings.ipynb

- src/active/create_location_filter_string.ipynb
        Calls get_target_toponyms.ipynb
        Calls lit_utility_functions_2025.ipynb

- src/active/create_search_strings.ipynb
        Calls lit_utility_functions_2025.ipynb

- src/active/download_ancillary_q_data.ipynb
        Calls set_up.py

- src/active/download_geographic_refs.ipynb
        Calls set_up.py

- src/active/get_ngrams_from_searchlist.ipynb
        No external dependencies identified.

- src/active/get_target_toponyms.ipynb
        Calls download_geographic_refs.ipynb
        Calls set_up.py

- src/active/download_osm.ipynb
        Calls set_up.py
        Calls filter_records_by_location.ipynb

- src/active/lit_utility_functions_2025.ipynb
        Contains multiple utility functions but does not depend on other scripts.
        Used by many other scripts for regex operations, file handling, and Zotero API integration.

- src/active/retrieve_fulltexts.ipynb
        Calls set_up.py
        Calls lit_utility_functions_2025.ipynb

- src/active/scholarly_2022.ipynb
        Uses scholarly and ProxyGenerator for scholarly publications.
        No direct dependency on other scripts in this directory.

- src/active/set_up.py
        Sets up project directory paths.
        A key dependency for almost all scripts.

- src/active/wos_scoping_4_assess_search_relevance.ipynb
        Calls lit_utility_functions_2025.ipynb
        Calls set_up.py
