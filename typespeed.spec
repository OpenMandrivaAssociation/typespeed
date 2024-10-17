%define version 0.6.5
%define release 10
%define name	typespeed




Name:		%name
Summary:	Type words that are flying by from left to right as fast as you can
License:	GPLv2+
URL:		https://tobias.eyedacor.org/typespeed/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Source:		http://tobias.eyedacor.org/typespeed/%{name}-%{version}.tar.gz
Group:		Games/Other
Version:	%version
Release:	%release
BuildRequires:	ncurses-devel, gettext-devel

%description
Typespeed gives your fingers' cps (total and correct), typoratio and
some points to compare with your friends.

Typespeed's idea is ripped from ztspeed (a dos game made by Zorlim).
Idea of the game should be clear to anyone, just type and type it fast
or be a loser.

%prep
%setup -q

%build
%configure --with-highscoredir=%{_localstatedir}/lib/games
%make

%install
%makeinstall highscoredir=$RPM_BUILD_ROOT%{_localstatedir}/lib/games
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/README
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Typespeed
Comment=Test your typing speed
Exec=/usr/bin/typespeed
Type=Application
Terminal=true
Categories=X-MandrivaLinux-MoreApplications-Games-Other;Game;Application;
X-Desktop-File-Install-Version=0.9
EOF

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/README COPYING NEWS TODO BUGS AUTHORS
%config(noreplace) %{_sysconfdir}/typespeedrc
%attr(2755,root,games) %{_bindir}/%{name}
%attr(775,root,games) %{_localstatedir}/lib/games/%{name}.score
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/locale/de_DE/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/fr_FR/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/it/LC_MESSAGES/%{name}.mo
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Sat Jul 10 2010 Nicolas Vigier <nvigier@mandriva.com> 0.6.5-9mdv2011.0
+ Revision: 549903
- eating french fries, drinking valstar and updating typespeed

* Sat Jul 10 2010 Nicolas Vigier <nvigier@mandriva.com> 0.6.5-8mdv2011.0
+ Revision: 549899
- Frites !
- bump release
- rebuild

* Sat Jul 04 2009 Nicolas Vigier <nvigier@mandriva.com> 0.6.5-5mdv2010.0
+ Revision: 392300
- rebuild

* Fri Jun 19 2009 Nicolas Vigier <nvigier@mandriva.com> 0.6.5-4mdv2010.0
+ Revision: 387294
- fix score file path
- rebuild

* Sun Mar 22 2009 Nicolas Vigier <nvigier@mandriva.com> 0.6.5-2mdv2009.1
+ Revision: 360543
- rebuild

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.6.5-1mdv2009.0
+ Revision: 280695
- New Release

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.6.4-4mdv2009.0
+ Revision: 261746
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.6.4-3mdv2009.0
+ Revision: 255035
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 01 2007 Nicolas Vigier <nvigier@mandriva.com> 0.6.4-1mdv2008.1
+ Revision: 114272
- new version

* Fri Nov 16 2007 Nicolas Vigier <nvigier@mandriva.com> 0.6.3-1mdv2008.1
+ Revision: 109097
- update to new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Fri Jun 01 2007 Nicolas Vigier <nvigier@mandriva.com> 0.6.2-1mdv2008.0
+ Revision: 34038
- version 0.6.2

* Fri May 04 2007 Nicolas Vigier <nvigier@mandriva.com> 0.6.1-1mdv2008.0
+ Revision: 22467
- Import typespeed

