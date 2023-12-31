.PHONY: create-dir

create-dir:
	@read -p "Enter day number: " day; \
	mkdir -p day$$day; \
	touch day$$day/$$day.py day$$day/input.txt day$$day/test.txt
