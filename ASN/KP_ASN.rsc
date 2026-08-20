# ASN Information in KP.
# Last Updated: UTC 2026-08-20 00:44:58
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading KP ASN list"
/routing filter num-list
:do { add list=KP_ASN range=131279 } on-error={}
