%define base_name	uqm
%define name		%{base_name}-3domusic
%define version		0.6.0
%define release		%mkrel 3

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


