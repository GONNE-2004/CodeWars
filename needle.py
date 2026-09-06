def find_needle(haystack):
    for n in haystack:
        if n == "needle":
            return f"found the needle at position {haystack.index('needle')}"


haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# find_needle(haystack)