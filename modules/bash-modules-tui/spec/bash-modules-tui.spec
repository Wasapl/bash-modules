
Name:           bash-modules-tui
Version:        2.0.2
Release:        1%{?dist}
Summary:        Modules for bash to implement basic TUI

Group:          System Environment/Base
URL:            http://trac.assembla.com/bash-modules/
License:        LGPLv2.1+
Source0:        %{name}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:  bash-modules
Requires:       bash
Requires:       bash-modules

%define  homedir /usr/share/bash-modules

%description
Optional modules to use with bash to implement basic text mode interface.

%prep
%setup -q -n %{name}


%build
# Nothing to do
#(
#  cd test
#  exec /bin/bash ./test.sh -q
#)

%install
rm -rf "$RPM_BUILD_ROOT"


mkdir -p "$RPM_BUILD_ROOT%homedir/"
cp -a src/bash-modules/* "$RPM_BUILD_ROOT%homedir/"

%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(644,root,root,755)
%doc COPYING* README Changelog doc/

%homedir


%changelog
* Tue Jul 16 2013 Volodymyr M. Lisivka <vlisivka@gmail.com> - 2.0.2-2
- License tag changed from LGPL to LGPL2.1+
