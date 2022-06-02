generate_icons:
	@mkdir -p images/case_icons
	@rm -rf images/case_icons/...
	@python -B icons.py