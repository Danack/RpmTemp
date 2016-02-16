# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

%define date %(date +%%Y_%%m_%%d) 

%global php_extdir  %(php-config --extension-dir 2>/dev/null || echo "undefined")

%global php_major_version  %(php-config --vernum 2>/dev/null | cut -c1 || echo "undefined")
%global php_minor_version  %(php-config --vernum 2>/dev/null | cut -c3 || echo "undefined")


%global php_version %{php_major_version}.%{php_minor_version}

Summary: A test imagick rpm package
Name: imagick-php%{php_version}-%{date}
Version: 3.4.0RC3
Release: 1
License: None
Group: Development/Tools
SOURCE0 : imagick-master.tar.gz
SOURCE1 : imagick.ini
URL: http://www.phpimagick.com/

#AutoReqProv: no

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q -n imagick-master
#%setup -q -n imagick-exportImagePixels


%build
rm -rf %{buildroot}
mkdir -p  %{buildroot}

#export CFLAGS="-Wno-deprecated-declarations -Wdeclaration-after-statement -Wall -Werror"
export CFLAGS="-Wno-deprecated-declarations -Wdeclaration-after-statement -Wall"
phpize
./configure --libdir=/usr/lib64
#./configure --libdir=/usr/lib64 --with-php-config=/usr/local/bin/php-config
# --enable-imagick-version-name
make

%install
#mkdir -p %{buildroot}/usr/local/lib/php/extensions/no-debug-zts-20131226/
mkdir -p %{buildroot}%{php_extdir}
mkdir -p %{buildroot}/etc/php.d
cp %{SOURCE1} %{buildroot}/etc/php.d/imagick.ini

pwd
# %{__install} -m 755 ./modules/imagick.so %{buildroot}/usr/local/lib/php/extensions/no-debug-zts-20131226/imagick.so
%{__install} -m 755 ./modules/imagick.so %{buildroot}%{php_extdir}/imagick.so

# in builddir
# cp -a * %{buildroot}

%clean
 # rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# %doc doc/*
%dir /usr/local
%dir /usr/local/lib/
%dir /usr/local/lib/php/
%dir /usr/local/lib/php/extensions/
%dir %{php_extdir}
%dir /etc/php.d
%{php_extdir}/*.so
/etc/php.d/imagick.ini


#%dir /usr/local/lib/php/extensions/no-debug-zts-20131226
#/usr/local/lib/php/extensions/no-debug-zts-20131226/imagick.so

%changelog
* Thu Apr 24 2009  Elia Pinto <devzero2000@rpm5.org> 1.0-1
- First Build

EOF
