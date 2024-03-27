Name     : qt6ct
Version  : 0.9
Release  : 1
URL      : https://github.com/trialuser02/qt6ct
Source0  : https://github.com/trialuser02/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary  : Qt 6 Configuration Tool
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6svg-dev qt6tools-dev
BuildRequires : xkbcomp-dev
BuildRequires : qttools-dev
BuildRequires:  Vulkan-Loader-dev 
BuildRequires:  Vulkan-Headers-dev
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(xpresent)
BuildRequires : pkgconfig(xv)


%description
qt6ct - Qt6 Configuration Tool
This program allows users to configure Qt5 settings (theme, font, icons, etc.)
under DE/WM without Qt integration.


%prep
%setup -q -n qt6ct-%{version}
cd %{_builddir}/qt6ct-%{version}

%build
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666226559
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "    
%cmake ..
make  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/bin/qt6ct
/usr/share/applications/qt6ct.desktop
/usr/share/qt6ct/
/usr/lib64/

# based on https://github.com/clearlinux-pkgs/qt5ct 
