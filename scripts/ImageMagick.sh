
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/ImageMagick/ImageMagick.spec $RPM_DIR/SPECS/ImageMagick.spec
cp ../zips/ImageMagick/ImageMagick-6.9.2-0.tar.gz $RPM_DIR/SOURCES/
cp ../packages/ImageMagick/policy.xml $RPM_DIR/SOURCES/policy.xml

cd $RPM_DIR 
rpmbuild --define "_topdir `pwd`" -ba SPECS/ImageMagick.spec

. ${startDir}/copyAndRepo.sh


