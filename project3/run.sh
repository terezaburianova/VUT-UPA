#!/bin/bash

# Collect urls
python3.10 get_urls.py >> url_test.txt
# Get specification for first 10 URLs
python3.10 get_prods.py "url_test.txt" 10
