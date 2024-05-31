all:
	make -C subtask1 all
	make -C subtask2 all
	make -C subtask3 all

clean:
	make -C subtask1 clean
	make -C subtask2 clean
	make -C subtask3 clean


check:
	make -C subtask1 test
	make -C subtask2 test
	make -C subtask3 test

.PHONY: all clean check
