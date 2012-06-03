# -*- coding: utf_8 -*-

#    Copyright (C) 2012  Olaf Radicke
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


class HtmlTemplate:
    
    def top(self, aktivtab):
        top =     u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"'
        top +=    '       "http://www.w3.org/TR/html4/loose.dtd">'
        top +=    '  <head>'
        top +=    '    <meta http-equiv="content-type" content="text/html; charset=utf-8">'
        top +=    '  <head>'
        top +=    '<html>'
        top +=     u'<link rel="stylesheet" href="static/home.css" type="text/css" media="screen" charset="utf-8"/>'
        top +=    '<div class="all">'
        #top +=    '    <div class="line" ></div>'
        top +=    '    <div class="bannerbox" >'
        top +=    u'        <h1>Mit was deckt sich dein Glaube?</h1>'
        top +=    '        <h3><i>BELIEF MATCHING</i> (beta)</h3>'
        #top +=    '        <img src="static/image.jpg" >'
        top +=    '    </div>'
        top +=    '    <div class="line" ></div>'
        top +=    '    <div class="mainmenue" >'
        top +=    '           <ul id="portal-globalnav">'
        if ( aktivtab == "home"):
            top +=    '            <li id="tableft_activ"><a href="/">Start</a></li>'
        else:
            top +=    '            <li id="tableft" ><a href="/">Start</a></li>'
        if ( aktivtab == "test"):
            top +=    '            <li id="tabmiddle_activ"><a href="test">Test</a></li>'
        else:
            top +=    '            <li id="tabmiddle"><a href="test">Test</a></li>'
        if ( aktivtab == "datenbasis"):
            top +=    '            <li id="tabright_activ"><a href="datenbasis">Datenbasis</a></li>'
        else:
            top +=    '            <li id="tabright"><a href="datenbasis">Datenbasis</a></li>'
        top +=    '           </ul>'
        top +=    '        </div>'
        top +=    '    <div class="line" ></div>'
        top +=    '    <div class="appbox">'  
        return top
    
    bottom =  '    </div>'
    bottom += '    <div class="footer">'
    bottom += 'BELIEF MATCHING | <a href="https://github.com/OlafRadicke/belief-matching">'
    bottom += 'Auf GitHub</a> | <a href="mailto:briefkasten@olaf-radicke.de">'
    bottom += 'briefkasten@olaf-radicke.de</a>'
    bottom += '    <div>'
    bottom += '<div></body></html>'