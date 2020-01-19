## Process this file with automake to produce Makefile.in

SUBDIRS = src po data

EXTRA_DIST =  autogen.sh ChangeLog.old \
	system-config-language.desktop.in \
	intltool-extract.in  \
	intltool-merge.in    \
	intltool-update.in


Applicationsdir = $(datadir)/applications
Applications_in_files = system-config-language.desktop.in
Applications_DATA = $(Applications_in_files:.desktop.in=.desktop)
@INTLTOOL_DESKTOP_RULE@

DISTCLEANFILES=                                 \
	intltool-extract                        \
	intltool-merge                  \
	intltool-update                 \
	system-config-language.desktop

install-data-local:
	@$(NORMAL_INSTALL)

dist-hook:
	$(MAKE) -C "$(srcdir)/po" "$(GETTEXT_PACKAGE).pot"
	cp -p "$(srcdir)/po/$(GETTEXT_PACKAGE).pot" "$(distdir)/po/"


# Manpage
  sclmandir = $(mandir)/man1
  dist_sclman_DATA = system-config-language.1

