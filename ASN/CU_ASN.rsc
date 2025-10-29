# ASN Information in CU.
# Last Updated: UTC 2025-10-29 01:06:55
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading CU ASN list"
/routing filter num-list
:do { add list=CU_ASN range=11960 } on-error={}
:do { add list=CU_ASN range=27725 } on-error={}
:do { add list=CU_ASN range=10569 } on-error={}
