
startDir=$(pwd)
. ./setupDirectory.sh

cp ../packages/ImageMagick/ImageMagick7.spec $RPM_DIR/SPECS/ImageMagick7.spec
cp ../zips/ImageMagick/ImageMagick-7.0.1-0.tar.gz $RPM_DIR/SOURCES/
cp ../packages/ImageMagick/policy.xml $RPM_DIR/SOURCES/policy.xml

cd $RPM_DIR 
rpmbuild --define "_topdir `pwd`" -ba SPECS/ImageMagick7.spec

. ${startDir}/copyAndRepo.sh
