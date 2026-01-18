# ASN Information in WS.
# Last Updated: UTC 2026-01-18 01:15:52
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading WS ASN list"
/routing filter num-list
:do { add list=WS_ASN range=17993 } on-error={}
:do { add list=WS_ASN range=153053 } on-error={}
:do { add list=WS_ASN range=38800 } on-error={}
:do { add list=WS_ASN range=38227 } on-error={}
:do { add list=WS_ASN range=150321 } on-error={}
:do { add list=WS_ASN range=139679 } on-error={}
