# ASN Information in HT.
# Last Updated: UTC 2025-10-14 01:00:10
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading HT ASN list"
/routing filter num-list
:do { add list=HT_ASN range=27653 } on-error={}
:do { add list=HT_ASN range=52260 } on-error={}
:do { add list=HT_ASN range=27759 } on-error={}
:do { add list=HT_ASN range=263685 } on-error={}
:do { add list=HT_ASN range=271897 } on-error={}
:do { add list=HT_ASN range=52382 } on-error={}
