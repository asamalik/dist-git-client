Name:		fedpkg-copr
Version:	0
Release:	1%{?dist}
Summary:	Fedpkg modified to work with copr dist git

Group:		Applications/Productivity
License:	GPLv2+
URL:		http://nothing.example.com
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	
Requires:	fedpkg
Requires:	pyrpkg

%description
This is a quick and dirty solution. It's a modified version of
fedpkg that works with repos named user/project/package


%prep
%setup -q


%build


%install
cp -a fedpkg-copr         %{buildroot}%{_bindir}/
cp -a fedpkg-copr.conf    %{buildroot}%{_sysconfdir}/


%files
%license LICENSE
%doc README

%config(noreplace)  %{_sysconfdir}/fedpkg-copr.conf
%{_bindir}/fedpkg-copr



%changelog

