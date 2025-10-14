# ASN Information in SY.
# Last Updated: UTC 2025-10-14 00:59:23
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading SY ASN list"
/routing filter num-list
:do { add list=SY_ASN range=214707 } on-error={}
:do { add list=SY_ASN range=29386 } on-error={}
:do { add list=SY_ASN range=29256 } on-error={}
:do { add list=SY_ASN range=48065 } on-error={}
:do { add list=SY_ASN range=213812 } on-error={}
