Summary: A text-based modem control and terminal emulation program
Name: minicom
Version: 2.3
Release: 6.1%{?dist}
URL: http://alioth.debian.org/projects/minicom/
License: GPLv2+
Group: Applications/Communications
ExcludeArch: s390 s390x
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: lockdev-devel ncurses-devel
Requires: lockdev lrzsz

Source0: http://alioth.debian.org/frs/download.php/2332/minicom-2.3.tar.gz

Patch1: minicom-2.3-ncurses.patch
Patch2: minicom-2.3-drop-privs.patch
Patch4: minicom-2.2-umask.patch
Patch6: minicom-2.2-spaces.patch
Patch7: minicom-2.3-gotodir.patch
Patch8: minicom-2.3-rh.patch
Patch9: minicom-2.3-esc.patch
Patch10: minicom-2.3-staticbuf.patch
Patch11: minicom-2.3-getline.patch

%description
Minicom is a simple text-based modem control and terminal emulation
program somewhat similar to MSDOS Telix. Minicom includes a dialing
directory, full ANSI and VT100 emulation, an (external) scripting
language, and other features.

%prep
%setup -q
%patch1 -p1 -b .ncurses
%patch2 -p1 -b .drop-privs
%patch4 -p1 -b .umask
%patch6 -p1 -b .spaces
%patch7 -p1 -b .gotodir
%patch8 -p1 -b .rh
%patch9 -p1 -b .esc
%patch10 -p1 -b .staticbuf
%patch11 -p1 -b .getline

cp -pr doc doc_
rm -f doc_/Makefile*

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644 doc/minicom.users $RPM_BUILD_ROOT%{_sysconfdir}/minicom.users

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog AUTHORS NEWS TODO doc_/*
%config(noreplace) %{_sysconfdir}/minicom.users
# DO NOT MAKE minicom SUID/SGID anything.
%{_bindir}/minicom
%{_bindir}/runscript
%{_bindir}/xminicom
%{_bindir}/ascii-xfr
%{_mandir}/man1/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.3-6.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Miroslav Lichvar <mlichvar@redhat.com> 2.3-5
- rename getline to avoid conflict with glibc (#511715)
- remove makefiles from docs
- drop wchar patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Miroslav Lichvar <mlichvar@redhat.com> 2.3-3
- rediff patches with fuzz

* Thu Mar 13 2008 Lubomir Kundrak <lkundrak@redhat.com> 2.3-2
- Add ChangeLog to %doc

* Sun Feb 24 2008 Lubomir Kundrak <lkundrak@redhat.com> 2.3-1
- 2.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.2-6
- Autorebuild for GCC 4.3

* Sun Sep 23 2007 Lubomir Kundrak <lkundrak@redhat.com> 2.2-5
- Fix capture file handling (#302081)

* Wed Aug 22 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.2-4
- update license tag

* Wed Jul 25 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.2-3
- check for errors on tty device (#248701)

* Tue Jul 10 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.2-2
- improve signal handling a bit (#246465)

* Fri Mar 09 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.2-1
- update to 2.2
- handle filenames with spaces (#98655)
- add requires for lrzsz
- spec cleanup

* Tue Jul 18 2006 Martin Stransky <stransky@redhat.com> 2.1-3
- removed unnecessary debug output (#199707)

* Tue Jul 18 2006 Martin Stransky <stransky@redhat.com> 2.1-2
- added ncurses-devel to BuildPrereq

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.1-1.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Jul 14 2005 Martin Stransky <stransky@redhat.com> 2.1-1
- New upstream version

* Mon Mar  7 2005 Martin Stransky <stransky@redhat.com>
- gcc4 patch

* Wed Oct 20 2004 Adrian Havill <havill@redhat.com> 2.00.0-20
- correct an off-by-one error array-store error (#110770)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Sep 12 2003 Adrian Havill <havill@redhat.com> 2.00.0-17.1
- bump n-v-r for RHEL

* Fri Sep 12 2003 Adrian Havill <havill@redhat.com> 2.00.0-17
- fix error handling for the case when you attempt to "goto" a dir
  that doesn't exist. (#103902)
- updated URL in spec file

* Thu Aug 21 2003 Adrian Havill <havill@redhat.com> 2.00.0-16.1
- bump n-v-r for RHEL

* Thu Aug 21 2003 Adrian Havill <havill@redhat.com> 2.00.0-16
- don't overwrite buffer when ins chars (#98733)

* Wed Aug 20 2003 Adrian Havill <havill@redhat.com> 2.00.0-15.1
- bump n-v-r for RHEL

* Wed Aug 20 2003 Adrian Havill <havill@redhat.com> 2.00.0-15
- initialize savetrans, check vttrans to prevent segfaults with
  certain ESC sequences (#84129)

* Fri Aug 01 2003 Adrian Havill <havill@redhat.com> 2.00.0-14
- removed static buffers that limit multi-file zmodem functionality (#98654)
- removed assertions from above patch, massage out conflicts with rh patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Sat Jan 18 2003 Mike A. Harris <mharris@redhat.com> 2.00.0-11
- Update spec file URL to new homepage (#71894)

* Mon Dec  2 2002 Tim Powers <timp@redhat.com> 2.00.0-10
- add PreReq coreutils so that we get the ordering right in the
  install

* Wed Nov 13 2002 Mike A. Harris <mharris@redhat.com> 2.00.0-9
- Added find_lang macro andlang files to package, also avoiding 
  _unpackaged_files_terminate_build
- Added with_desktop_menu_entry macro to disable minicom.desktop by default

* Tue Oct  8 2002 Mike A. Harris <mharris@redhat.com> 2.00.0-8
- All-arch rebuild
- Make /etc/minicom.users config(noreplace)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Mike A. Harris <mharris@redhat.com> 2.00.0-4
- Rebuilt in new build environment

* Tue Feb 26 2002 Mike A. Harris <mharris@redhat.com> 2.00.0-3
- Rebuilt in new build environment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 2.00.0-2
- automated rebuild

* Wed Nov 21 2001 Mike A. Harris <mharris@redhat.com> 2.00.0-1
- Updated to version 2.00.0-0, which now uses GNU autoconf for everything,
  to ease portability and internationalization issues.  Hold on for the
  ride, as there's bound to be some bumps on the way.  ;o)  On the up side,
  the packaging is likely to be MUCH more maintainable in the future, which
  is very nice to see.
- Disabled most patches as they are either included now, not needed, or
  it has yet to be determined.

* Fri Oct 12 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.83.1-17
- Delete bad entries in ko.po, fix charset in ja.po

* Tue Aug 28 2001 Jeff Johnson <jbj@redhat.com>
- map specific errno's into status for return from helper.

* Tue Aug 14 2001 Jeff Johnson <jbj@redhat.com>
- rebuild against unzigged lockdev-1.0.0-11 (#51577).
- add BuildPrereq: on lockdev-devel, not /usr/include/baudboy.h.

* Sun Aug 12 2001 Mike A. Harris <mharris@redhat.com> 1.83.1-14
- Added Requires: lockdev (#51576)
- s/Copyright/License/

* Sat Jul 28 2001 Jeff Johnson <jbj@redhat.com>
- use baudboy for serial port locking.

* Mon Jul 23 2001 Mike A. Harris <mharris@redhat.com> 1.83.1-12
- Added minicom-1.83.1-disable-message.patch to disable warning message and
  delay when running minicom as root since root-only is the only supported
  method of running minicom now due to security issues.
  
* Sat Jul 21 2001 Tim Powers <timp@redhat.com> 1.83.1-11
- no minicom applnk entry. Is cluttering up the menus

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add ExcludeArch: s390 s390x
- allow to build with newer gettext versions

* Thu May  3 2001 Mike A. Harris <mharris@redhat.com> 1.83.1-8
- Changed minicom to disable SGID/SUID operation completely as it was
  never designed to be secure, and likely never will be. (#35613)
- Updated the format string patch I made to fix more format string abuses.
- Added Czeck cs_CZ locale translations.

* Thu Apr 12 2001 Mike A. Harris <mharris@redhat.com>
- Fixed format string vuln in usage of do_log()  (bug #35613)
- Fixed misc other format string abuse with werror().
- Changed main tarball to bzip2 compression
- Corrected Buildroot to use _tmppath

* Tue Mar 27 2001 Crutcher Dunnavant <crutcher@redhat.com>
- patch to drop mask for config file

* Fri Feb 23 2001 Jakub Jelinek <jakub@redhat.com>
- fix build under glibc 2.2.2

* Thu Aug 24 2000 Bill Nottingham <notting@redhat.com>
- drop privs on opening of capture file

* Fri Aug  4 2000 Bill Nottingham <notting@redhat.com>
- add translation to desktop entry

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- update to 1.83.1

* Wed Apr  5 2000 Bill Nottingham <notting@redhat.com>
- rebuild against current ncurses/readline

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description

* Fri Dec 17 1999 Bill Nottingham <notting@redhat.com>
- update to 1.83.0

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 1.82.1
- s/sunsite/metalab

* Wed May 19 1999 Jeff Johnson <jbj@redhat.com>
- restore setgid uucp to permit minicom to lock in /var/lock (#2922).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Tue Jan 24 1999 Michael Maher <mike@redhat.com>
- fixed bug, changed groups.

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- updated to 1.82 to include i18n fixes

* Wed Sep 02 1998 Michael Maher <mike@redhat.com>
- Built package for 5.2.

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- security fixes (alan cox, but he forgot about the changelog)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- BuildRoot; updated .make patch to cope with the buildroot
- fixed the spec file

* Tue May 06 1998 Michael Maher <mike@redhat.com>
- update of package (1.81)

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
