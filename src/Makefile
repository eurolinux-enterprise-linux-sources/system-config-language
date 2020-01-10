#License: GPL
#Copyright Red Hat Inc.  Jan 2001

PKGNAME=system-config-language
VERSION=$(shell awk '/Version:/ { print $$2 }' ${PKGNAME}.spec)
CVSTAG=r$(subst .,-,$(VERSION))
SUBDIRS=po

MANDIR=/usr/share/man
PREFIX=/usr
DATADIR=${PREFIX}/share
PKGDATADIR=${DATADIR}/${PKGNAME}
PKGIMAGESDIR=${PKGDATADIR}/images

PAMD_DIR        = /etc/pam.d
SECURITY_DIR    =/etc/security/console.apps

default: subdirs

subdirs:
	for d in $(SUBDIRS); do make -C $$d; [ $$? = 0 ] || exit 1; done

install: ${PKGNAME}.desktop
	mkdir -p $(INSTROOT)/usr/bin
	mkdir -p $(INSTROOT)$(PKGDATADIR)
	mkdir -p $(INSTROOT)$(PAMD_DIR)
	mkdir -p $(INSTROOT)$(SECURITY_DIR)
	mkdir -p $(INSTROOT)$(PKGDATADIR)/pixmaps
	mkdir -p $(INSTROOT)/usr/share/applications
#	mkdir -p $(INSTROOT)/usr/share/firstboot
#	mkdir -p $(INSTROOT)/usr/share/firstboot/modules
	mkdir -p $(INSTROOT)/usr/share/icons/hicolor/48x48/apps

	install src/*.py $(INSTROOT)$(PKGDATADIR)
	install src/locale-list $(INSTROOT)$(PKGDATADIR)
	install src/${PKGNAME} $(INSTROOT)$(PKGDATADIR)/${PKGNAME}
	install ${PKGNAME}.desktop $(INSTROOT)/usr/share/applications/${PKGNAME}.desktop
	install ${PKGNAME}.pam $(INSTROOT)$(PAMD_DIR)/${PKGNAME}
	install ${PKGNAME}.console $(INSTROOT)$(SECURITY_DIR)/${PKGNAME}
	install pixmaps/${PKGNAME}.png $(INSTROOT)$(PKGDATADIR)/pixmaps/${PKGNAME}.png
	install pixmaps/${PKGNAME}.png $(INSTROOT)/usr/share/icons/hicolor/48x48/apps
	ln -sf consolehelper $(INSTROOT)/usr/bin/${PKGNAME}
#	ln -sf $(PKGDATADIR)/language_gui.py $(INSTROOT)/usr/share/firstboot/modules/language.py 
	for d in $(SUBDIRS); do \
	(cd $$d; $(MAKE) INSTROOT=$(INSTROOT) MANDIR=$(MANDIR) install) \
		|| case "$(MFLAGS)" in *k*) fail=yes;; *) exit 1;; esac; \
	done && test -z "$$fail"

archive:
	@rm -rf /tmp/${PKGNAME}-$(VERSION)
	@mkdir /tmp/${PKGNAME}-$(VERSION)
	@cp -r * /tmp/${PKGNAME}-$(VERSION)/
	@dir=$$PWD; cd /tmp; tar --bzip2 -cSpf $$dir/${PKGNAME}-$(VERSION).tar.bz2 ${PKGNAME}-$(VERSION)
	@rm -rf /tmp/${PKGNAME}-$(VERSION)
	@echo "The archive is in ${PKGNAME}-$(VERSION).tar.bz2"

snapsrc: archive
	@rpmbuild -ta $(PKGNAME)-$(VERSION).tar.bz2

local: clean
	@rm -rf ${PKGNAME}-$(VERSION).tar.bz2
	@rm -rf /tmp/${PKGNAME}-$(VERSION) /tmp/${PKGNAME}
	@dir=$$PWD; cd /tmp; cp -a $$dir ${PKGNAME}
	@mv /tmp/${PKGNAME} /tmp/${PKGNAME}-$(VERSION)
	@dir=$$PWD; cd /tmp; tar --bzip2 -cSpf $$dir/${PKGNAME}-$(VERSION).tar.bz2 ${PKGNAME}-$(VERSION)
	@rm -rf /tmp/${PKGNAME}-$(VERSION)	
	@echo "The archive is in ${PKGNAME}-$(VERSION).tar.bz2"

clean:
	@rm -fv *~
	@rm -fv src/*.pyc
	@rm -fv ${PKGNAME}.desktop

%.desktop: %.desktop.in
	@intltool-merge -d -u po/ $< $@
