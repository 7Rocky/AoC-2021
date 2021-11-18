test:
	@for d in $(shell ls -d ${PWD}/*/); do \
		cd $${d} && echo '\nTesting:' && pwd && python3 -m unittest main_test.py; \
	done

.PHONY: test
