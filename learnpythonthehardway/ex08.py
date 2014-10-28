# -*- coding: utf-8 -*-

# define formatter with four %r, to match four strings or numbers or whatever.
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

formatter_chinese = "%s %s %s %s"
# There will be wrong word,why?
# how can i print chinese?
print formatter_chinese % ("学", "习", "派", "森")