%define version 0.6.1
%define release %mkrel 1
%define name	typespeed

Name:		%name
Summary:	type words that are flying by from left to right as fast as you can
License:	GPL
URL:		http://tobias.eyedacor.org/typespeed/
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
%configure docdir=%{_datadir}/doc/%{name}-%{version}
%make

%install
%makeinstall
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
Encoding=UTF-8
X-Desktop-File-Install-Version=0.9
EOF

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/README COPYING NEWS TODO BUGS AUTHORS
%config %{_sysconfdir}/typespeedrc
%attr(2755,root,games) %{_bindir}/%{name}
%attr(775,root,games) %{_localstatedir}/games/%{name}.score
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/locale/de_DE/LC_MESSAGES/%{name}.mo
%{_datadir}/applications/mandriva-%{name}.desktop

