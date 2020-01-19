Summary:  A graphical interface for modifying the system language
Name:     system-config-language
Version:  1.4.0
Release:  7%{?dist}
URL:      https://fedorahosted.org/system-config-language/
Source0:  https://fedorahosted.org/releases/s/y/system-config-language/%{name}-%{version}.tar.bz2
#https://bugzilla.redhat.com/show_bug.cgi?id=1040298
Patch0:   %{name}-%{version}-Disable-OK-for-default-language.patch
#https://bugzilla.redhat.com/show_bug.cgi?id=1040309
Patch1:   %{name}-%{version}-Fix-No-Groups-exists-traceback.patch
#https://bugzilla.redhat.com/show_bug.cgi?id=1045993
Patch2:   %{name}-%{version}-Change-Oriya-to-Odia.patch
#https://bugzilla.redhat.com/show_bug.cgi?id=1050967
Patch3:   %{name}-%{version}-Fix-text-mode-crash-for-no-group-exists.patch
#https://bugzilla.redhat.com/show_bug.cgi?id=1046846
Patch4:   %{name}-%{version}-translation-updates.patch
Patch5:   %{name}-%{version}-update-po-headers.patch
#https://bugzilla.redhat.com/show_bug.cgi?id=1328068
Patch6:   %{name}-%{version}-enhance-ui-messages.patch
License:  GPLv2+

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: python2-devel

Requires: pygtk2
Requires: usermode
Requires: usermode-gtk
Requires: yum
Requires: gtk2

%description
system-config-language is a graphical user interface that 
allows the user to change the default language of the system.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p1
%patch6 -p1

%build
%configure

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

desktop-file-install --vendor system --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
  --add-category System \
  --add-category Settings \
  --add-category X-Red-Hat-Base                             \
  %{buildroot}%{_datadir}/applications/system-config-language.desktop

%find_lang %name

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%doc COPYING
%{_bindir}/system-config-language
%dir %{_datadir}/system-config-language
%{_datadir}/system-config-language/*
%{_datadir}/applications/system-config-language.desktop
%{_datadir}/icons/hicolor/48x48/apps/system-config-language.png
%{_mandir}/man1/system-config-language.1.gz
%config(noreplace) %{_sysconfdir}/pam.d/system-config-language
%config(noreplace) %{_sysconfdir}/security/console.apps/system-config-language

%changelog
* Wed Apr 20 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.4.0-7
- Resolves:rh#1328068 - enhance the UI messages when clicked on OK button

* Wed Jan 15 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.4.0-6
- Resolves:rh#1046846 - [system-config-language] Translations incomplete

* Tue Jan 14 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.4.0-5
- Resolves:rh#1045993 - Change language name from Oriya to Odia.

* Mon Jan 13 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.4.0-4
- Resolves:rh#1050967 - system-config-language traceback due to missing zulu-support package

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4.0-3
- Mass rebuild 2013-12-27

* Mon Dec 23 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.4.0-2
- Resolves:rh#1040298 - OK button should be disabled always for the default selected language
- Resolves:rh#1040309 - Fix 'No Group named...exists' dialog produced traceback & warning messages
- Resolves:rh#1045993 - Change language name from Oriya to Odia.

* Mon Jun 10 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.4.0-1
- Update to 1.4.0 release

* Fri May 10 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.3.6-1
- Update to 1.3.6 release

* Fri Apr 26 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.3.5-24
- Resolves:rh#956784 - Add Interlingua to the local-list file and include Interlingua localization to the package

* Mon Apr 22 2013 Pravin Satpute <psatpute@redhat.com> - 1.3.5-23
- Resolves: rh#638650 reverting changes for zh_TW

* Mon Apr 22 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.3.5-22
- Resolves:rh#954124 - No kyrgyz language in s-c-l

* Mon Apr 08 2013 Pravin Satpute <psatpute@redhat.com> - 1.3.5-21
- Improved patch 638650 as per comments by reporter

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 08 2013 Parag Nemade <pnemade AT redhat DOT com> - 1.3.5-19
- Resolves:rh#886446 - system-config-language tracebacks in TUI mode
- Resolves:rh#892560 - system-config-language only provides english in Fedora 18
- Resolves:rh#889956 - include language Kashmiri Arabic

* Mon Nov 26 2012 Pravin Satpute <psatpute@redhat.com> - 1.3.5-18
- Patched Makefile

* Mon Nov 26 2012 Anish Patil <apatil@redhat.com> - 1.3.5-17
- Fixed Requires python-devel issue

* Fri Nov 23 2012 Anish Patil <apatil@redhat.com> - 1.3.5-16
- Fixed bug 879472

* Fri Nov 2 2012 Anish Patil <apatil@redhat.com> - 1.3.5-14
- Fixed bugs 860453,871119

* Thu Sep 20 2012 Anish Patil <apatil@redhat.com> - 1.3.5-13
- Fixed bugs 858168,858059,858056

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Pravin Satpute <psatpute@redhat.com>- 1.3.5-11
- Resolves bug 817083

* Fri Mar 30 2012 Pravin Satpute <psatpute@redhat.com>- 1.3.5-10
- Resolved bug-803851

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon May 02 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.3.5-8
- fix loading on the KDE spin (#700967, s-c-l-700967.patch)

* Wed Mar 09 2011 Naveen Kumar <nkumar@redhat.com>- 1.3.5-7
- apply patch s-c-l-681802_681805.patch
- resolves bug #681802 & #681805

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 11 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.5-5
- apply patch s-c-l-634556.patch
- resolves bug #634556
- modifications in s-c-l to install even conditional & default packages

* Thu Oct 7 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.5-4
- apply patch s-c-l-638650.patch
- resolves bug #638650

* Mon Oct 4 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.5-3
- Spec file updated according to new guidelines
- resolves bug #624008

* Fri Oct 1 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.5-2
- resolves bug #624008
- apply patch s-c-l-624008.patch
- adds Low-German (nds_DE) to s-c-l
- comment a redundant line in language_backend.py

* Wed Sep 8 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.5-1
- new release by upstream

* Mon Aug 9 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.4-6
- apply patch s-c-l_445796_545499.patch
- resolves bug #445796
- resolves bug #545499

* Fri Jul 9 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.4-5
- apply patch s-c-l_607927.patch
- resolves bug #607927

* Tue Jun 22 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.4-4
- apply patch s-c-l_545499.patch
- resolves bug #545499

* Fri Jun 18 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.4-3
- apply patch s-c-l_598423.patch
- resolves bug #598423

* Wed Apr 14 2010 Naveen Kumar <nkumar@redhat.com>- 1.3.4-2
- apply patch scl-1.3.4-devel.patch
- contains some enhanc. reg. force. change of lang. when dep. are not installed 
- Resolves Bug #568688

* Wed Mar 10 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.4-1
- upstrem new release with updated translations 
- committed patches to upstream

* Fri Feb 26 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.3-6
- resolved bug 568653

* Thu Feb 25 2010 Pravin Satpute <psatpute@redhat.com>- 1.3.3-5
- resolved bug 568285

* Thu Dec 10 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-4
- updated URL and source field

* Mon Oct 26 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-3
- fixed 530698

* Fri Oct 09 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-2
- fixed 525040

* Wed Sep 23 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.3-1
- upstream release of 1.3.3
- updated .pot files

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 24 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-9
- fix bug 493888

* Mon Jul 13 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-8
- fix bug 493858, 507796

* Tue Jul 07 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-7
- fix bug 598975
- patch from Jeremy Katz katzj@redhat.com

* Mon May 25 2009 Pravin Satpute <psatpute@redhat.com>- 1.3.2-6
- fix bug 493824

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.2-4
- Rebuild for Python 2.6

* Wed Oct 22 2008 Pravin Satpute <psatpute@redhat.com>- 1.3.2-3
- fix bug 467919

* Wed Oct 8 2008 Pravin Satpute <psatpute@redhat.com>- 1.3.2-2
- fix bug 462914

* Wed Sep 17 2008 Pravin Satpute <psatpute@redhat.com>- 1.3.2-1
- upstream realease 1.3.2
- fix bug 444568, 462439

* Wed Jul 16 2008 Pravin Satpute <psatpute@redhat.com> - 1.3.1-2
- fix bug 442901

* Tue Jun 24 2008 Pravin Satpute <psatpute@redhat.com> - 1.3.1-1
- upstream release 1.3.1

* Mon May 26 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.15-5
- modified system-config-language-447008.patch file

* Thu May 22 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.15-4
- fix bug 447008
- fix bug 429808
- fix bug 447879

* Mon Apr 28 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.15-3
- fix bug 442901

* Tue Jan 15 2008 Lingning Zhang <lizhang@redhat.com> - 1.2.15-2
- fix bug428391.

* Wed Dec 26 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.15-1
- fix bug294561.

* Tue Nov 27 2007 Parag Nemade <pnemade@redhat.com> - 1.2.14-2
- Merge review SPEC cleanup rh#226461

* Mon Nov 19 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.14
- fix bug386731.

* Mon Oct 22 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.13
- fix bug332361.

* Tue Oct 9 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.12
- fix bug294531.

* Fri Sep 21 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.11
- fix bug294571.

* Thu Sep 20 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.10
- fix bug288851 and bug297461.
- add the Nepali support.

* Mon Sep 10 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.9
- fix bug275711 and bug284331.

* Mon Aug 20 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.8
- re-fix bug251478.

* Mon Aug 13 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.7
- fix bug251478.

* Mon Aug 6 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.6
- re-fix bug241744.

* Thu Jul 5 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.5
- fix bug241746.

* Tue Jul 3 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.4
- fix bug241747 and bug246578.

* Tue Jul 3 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.3
- fix bug245872 and bug241744.

* Tue Jun 19 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.2
- modify the category value in system-config-language.spec.
- fix bug243529. 

* Mon Jun 18 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.1
- Fix bug237715, bug241744 and bug225949(patch from Stephanos Manos).

* Tue May 29 2007 Lingning Zhang <lizhang@redhat.com> - 1.2.0
- support to install languages what is not installed.

* Fri May 25 2007 Lingning Zhang <lizhang@redhat.com> - 1.1.18-1
- Update translations (#216093)
- Add new languages (#217125, #239999)

* Wed Nov 22 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.16-1
- Update translations (#216093)

* Thu Nov 16 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.15-1
- Use correct Norwegian language (#209438)
- Fix traceback in text mode (#215319)
- Update potfile

* Fri Oct 20 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.14-1
- Fix typos (#211434)

* Mon Oct 16 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.13-1
- Fix Chinese locale re-selection (#208407)

* Fri Oct 13 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.12-1
- Add Orya support (#210373)

* Mon Jul 17 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.11-2
- Don't nuke *.pyc in preun (#198959)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.11-1.1
- rebuild

* Tue Feb 28 2006 Paul Nasrat <pnasrat@redhat.com> - 1.1.11-1
- Update translations
- Serbian locales (#172600)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 24 2005 Paul Nasrat <pnasrat@redhat.com> - 1.1.10-1
- pam_stack deprecated (#170631)

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1.1.9-2
- silence %%post

* Fri Apr 01 2005 Paul Nasrat <pnasrat@redhat.com> 1.1.9-1
- Translation updates
- pygtk deprecations

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 1.1.8-2
- Update the GTK+ theme icon cache on (un)install

* Fri Oct 01 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.8-1
- Indic UTF-8 locales
- Translations

* Wed Sep 29 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.7-1
- update locale-list (bug# 134034)

* Tue Sep 07 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.6-2
- Buildrequires intltool

* Tue Sep 07 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.6-1
- Translatable desktop

* Mon Sep 06 2004 Paul Nasrat <pnasrat@redhat.com> 1.1.5-3
- fix gtk.mainloop/mainquit 

* Thu Apr  8 2004 Brent Fox <bfox@redhat.com> 1.1.5-2
- fix icon path (bug #120177)

* Mon Jan 12 2004 Brent Fox <bfox@redhat.com> 1.1.5-1
- update locale-list (bug #107450)

* Fri Jan  9 2004 Brent Fox <bfox@redhat.com> 1.1.4-1
- enable TUI mode

* Wed Jan 07 2004 Than Ngo <than@redhat.com> 1.1.3-1
- make changes for Python2.3

* Thu Nov 20 2003 Brent Fox <bfox@redhat.com> 1.1.2-1
- fix typo in the Obsoletes

* Wed Nov 19 2003 Brent Fox <bfox@redhat.com> 1.1.1-1
- rebuild

* Wed Nov 12 2003 Brent Fox <bfox@redhat.com> 1.1.0-1
- add Obsoletes for redhat-config-language
- make changes for Python2.3

* Mon Nov 10 2003 Brent Fox <bfox@redhat.com> 1.1.0-1
- convert redhat-config-language into system-config-language

* Mon Oct 13 2003 Brent Fox <bfox@redhat.com> 1.0.16-1
- rebuild for latest translations (bug #106618)

* Mon Sep 15 2003 Brent Fox <bfox@redhat.com> 1.0.15-2
- bump release num and rebuild

* Mon Sep 15 2003 Brent Fox <bfox@redhat.com> 1.0.15-1
- add Requires for rhpl (bug #104210)

* Thu Aug 14 2003 Brent Fox <bfox@redhat.com> 1.0.14-1
- tag on every release

* Wed Aug 13 2003 Brent Fox <bfox@redhat.com> 1.0.12-1
- remove python-tools dependency

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.11-2
- bump relnum and rebuild

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.11-1
- fix build problem

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.10-2
- bump relnum and rebuild

* Thu Jul 31 2003 Brent Fox <bfox@redhat.com> 1.0.10-1
- change runPriority

* Thu Jul  3 2003 Brent Fox <bfox@redhat.com> 1.0.9-2
- bump relnum and rebuild

* Thu Jul  3 2003 Brent Fox <bfox@redhat.com> 1.0.9-1
- use UTF-8 in CJK locales (bug #98522)

* Wed Jul  2 2003 Brent Fox <bfox@redhat.com> 1.0.8-2
- bump relnum and rebuild

* Wed Jul  2 2003 Brent Fox <bfox@redhat.com> 1.0.8-1
- use rhpl translation module

* Thu Jun 26 2003 Brent Fox <bfox@redhat.com> 1.0.7-1
- make sure the config file is written before calling changeLocale()

* Thu Jun 26 2003 Brent Fox <bfox@redhat.com> 1.0.6-1
- add some hooks for firstboot so locale can change on the fly (#91984)

* Wed May 21 2003 Brent Fox <bfox@redhat.com> 1.0.5-1
- add some hacks to make simplified chinese work (bug #84772)

* Tue Feb 18 2003 Brent Fox <bfox@redhat.com> 1.0.4-1
- update locale-list (bug #84183)

* Wed Feb 12 2003 Jeremy Katz <katzj@redhat.com> 1.0.3-3
- fixes for cjk tui (#83518)

* Thu Jan 30 2003 Brent Fox <bfox@redhat.com> 1.0.3-2
- fix a po file encoding problem.  please use utf-8 in the future

* Thu Jan 30 2003 Brent Fox <bfox@redhat.com> 1.0.3-1
- bump and build

* Thu Jan 23 2003 Brent Fox <bfox@redhat.com> 1.0.2-2
- add Bulgarian to locale-list

* Thu Jan 23 2003 Brent Fox <bfox@redhat.com> 1.0.2-1
- update translations in desktop file

* Tue Dec 17 2002 Bill Nottingham <notting@redhat.com> 1.0.1-13
- fix dangling symlink that broke firstboot

* Mon Dec 16 2002 Brent Fox <bfox@redhat.com> 1.0.1-12
- fix a typo

* Mon Dec 16 2002 Brent Fox <bfox@redhat.com> 1.0.1-11
- show a warning if run in console mode (bug #78739)

* Sun Dec 15 2002 Brent Fox <bfox@redhat.com> 1.0.1-10
- strip off @euro from the supported langs (bug #77637)

* Tue Nov 12 2002 Brent Fox <bfox@redhat.com> 1.0.1-9
- pam path changes

* Tue Oct 15 2002 Brent Fox <bfox@redhat.com> 1.0.1-8
- Handle upgrading with different encodings in /etc/sysconfig/clock

* Thu Sep 19 2002 Brent Fox <bfox@redhat.com> 1.0.1-7
- Patch to desktop file from kmraas@online.no applied for [no] translation

* Tue Sep 10 2002 Bill Nottingham <notting@redhat.com> 1.0.1-6
- don't write SYSFONTACM="utf8"; switch default font to match anaconda

* Tue Sep  3 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.1-5
- Obsolete locale_config

* Wed Aug 28 2002 Brent Fox <bfox@redhat.com> 1.0.1-4
- Convert to noarch

* Wed Aug 28 2002 Brent Fox <bfox@redhat.com> 1.0.1-3
- Remove dupe for Romanian

* Wed Aug 28 2002 Brent Fox <bfox@redhat.com> 1.0.1-2
- Only apply the changes if the user actually changed something

* Wed Aug 21 2002 Preston Brown <pbrown@localhost.localdomain> 1.0.1-1
- we were writing to the wrong gdm file...

* Fri Aug 16 2002 Brent Fox <bfox@redhat.com> 1.0-2
- pull translations into locale-list
- convert locale-list to UTF-8

* Fri Aug 16 2002 Preston Brown <pbrown@redhat.com> 1.0-1
- reset GDM config if lang changes

* Wed Aug 14 2002 Brent Fox <bfox@redhat.com> 0.9.9-8
- call destroy on window close

* Tue Aug 13 2002 Tammy Fox <tfox@redhat.com> 0.9.9-7
- better icon

* Tue Aug 13 2002 Brent Fox <bfox@redhat.com> 0.9.9-6
- Fix desktop file icon path

* Mon Aug 12 2002 Brent Fox <bfox@redhat.com> 0.9.9-5
- update locale list

* Mon Aug 12 2002 Tammy Fox <tfox@redhat.com> 0.9.9-4
- Replace System with SystemSetup in desktop file categories

* Sun Aug 11 2002 Brent Fox <bfox@redhat.com> 0.9.9-3
- fix desktop file

* Mon Aug 05 2002 Brent Fox <bfox@redhta.com> 0.9.9-1
- pull in desktop file translations

* Fri Aug 02 2002 Tammy Fox <tfox@redhat.com> 0.9.8-2
- Fix desktop file categories

* Fri Aug 02 2002 Brent Fox <bfox@redhat.com> 0.9.8-1
- Make changes for new pam timestamp policy

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 0.9.6-3
- fix Makefiles and spec files so that translations get installed

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 0.9.6-2
- update spec file for public beta 2

* Tue Jul 23 2002 Tammy Fox <tfox@redhat.com> 0.9.5-2
- Fix desktop file (bug #69475)

* Thu Jul 18 2002 Brent Fox <bfox@redhat.com> 0.9.5-1
- Update for pygtk2 API change

* Tue Jul 16 2002 Brent Fox <bfox@redhat.com> 0.9.4-2
- bump rev num and rebuild

* Thu Jul 11 2002 Brent Fox <bfox@redhat.com> 0.9.3-2
- Update changelogs and rebuild

* Thu Jul 11 2002 Brent Fox <bfox@redhat.com> 0.9.3-1
- Update changelogs and rebuild

* Mon Jul 01 2002 Brent Fox <bfox@redhat.com> 0.9.2-1
- Bump rev number

* Mon Jul 01 2002 Brent Fox <bfox@redhat.com> 0.9.2-1
- Bump rev number

* Thu Jun 27 2002 Brent Fox <bfox@redhat.com> 0.9.1-2
- Added a message dialog when applying changes

* Wed Jun 26 2002 Brent Fox <bfox@redhat.com> 0.9.1-1
- Fixed description

* Tue Jun 25 2002 Brent Fox <bfox@redhat.com> 0.9.4-5
- Create pot file

* Mon Jun 24 2002 Brent Fox <bfox@redhat.com> 0.9.4-4
- Fix spec file

* Fri Jun 21 2002 Brent Fox <bfox@redhat.com> 0.9.0-3
- Remove cancel button
- init doDebug to None

* Thu Jun 20 2002 Brent Fox <bfox@redhat.com> 0.9.0-2
- Don't pass doDebug into init
- Add snapsrc to Makefile

* Wed May 29 2002 Brent Fox <bfox@redhat.com> 0.2.0-6
- handle an existing but empty i18n file 

* Sun May 26 2002 Brent Fox <bfox@redhat.com> 0.2.0-5
- raise a RuntimeError if /etc/sysconfig/i18n file doesn't exist

* Tue May 14 2002 Brent Fox <bfox@redhat.com>
- improved check for existing i18n file
- added debug mode capability

* Wed Nov 28 2001 Brent Fox <bfox@redhat.com>
- initial coding and packaging

