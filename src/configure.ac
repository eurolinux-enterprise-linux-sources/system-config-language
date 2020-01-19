dnl Process this file with autoconf to produce a configure script.
AC_PREREQ(2.60)

AC_INIT([system-config-language], [1.4.0])
AM_CONFIG_HEADER(config.h)
AM_INIT_AUTOMAKE([dist-xz dist-bzip2 subdir-objects])
AM_MAINTAINER_MODE

AC_ISC_POSIX
AC_PROG_CC
AM_PROG_CC_STDC
AC_HEADER_STDC

AC_PROG_INTLTOOL([0.35.0])

GETTEXT_PACKAGE=system-config-language
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE,"$GETTEXT_PACKAGE", [Gettext package.])

dnl Add the languages which your application supports here.
ALL_LINGUAS="ar as ast be bg bn_IN bn bs ca cs cy da de el en_GB es et fa fi fr gl gu he hi hr hu hy ia id is it ja ka kn ko ks@devanagari ku lo lt lv mai mk ml mn mr ms my nb nds nl or pa pl pt_BR pt ro ru si sk sl sq sr@latin sr sv ta te tg th tr uk ur vi zh_CN zh_TW zu "

AM_GLIB_GNU_GETTEXT

AC_OUTPUT([
Makefile
system-config-language.desktop.in
src/Makefile
po/Makefile.in
data/Makefile
data/icons/Makefile
data/conf/Makefile
])

