'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2015 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2011-2015 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: prepil.py - Last Update: 1/15/2015 Ver. 2.7.10 RC 1  - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
from PIL import Image, ImageDraw, ImageFont;
import upcean.fonts;

try:
 import pkg_resources;
 pkgres = True;
except ImportError:
 pkgres = False;

fontpathocra = upcean.fonts.fontpathocra;
fontpathocraalt = upcean.fonts.fontpathocraalt;
fontpathocrb = upcean.fonts.fontpathocrb;
fontpathocrbalt = upcean.fonts.fontpathocrbalt;
fontpath = upcean.fonts.fontpath;

''' // Source: http://stevehanov.ca/blog/index.php?id=28 '''
def snapCoords( ctx, x, y ):
 (xd, yd) = ctx.user_to_device(x, y);
 return ( round(x) + 0.5, round(y) + 0.5 );

def drawColorLine( ctx, x1, y1, x2, y2, color ):
 ctx.line((x1, y1, x2, y2), fill=color);

def drawColorRectangle( ctx, x1, y1, x2, y2, color ):
 ctx.rectangle([(x1, y1), (x2, y2)], fill=color);

def drawColorText( ctx, size, x, y, text, color, ftype = "ocrb" ):
 if(ftype=="ocra"):
  font = ImageFont.truetype(fontpathocra, size);
 if(ftype=="ocrb"):
  font = ImageFont.truetype(fontpathocrb, size);
 text = str(text);
 ctx.text((x, y), text, font=font, fill=color);
 del(font);

def drawColorRectangleAlt( ctx, x1, y1, x2, y2, color ):
 ctx.rectangle([(x1, y1), (x2, y2)], outline=color);
