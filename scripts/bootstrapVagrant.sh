#!/bin/bash


intahwebzGroup="www-data"

cd /tmp

#Also set the directories shared through vagrant
guest=0

#echo "The number of arguments is: $#"
#a=${@}
#echo "The total length of all arguments is: ${#a}: "
count=0
for var in "$@"
do
    if [ ${#var} ]; then
        guest=1
    fi
done

echo "guest is ${guest}"

# cd /home/github/PackageTest/PackageTest

#Huge download!
# yum -y upgrade
echo "Installing gcc make ruby ruby-devel ruby-libs rubygems"
# yum -y install gcc make ruby ruby-devel ruby-libs rubygems

yum -y install gcc make
yum -y install autoconf bison re2c bzip2-devel libcurl-devel libjpeg-turbo-devel libpng-devel libxml2-devel freetype-devel libpng libjpeg-turbo libmcrypt-devel libicu-devel libyaml-devel git ghostscript gcc gcc-c++ openssl-devel siege strace fftw fftw-devel rpm-build pcre-devel createrepo libyaml-devel jasper-devel lcms-devel libX11-devel libXext-devel libXt-devel ghostscript-devel libtiff-devel libwebp-devel giflib-devel libtool valgrind jasper
#Sphinx packages
#package "babel"
#package "setuptools"
#package "elementtree"
#package "meld3"
#package "Sphinx"
#package "snowballstemmer"
#package "docutils"
#package "Pygments"
#package "Jinja2"
#package "six"
#package "pytz"
#package "MarkupSafe"






# update RubyGems
# echo "Forget updating gems"

# This is disabled because it takes approximately forever
#echo "Updating gems"
#gem update --system

echo "installing chef"
#Force version 1.25 because the newer versions need a later version of Ruby that the on
#we have installed

#gem install mime-types -v 1.25 --no-rdoc --no-ri
# gem install chef ohai --no-rdoc --no-ri
# gem install chef ohai travis --no-rdoc --no-ri

# if ! gem spec mime-types > /dev/null 2>&1; then
#   echo "gem install mime-types -v 1.25 --no-rdoc --no-ri"
#   gem install mime-types -v 1.25 --no-rdoc --no-ri
# fi

# if ! gem spec chef > /dev/null 2>&1; then
#   echo "gem install chef --no-rdoc --no-ri"
#   gem install chef -v 1.25 --no-rdoc --no-ri
# fi

#if ! gem spec ohai > /dev/null 2>&1; then
#  gem install ohai -v 1.25 --no-rdoc --no-ri
#fi

#if ! gem spec travis > /dev/null 2>&1; then
#  gem install travis -v 1.25 --no-rdoc --no-ri
#fi


mkdir -p /etc/chef

cd /home/github/BastionRPM
chef-solo -c conf/chef/config.rb -j conf/chef/node_centos.json
cd /home/github
gpg --import basereality-GPG-KEY.private

# These are to allow us to build signed rpms
sudo echo "%_signature gpg" > /root/.rpmmacros
sudo echo "" >> /root/.rpmmacros
sudo echo "%_gpg_name Dan Ackroyd" >> /root/.rpmmacros


# sudo rpm --import ../basereality-GPG-KEY.private