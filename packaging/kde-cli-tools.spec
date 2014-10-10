# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kde-cli-tools

# >> macros
# << macros

Summary:    Tools based on KDE Frameworks 5 to better interact with the system
Version:    5.1.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kde-cli-tools.yaml
Source101:  kde-cli-tools-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kdesu-devel
BuildRequires:  kdelibs4support-devel

%description
Tools based on KDE Frameworks 5 to better interact with the system.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_kf5_bindir}/kcmshell5
%{_kf5_bindir}/kde-open5
%{_kf5_bindir}/kdecp5
%{_kf5_bindir}/kdemv5
%{_kf5_bindir}/keditfiletype5
%{_kf5_bindir}/kioclient5
%{_kf5_bindir}/kmimetypefinder5
%{_kf5_bindir}/kstart5
%{_kf5_bindir}/ksvgtopng5
%{_kf5_bindir}/ktraderclient5
%{_kf5_libdir}/libkdeinit5_kcmshell5.so
%{_kf5_plugindir}/kcm_filetypes.so
%{_kf5_libdir}/libexec/kdeeject
%{_kf5_libdir}/libexec/kdesu
%{_kf5_htmldir}/en/kdesu
%{_kf5_servicesdir}/filetypes.desktop
%{_mandir}/man1/kdesu.1.gz
# >> files
# << files
