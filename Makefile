all:

init-sumatra: .smt

.smt:
	smt init SumatraBug
	smt configure -e python -m main.py --addlabel=parameters --on-changed=store-diff

run:
	smt run -r "Create a Sumatra record." defaults.param


purge:
	rm -rf .smt/ Data/

.PHONY: all init-sumatra run purge
