# ASN Information in KP.
# Last Updated: UTC 2026-04-15 01:48:57
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading KP ASN list"
/routing filter num-list
:do { add list=KP_ASN range=131279 } on-error={}
