# ***************************************************************************
# *   Copyright (c) 2021 Bernd Hahnebach <bernd@bimstatik.org>              *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

__title__ = "FreeCAD FEM calculix constraint sectionprint"
__author__ = "Bernd Hahnebach"
__url__ = "https://www.freecadweb.org"


def write_surfacefaces_constraints_sectionprint(f, femobj, sectionprint_obj, ccxwriter):
    f.write("*SURFACE, NAME=SECTIONFACE{}\n".format(sectionprint_obj.Name))
    for i in femobj["SectionPrintFaces"]:
        f.write("{},S{}\n".format(i[0], i[1]))


def constraint_sectionprint_writer(f, femobj, sectionprint_obj, ccxwriter):
    f.write(
        "*SECTION PRINT, SURFACE=SECTIONFACE{}, NAME=SECTIONPRINT{}\n"
        .format(sectionprint_obj.Name, sectionprint_obj.Name)
    )
    f.write("SOF, SOM, SOAREA\n")