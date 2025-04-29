# Basin Threshold Tool: academic literature mining workflow
*Science-based targets for Nature: Freshwater*

This repository contains the code base for mining the academic literature supporting the Basin Threshold Tool. The Basin Threshold Tool is a global data repository of local-level surface water and groundwater quantity and quality data, environmental flow (e-flow) knowledge, and associated models, methods, and tools, designed in alignment with global frameworks for protecting freshwater biodiversity. This repository focuses specifically, in its initial phase, on mining _academic_ literature on environmental flows assessments. The desired output is a database of e-flows estimates for specific hydrologic basins for use by companies to set targets. Therefore, the search protocol is designed to be applied to specific river basins, starting with the smallest scale and broadening the focus to include all relevant information in the larger basin and administrative areas, if needed. That said, the objective of this protocol and to eventually be applicable to the global scale, such that its applications to hundreds of basins should be tractable, even if requiring extensive work.

Programming language: Python, using Jupyter Notebook in Jupyter Lab
Bibliographic management software: [Zotero](https://www.zotero.org/download/) 

# Workflow
- **src/active/set_up.py**  
Sets up project directory paths. A key dependency for almost all scripts.
  
- **src/active/lit_utility_functions_2025.ipynb**  
Contains multiple utility functions but does not depend on other scripts.
Used by many other scripts for regex operations, file handling, and Zotero API integration.
  
- **src/active/create_search_strings.ipynb**  
_Calls lit_utility_functions_2025.ipynb_  
Constructs search strings based on keywords. This script is used as a foundation for generating queries in other parts of the workflow.  

- **src/active/download_geographic_refs.ipynb**  
_Calls set_up.py_  
Downloads the Global Administrative Areas (GADM), National Hydrography Dataset Plus (NHDPlus), and HydroATLAS (BasinATLAS and RiverATLAS) datasets. Includes functions to download and extract zip files from URLs, and for downloading data from Amazon S3 cloud storage.  

- **src/active/get_target_toponyms.ipynb**  
_Calls set_up.py, download_geographic_refs.ipynb_  
_Requires output from download_geographic_refs.ipynb_  
Retrieve a list of toponyms (NHD hydrologic unit names, river names from NHD and administrative unit names) associated with all coordinates in an input table or with an input vector dataset (points, lines or polygons).  

- **src/active/create_location_filter_string.ipynb**  
_Calls lit_utility_functions_2025.ipynb, get_target_toponyms.ipynb_  
Generates location-based filter strings for narrowing down search results based on pre-retrieved toponyms: basin, river and administrative unit names. Writes toponym set to pickle  

- **src/active/create_api_call.ipynb**  
_Calls set_up.py, lit_utility_functions_2025.ipynb, create_search_strings.ipynb_  
_Requires output from create_location_filter_string.ipynb_  
Create and run API calls for OpenAlex. It integrates search strings and sets up parameters for interfacing with OpenAlex and Zotero APIs, then make the literature search calls in OpenAlex, filter the results and deduplicate them across searches.  

- **src/active/assess_search_match_with_testlist.ipynb**  
_Calls set_up.py, lit_utility_functions_2025.ipynb_  
This script evaluates the relevance of search results by comparing them with a predefined test list. It benchmarks the usefulness of search strings or filtering criteria for target datasets.  

- **src/active/download_ancillary_q_data.ipynb**  
_Calls set_up.py_  
Downloads ancillary hydrological datasets required for analysis: USGS discharge data using daily values (dv)

- **src/active/retrieve_fulltexts.ipynb**  
_Calls set_up.py, lit_utility_functions_2025.ipynb_  
Unfinished: Downloads full-text articles and metadata for records. Processes RIS files and integrates with OpenAlex datasets to enrich the bibliographic data.  


# Scripts not used (yet)
- **src/active/get_ngrams_from_searchlist.ipynb**
Extracts and analyzes n-grams (word sequences) from a list of search results. This script is useful for identifying patterns or trends in text data.

- **src/active/download_osm.ipynb**  
_Calls set_up.py, filter_records_by_location.ipynb_  
Downloads and processes OSM waterway data using pyrosm, filters for rivers and streams, and optionally subsets it with a polygon GeoDataFrame.  

- **src/active/wos_scoping_4_assess_search_relevance.ipynb**  
_Calls lit_utility_functions_2025.ipynb, set_up.py_
Processes and compiles references from Web of Science (WoS) search results. Evaluates the inclusion and exclusion of references based on predefined categories and generates summary statistics for search relevance.

- **src/active/scholarly_2022.ipynb**  
Uses scholarly and ProxyGenerator to retrieve publications from Google Scholar