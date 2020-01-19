## Process this file with automake to produce Makefile.in

EXTRA_DIST = \
      gui_detailsDialog.py  \
      gui_install.py   \
      i18n       \
      lang_dict.py         \
      language_gui.py  \
      locale-list  \
      system-config-language.py  \
      yumhelpers.glade  \
      gui_errors.py  \
      gui_progress.py  \
      i18n-long  \
      language_backend.py  \
      language_tui.py  \
      system-config-language  \
      tui_install.py

pkgdata_SCRIPTS = system-config-language
PKGNAME=system-config-language

install-exec-local:
	mkdir -p $(DESTDIR)$(bindir)
	ln -sf consolehelper $(DESTDIR)$(bindir)/${PKGNAME}

install-data-local:
	mkdir -p $(DESTDIR)$(pkgdatadir)
	install -m  0644 *.py $(DESTDIR)$(pkgdatadir)
	install -m 0644 locale-list $(DESTDIR)$(pkgdatadir)
	install -m 0755 ${PKGNAME} $(DESTDIR)$(pkgdatadir)/${PKGNAME}
	install -m 0644 yumhelpers.glade $(DESTDIR)$(pkgdatadir)/yumhelpers.glade

uninstall-local:
	rm $(DESTDIR)$(pkgdatadir)/*.py
	rm yumhelpers.glade locale-list
