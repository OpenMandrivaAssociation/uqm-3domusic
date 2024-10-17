%define base_name	uqm

Name:		%{base_name}-3domusic
Version:	0.8.0
Release:	1
Summary:	Optional 3DO music package for Ur-Quan Masters game
License:	GPL
Group:		Games/Strategy
URL:		https://sc2.sourceforge.net
Source:		http://sourceforge.net/projects/sc2/files/UQM/%(echo %{version} |cut -d. -f1-2)/uqm-%{version}-3domusic.uqm
Requires:	%{base_name}
BuildArch:	noarch

%description
The Ur-Quan Masters is a port of the 3DO version of Star Control 2.

%prep
%setup -c -q

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/%{base_name}/content/addons
cp -pr * %{buildroot}%{_gamesdatadir}/%{base_name}/content/addons/

%files
%defattr(-,root,root)
%{_gamesdatadir}/%{base_name}/content/addons/3domusic
