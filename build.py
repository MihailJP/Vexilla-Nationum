#!/usr/local/bin/fontforge

import fontforge
Font = fontforge.open("VexillaNationum.sfd")
for Glyph in Font.glyphs():
	print Glyph.glyphname
	if Glyph.isWorthOutputting():
		for Contour in Glyph.foreground:
			if len(Contour) == 1:
				X = Contour[0].x; Y = Contour[0].y
				Radius = 18
				MagnPnct = fontforge.contour()
				MagnPnct += fontforge.point(X+Radius,Y+Radius,False)
				MagnPnct += fontforge.point(X+Radius,Y,True)
				MagnPnct += fontforge.point(X+Radius,Y-Radius,False)
				MagnPnct += fontforge.point(X+Radius,Y-Radius,False)
				MagnPnct += fontforge.point(X,Y-Radius,True)
				MagnPnct += fontforge.point(X-Radius,Y-Radius,False)
				MagnPnct += fontforge.point(X-Radius,Y-Radius,False)
				MagnPnct += fontforge.point(X-Radius,Y,True)
				MagnPnct += fontforge.point(X-Radius,Y+Radius,False)
				MagnPnct += fontforge.point(X-Radius,Y+Radius,False)
				MagnPnct += fontforge.point(X,Y+Radius,True)
				MagnPnct += fontforge.point(X+Radius,Y+Radius,False)
				MagnPnct.closed = True
				Glyph.foreground += MagnPnct
		Glyph.stroke("circular",24,"round","miter",())
Font.strokedfont = False
Font.generate("VexillaNationum.ttf")
