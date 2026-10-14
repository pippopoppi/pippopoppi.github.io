#!/usr/bin/env python3
"""Render og.png (1200x630) and icon-180.png for the Pippo Poppi Games hub with Pillow only."""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..')
def font(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return ImageFont.load_default()
BG=(11,16,32); INK=(241,245,249); MUTED=(148,163,184); AMBER=(251,191,36); GREEN=(34,197,94); PANEL=(20,26,46); LINE=(38,48,82)
W,H=1200,630
img=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(img)
d.text((70,120),'PIPPO POPPI',font=font(88),fill=INK)
d.text((70,222),'GAMES',font=font(104),fill=AMBER)
d.text((72,360),'Otto giochi gratis nel browser.',font=font(34),fill=MUTED)
d.text((72,404),'Niente da installare: tocca e gioca.',font=font(34),fill=MUTED)
names=['Math Survival','Coccodrillo vs Piccione','Racism 2','Slotcars Simulator','Void Vanguard','Steel Command','Crowd Cannon','Crowd Cannon: Lanes']
x0,y0=760,70
for i,n in enumerate(names):
    y=y0+i*62
    d.rounded_rectangle([x0,y,x0+370,y+50],radius=12,fill=PANEL,outline=LINE,width=2)
    d.ellipse([x0+14,y+15,x0+34,y+35],fill=GREEN)
    d.text((x0+48,y+25),n,font=font(20),fill=INK,anchor='lm')
d.text((72,586),'pippopoppi.github.io  -  Pippo Poppi Games',font=font(22),fill=MUTED)
img.save(os.path.join(OUT,'og.png'),optimize=True)
ic=Image.new('RGB',(180,180),BG); dd=ImageDraw.Draw(ic)
dd.text((90,78),'PP',font=font(74),fill=INK,anchor='mm')
dd.rounded_rectangle([40,120,140,134],radius=7,fill=AMBER)
dd.text((90,156),'GAMES',font=font(22),fill=MUTED,anchor='mm')
ic.save(os.path.join(OUT,'icon-180.png'),optimize=True)
print('ok')
