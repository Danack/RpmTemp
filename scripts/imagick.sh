#https://stereochro.me/ideas/rpm-for-the-unwilling

startDir=$(pwd)
. ./setupDirectory.sh

yum -y install ImageMagick-2015_09_19-devel-6.9.2


cp ../packages/imagick/imagick.spec $RPM_DIR/SPECS/imagick.spec
cp ../packages/imagick/* $RPM_DIR/SOURCES/
cp ../zips/imagick/imagick-3.4.0RC3/imagick-master.tar.gz $RPM_DIR/SOURCES/imagick-master.tar.gz

cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/imagick.spec

. ${startDir}/copyAndRepo.sh