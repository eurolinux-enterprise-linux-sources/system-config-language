#!/usr/bin/python

## languageBackend.py - Contains the backend code needed for system-config-language
## Copyright (C) 2002, 2003 Red Hat, Inc.
## Copyright (C) 2002, 2003 Brent Fox <bfox@redhat.com>

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import string
import os
import commands

##
## I18N
## 
import gettext
gettext.bindtextdomain ("system-config-language", "/usr/share/locale")
gettext.textdomain ("system-config-language")
_=gettext.gettext

class LanguageBackend:
    def getInstalledLangs(self):
        self.originalFile = None
        path = '/etc/locale.conf'
        if os.access(path, os.R_OK) == 0:
            return None, None
        else:
            fd = open(path, "r")
            self.originalFile = fd.readlines()
            fd.close()

            defaultLang = None
            langs = None

            for line in self.originalFile:
                if line[:5] == "LANG=":
                    defaultLang = string.replace(line[5:], '"', '')
                    defaultLang = string.strip(defaultLang)
                if line[:9] == "SUPPORTED":
                    langs = string.replace(line[10:], '"', '')
                    langs = string.strip(langs)
                    langs = string.split(langs, ':')

            if langs:
                for lang in langs:
                    #Chop off any encoding data.  We don't really need it
                    langBase = self.removeEncoding(lang)
                    langs[langs.index(lang)] = langBase

            if defaultLang:
                defaultLang = self.removeEncoding(defaultLang)
            else:
                defaultLang = "en_US"
            
            return defaultLang, langs

    def removeEncoding(self, lang):
        if '@' in lang:
            langBase = string.split(lang, '@')
            return langBase[0]
        elif '.' in lang:
            langBase = string.split(lang, '.')
            return langBase[0]
        else:
            return lang

    def readTable(self):
        lines = None
        fd = None
        try:
            fd = open("locale-list", "r")
        except:
            try:
                fd = open("/usr/share/system-config-language/locale-list", "r")
            except:
                pass

        if fd:
            lines = fd.readlines()
            fd.close()

        if not lines:
            raise RuntimeError, (_("Cannot find locale-list"))
        else:
            return lines

    def writeI18N(self, defaultLang, modules, sysfont, sysfontacm):
        locale_path = '/etc/locale.conf'
        if os.access(locale_path, os.R_OK) != 0:
            fd = open(locale_path, 'w')
            if self.originalFile:
                for line in self.originalFile:
                    if line[:5] == "LANG=":
                        fd.write('LANG="' + defaultLang + '"\n')
                         #XXX - horrible hack to make simplified chinese work
                        if defaultLang == "zh_CN.GB18030":
                            fd.write('LANGUAGE="zh_CN.GB18030:zh_CN.GB2312:zh_CN"\n')
                    elif line[:9] == 'LANGUAGE=':
                        #XXX - horrible hack to make simplified chinese work
                        if defaultLang != "zh_CN.GB18030":
                            pass
                    else:
                        fd.write(line)
            else:
                fd.write('LANG="' + defaultLang + '"\n')
            vsconsole_file = "/etc/vconsole.conf"
            fd = open(vsconsole_file, "r")
            vsconsole_data = fd.readlines()
            fd.close()
            fd = open(vsconsole_file, "w")
            for line in vsconsole_data:
                if line[:5] == "FONT=":
                    fd.write('FONT="' + sysfont + '"\n')
                else:
                    fd.write(line)
            fd.close()
        else:
            fd = open('/etc/sysconfig/i18n', 'w')
            if self.originalFile:
                for line in self.originalFile:
                    if line[:5] == "LANG=":
                        fd.write('LANG="' + defaultLang + '"\n')
                         #XXX - horrible hack to make simplified chinese work
                        if defaultLang == "zh_CN.GB18030":
                            fd.write('LANGUAGE="zh_CN.GB18030:zh_CN.GB2312:zh_CN"\n')
                    elif line[:8] == "SYSFONT=":
                        fd.write('SYSFONT="' + sysfont + '"\n')                
                    elif line[:11] == 'SYSFONTACM=':
                        fd.write('SYSFONTACM="' + sysfontacm + '"\n')
                    elif line[:9] == 'LANGUAGE=':
                        #XXX - horrible hack to make simplified chinese work
                        if defaultLang != "zh_CN.GB18030":
                            pass
                    else:
                        fd.write(line)
            else:
                fd.write('LANG="' + defaultLang + '"\n')
                if modules:
                    fd.write('SUPPORTED="' + modules + '"\n')
                    fd.write('SYSFONT="' + sysfont + '"\n')
                if sysfontacm != "utf8":
                    fd.write('SYSFONTACM="' + sysfontacm + '"\n')
                    #XXX - horrible hack to make simplified chinese work
                if defaultLang == "zh_CN.GB18030":
                    fd.write('LANGUAGE="zh_CN.GB18030:zh_CN.GB2312:zh_CN"\n')
            fd.close()

        # hack for writing information to grub.conf, thanks to  Hans de Goede  <hdegoede@redhat.com> for mentioning this.
        # resolves RHBZ bug # 545499
        # (cmdstatus, cmdout)= commands.getstatusoutput('/sbin/new-kernel-pkg --package kernel --dracut --install $(uname -r)')        

        (cmdstatus, cmdout)= commands.getstatusoutput('rpm -q kernel kernel-PAE | grep -v kernel-PAE ')
        kernels=cmdout.split('\n')
        for kernel in kernels:
            (cmdstatus, cmdout)= commands.getstatusoutput('/sbin/new-kernel-pkg --package kernel --dracut --install '+kernel)
    
        (cmdstatus, cmdout)= commands.getstatusoutput('rpm -q kernel kernel-PAE | grep  kernel-PAE |grep -v \'package kernel-PAE is not installed\' ')
        kernels=cmdout.split('\n')
        for kernel in kernels:
            (cmdstatus, cmdout)= commands.getstatusoutput('/sbin/new-kernel-pkg --package kernel-PAE --dracut --install '+kernel)

