#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import sys
from xml.sax.saxutils import escape


def main():
    usage = """
    usage: csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html

    maxwidth is an optional integer; if specified, configures the max number of characters
    that can be inserted in the string field, otherwise, the default is 100

    format is the formatation used for numbers; if not specified, the default is ".0f"
    """

    if process_options() == (None, None):
        print(usage)
        sys.exit()

    else:
        maxwidth, _format = process_options()
        print_start()
        print(maxwidth, _format)
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, _format)
                count += 1
            except EOFError:
                break
        print_end()

def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth, formatting):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    number_format = "<td align='right'>{{0:{0}}}</td>".format(formatting)

    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(number_format.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = escape_html(field)
                else:
                    field = "{0} ...".format(
                            escape_html(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def escape_html(text):
    escape(text)
    return text


def print_end():
    print("</table>")

def process_options(maxwidth=100, _format=".0f"):
    maxwidth_arg = "maxwidth="
    format_arg = "format="

    if len(sys.argv) > 1:
        try:
            if ["-h", "--help"] in sys.argv:
                print(    
            """
            usage: csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html

            maxwidth is an optional integer; if specified, configures the max number of characters
            that can be inserted in the string field, otherwise, the default is 100

            format is the formatation used for numbers; if not specified, the default is ".0f"
            """
            )
                return (None, None)
            
            elif all([len(sys.argv) >= 2 and sys.argv[1].startswith(maxwidth_arg),
                    len(sys.argv) >= 2 and sys.argv[2].startswith(format_arg)]):

                maxwidth = int(sys.argv[1][len(maxwidth_arg):])
                _format = str(sys.argv[2][len(format_arg):])
        
                return (maxwidth, _format)
        except IndexError:

            return (None, None)
 
    else:
        return (maxwidth, _format)

if __name__ == "__main__":
    main()

