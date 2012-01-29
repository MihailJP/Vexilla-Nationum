#!/usr/local/bin/fontforge

import fontforge
Font = fontforge.open("VexillaNationum.sfd")
for Glyph in Font.glyphs():
	if Glyph.isWorthOutputting():
		Glyph.stroke("circular",24,"round","miter",())
Font.strokedfont = False
Font.generate("VexillaNationum.ttf")
