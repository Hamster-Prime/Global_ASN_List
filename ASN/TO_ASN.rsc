# ASN Information in TO.
# Last Updated: UTC 2025-10-21 01:02:17
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading TO ASN list"
/routing filter num-list
:do { add list=TO_ASN range=132579 } on-error={}
:do { add list=TO_ASN range=132831 } on-error={}
:do { add list=TO_ASN range=38201 } on-error={}
:do { add list=TO_ASN range=38198 } on-error={}
