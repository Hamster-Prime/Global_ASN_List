# ASN Information in KP.
# Last Updated: UTC 2025-12-15 01:08:05
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading KP ASN list"
/routing filter num-list
:do { add list=KP_ASN range=131279 } on-error={}
