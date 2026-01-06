# ASN Information in SY.
# Last Updated: UTC 2026-01-06 01:09:43
# Made by ASN Fetcher Script, All rights reserved.

/log info "Loading SY ASN list"
/routing filter num-list
:do { add list=SY_ASN range=214707 } on-error={}
:do { add list=SY_ASN range=29386 } on-error={}
:do { add list=SY_ASN range=216472 } on-error={}
:do { add list=SY_ASN range=29256 } on-error={}
:do { add list=SY_ASN range=48065 } on-error={}
:do { add list=SY_ASN range=213812 } on-error={}
