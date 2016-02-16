#https://stereochro.me/ideas/rpm-for-the-unwilling

startDir=$(pwd)
. ./setupDirectory.sh


cp ../packages/imagick/imagick.spec $RPM_DIR/SPECS/imagick.spec
cp ../packages/imagick/* $RPM_DIR/SOURCES/
cp ../zips/imagick/imagick-exportImagePixels.tar.gz $RPM_DIR/SOURCES/imagick-exportImagePixels.tar.gz

`



cd $RPM_DIR
rpmbuild --define "_topdir `pwd`" -ba SPECS/imagick.spec

. ${startDir}/copyAndRepo.sh





