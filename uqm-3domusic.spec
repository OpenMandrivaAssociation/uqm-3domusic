%define base_name	uqm
%define name		%{base_name}-3domusic
%define version		0.6.0
%define release		%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Optional 3DO music package for Ur-Quan Masters game
License:	GPL
Group:		Games/Strategy
URL:		http://sc2.sourceforge.net
Source:		http://prdownloads.sourceforge.net/sc2/%{base_name}-%{version}-3domusic.uqm
Requires:	%{base_name}
BuildArch:	    noarch
ExcludeArch:    x86_64 amd64
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The Ur-Quan Masters is a port of the 3DO version of Star Control 2.

%prep
%setup -c -q

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}/content
cp -pr * %{buildroot}%{_gamesdatadir}/%{base_name}/content

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{base_name}/content/credits/*
%{_gamesdatadir}/%{base_name}/content/ipanims/*
%{_gamesdatadir}/%{base_name}/content/lbm/*




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-7mdv2010.0
+ Revision: 434568
- rebuild
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0-5mdv2009.0
+ Revision: 255182
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.6.0-3mdv2008.1
+ Revision: 140925
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Feb 14 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-3mdv2007.0
+ Revision: 121006
- drop versioning on base package dependency

* Thu Jan 25 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-2mdv2007.1
+ Revision: 113142
- game engine is not x86_64 compatible, so mark content as noarch too
- new version
- Import uqm-3domusic

* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-3mdv2007.0
- Rebuild

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-2mdk
- fix new directory dupliaction

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1mdk
- new version
- use original archive
- fix directory duplication with uqm-content

* Wed Aug 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-2mdk
- use correct archive
- %%mkrel

* Tue May 31 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.0-1mdk 
- first release as a distinct package

