# vim:set noet ts=4:
conf_DATA = \
    $(NULL)

EXTRA_DIST= \
  system-config-language.pam \
  system-config-language.console

confdir = $(sysconfdir)

PKGNAME=system-config-language

install-data-local:
	mkdir -p $(DESTDIR)$(sysconfdir)/pam.d
	mkdir -p $(DESTDIR)$(sysconfdir)/security/console.apps
	install -m 0644 ${PKGNAME}.pam $(DESTDIR)$(sysconfdir)/pam.d/${PKGNAME}
	install -m 0644 ${PKGNAME}.console $(DESTDIR)$(sysconfdir)/security/console.apps/${PKGNAME}

uninstall-local:
	rm $(DESTDIR)$(sysconfdir)/pam.d/${PKGNAME}
	rm $(DESTDIR)$(sysconfdir)/security/console.apps/${PKGNAME}

