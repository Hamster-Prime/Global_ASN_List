# ASN Information in YE.
# Last Updated: UTC 2025-12-16 01:07:45
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading YE ASN list"
/routing filter num-list
:do { add list=YE_ASN range=12486 } on-error={}
:do { add list=YE_ASN range=30873 } on-error={}
:do { add list=YE_ASN range=204317 } on-error={}
