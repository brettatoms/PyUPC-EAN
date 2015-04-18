#!/usr/bin/env python

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2015 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2011-2015 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: pydeb-den.py - Last Update: 4/18/2015 Ver. 0.0.1 RC 1 - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import re, os, sys, time, datetime;

proname = "pydeb-gen";
prover = "0.0.1";

pkgsource = "py3upc-ean";
pkgver = "2.7.11-3";
pkgdistname = "trusty";
pkgurgency = "urgency=low";
pkgmaintainername = "Kazuki Przyborowski";
pkgmaintaineremail = "kazuki.przyborowski@gmail.com";
pkgmaintainer = pkgmaintainername+" <"+pkgmaintaineremail+">";
pkghomepage = "https://github.com/GameMaker2k/PyUPC-EAN/";
pkgsection = "python";
pkgpriority = "optional";
pkgbuilddepends = "python3-setuptools, python3-all, python3-imaging, debhelper";
pkgstandardsversion = "3.9.1";
pkgpackage = "python3-pyupcean";
pkgarchitecture = "all";
pkgdepends = "${misc:Depends}, ${python:Depends}";
pkgdescription = "A barcode library/module for python.\n PyUPC-EAN is a barcode library/module for Python. It supports the barcode formats upc-e, upc-a, ean-13, ean-8, ean-2, ean-5, itf14, codabar, code11, code39, code93, and msi.";
pkgmycurtime = datetime.datetime.now();
pkgmycurtimetuple = pkgmycurtime.timetuple();
pkgutccurtime = datetime.datetime.utcnow();
pkgutccurtimetuple = pkgutccurtime.timetuple();
pkgtzhour = datetime.datetime.now().timetuple()[3] - datetime.datetime.utcnow().timetuple()[3];
if(pkgtzhour<0):
 pkgtzhourstr = "-"+str(abs(datetime.datetime.now().timetuple()[3]-datetime.datetime.utcnow().timetuple()[3])).zfill(2);
if(pkgtzhour>=0):
 pkgtzhourstr = str(abs(datetime.datetime.now().timetuple()[3]-datetime.datetime.utcnow().timetuple()[3])).zfill(2);
pkgtzminute = datetime.datetime.now().timetuple()[4] - datetime.datetime.utcnow().timetuple()[4];
pkgtzminutestr = str(pkgtzminute).zfill(2);
pkgtzstr = time.strftime("%a, %d %b %Y %H:%M:%S")+" "+pkgtzhourstr+pkgtzminutestr;

debpkg_debian_dir = os.path.realpath(os.getcwd()+os.path.sep+"debian");
if(not os.path.exists(debpkg_debian_dir)):
 os.makedirs(debpkg_debian_dir);

debpkg_changelog_file = os.path.realpath(debpkg_debian_dir+os.path.sep+"changelog");
debpkg_string_temp = pkgsource+" ("+pkgver+") "+pkgdistname+"; "+pkgurgency+"\n\n";
debpkg_string_temp += "  * source package automatically created by "+proname+" "+prover+"\n\n";
debpkg_string_temp += " -- "+pkgmaintainer+"  "+pkgtzstr+"\n";
debpkg_file_temp = open(debpkg_changelog_file, "w");
debpkg_file_temp.write(debpkg_string_temp);
debpkg_file_temp.close();

debpkg_compat_file = os.path.realpath(debpkg_debian_dir+os.path.sep+"compat");
debpkg_string_temp = "7\n";
debpkg_file_temp = open(debpkg_compat_file, "w");
debpkg_file_temp.write(debpkg_string_temp);
debpkg_file_temp.close();

debpkg_control_file = os.path.realpath(debpkg_debian_dir+os.path.sep+"control");
debpkg_string_temp = "Source: "+pkgsource+"\n";
debpkg_string_temp += "Maintainer: "+pkgmaintainer+"\n";
debpkg_string_temp += "Homepage: "+pkghomepage+"\n";
debpkg_string_temp += "Section: "+pkgsection+"\n";
debpkg_string_temp += "Priority: "+pkgpriority+"\n";
debpkg_string_temp += "Build-Depends: "+pkgbuilddepends+"\n";
debpkg_string_temp += "Standards-Version: "+pkgstandardsversion+"\n\n";
debpkg_string_temp += "Package: "+pkgpackage+"\n";
debpkg_string_temp += "Architecture: "+pkgarchitecture+"\n";
debpkg_string_temp += "Depends: "+pkgdepends+"\n";
debpkg_string_temp += "Description: "+pkgdescription+"\n";
debpkg_file_temp = open(debpkg_control_file, "w");
debpkg_file_temp.write(debpkg_string_temp);
debpkg_file_temp.close();

debpkg_rules_file = os.path.realpath(debpkg_debian_dir+os.path.sep+"rules");
debpkg_string_temp = "#!/usr/bin/make -f\n\n";
debpkg_string_temp += "# This file was automatically generated by stdeb 0.6.0+git at\n";
debpkg_string_temp += "# Fri, 17 Apr 2015 03:46:00 -0500\n\n";
debpkg_string_temp += "%:\n";
debpkg_string_temp += "	dh $@ --with python3\n";
debpkg_string_temp += "override_dh_auto_build:\n";
debpkg_string_temp += "	python3 setup.py build\n\n";
debpkg_string_temp += "override_dh_auto_test:\n";
debpkg_string_temp += "	python3 setup.py test\n\n";
debpkg_string_temp += "override_dh_auto_install:\n";
debpkg_string_temp += "	python3 setup.py install \\\n";
debpkg_string_temp += "        --force --root=$(CURDIR)/debian/python3-pyupcean \\\n";
debpkg_string_temp += "        --no-compile -O0 --install-layout=deb\n\n";
debpkg_string_temp += "override_dh_auto_clean:\n";
debpkg_string_temp += "	python3 setup.py clean\n";
debpkg_file_temp = open(debpkg_rules_file, "w");
debpkg_file_temp.write(debpkg_string_temp);
debpkg_file_temp.close();

debpkg_source_dir = os.path.realpath(debpkg_debian_dir+os.path.sep+"source");
if(not os.path.exists(debpkg_source_dir)):
 os.makedirs(debpkg_source_dir);

debpkg_format_file = os.path.realpath(debpkg_source_dir+os.path.sep+"format");
debpkg_string_temp = "3.0 (native)\n";
debpkg_file_temp = open(debpkg_format_file, "w");
debpkg_file_temp.write(debpkg_string_temp);
debpkg_file_temp.close();

debpkg_options_file = os.path.realpath(debpkg_source_dir+os.path.sep+"options");
debpkg_string_temp = "extend-diff-ignore=\"\\.egg-info\"\n";
debpkg_file_temp = open(debpkg_options_file, "w");
debpkg_file_temp.write(debpkg_string_temp);
debpkg_file_temp.close();
