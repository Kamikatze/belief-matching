
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

import sys
import sqlite3
import web
from web import form

import HtmlTemplate
import index
import belieftest
import databaseview
import participate
import sqlgenerator
import databaseedit

urls = (
  '/', 'index.index',
  '/belieftest', 'belieftest.belieftest',
  '/databaseview','databaseview.databaseview',
  '/databaseedit','databaseedit.databaseedit',
  '/participate','participate.participate',
  '/sqlgenerator','sqlgenerator.sqlgenerator')


app = web.application(urls, globals())#, web.reloader)


htemp = HtmlTemplate.HtmlTemplate()
         


if __name__ == "__main__":
    app.run()
