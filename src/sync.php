<?php

require_once(realpath(__DIR__).'/../vendor/autoload.php');

require_once(realpath(__DIR__).'/../../BastionRPMConfig.php');


use Aws\S3\S3Client;
use Bastion\S3Sync;
use Bastion\S3ACLNoRestrictionGenerator;

$aclGenerator = new S3ACLNoRestrictionGenerator();

if (ini_get('allow_url_fopen') == false) {
    echo "Needs to be run with allow_url_fopen enabled.";
    exit(-1);
}

//if (false) {
//    //Theoretically this should be used but the uploading sometimes fails, and retyping
//    in the password for signing is too annoying
//    $syncTime = filemtime("sign.time");
//    $now = time();
//    if (($now - $syncTime) > 5) {
//        echo "sign.time is more than 5 seconds old - the RPM files have not been signed recently, so aborting upload.";
//        exit(-1);
//    }
//}


$urlList = [
    "/index.html",
    "/RPMS/noarch/index.html",
    "/RPMS/x86_64/index.html",
    "/RPMS/index.html",
];


$s3Client = S3Client::factory([
    'key' => $s3Key,
    'secret' => $s3Secret,
    'region' => $s3Region
]);

$s3Client->getConfig()->set('curl.options', array(CURLOPT_VERBOSE => true));

$sync = new S3Sync($rpmBucketName, $aclGenerator,  $s3Client);

try {
    $sync->putFile("../repo/index.html", "index.html");
    $sync->putFile("../repo/basereality-GPG-KEY.public", "basereality-GPG-KEY.public");
    $sync->syncDirectory("../repo/RPMS", "RPMS");
    $sync->syncDirectory("../repo/RPMS/x86_64", "RPMS/x86_64");
    $sync->syncDirectory("../repo/SRPMS", "SRPMS");
    $sync->finishProcessing();
}
catch (\Exception $e) {

    echo $e->getMessage();
    echo "\n";
    echo $e->getTraceAsString();
    echo "\n";
}

/*

// arn:aws:s3:::rpm.basereality.com

//Complete
{
    "Version": "2012-10-17",
    "Statement": [
        {
            
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:PutObject",
                "s3:GetObjectAcl",
                "s3:GetObjectVersionAcl",
                "s3:PutObjectAcl",
                "s3:PutObjectVersionAcl",
                "s3:DeleteObject",
                "s3:DeleteObjectVersion",
                "s3:ListMultipartUploadParts",
                "s3:AbortMultipartUpload",
                "s3:GetObjectTorrent",
                "s3:GetObjectVersionTorrent",
                "s3:RestoreObject",
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:ListAllMyBuckets",
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketAcl",
                "s3:PutBucketAcl",
                "s3:GetBucketCORS",
                "s3:PutBucketCORS",
                "s3:GetBucketVersioning",
                "s3:PutBucketVersioning",
                "s3:GetBucketRequestPayment",
                "s3:PutBucketRequestPayment",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicy",
                "s3:DeleteBucketPolicy",
                "s3:PutBucketPolicy",
                "s3:GetBucketNotification",
                "s3:PutBucketNotification",
                "s3:GetBucketLogging",
                "s3:PutBucketLogging",
                "s3:GetBucketTagging",
                "s3:PutBucketTagging",
                "s3:GetBucketWebsite",
                "s3:PutBucketWebsite",
                "s3:PutReplicationConfiguration"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:GetObjectAcl",
                "s3:PutObjectAcl",
                "s3:ListBucket",
                "s3:ListAllMyBuckets",
                "s3:GetBucketAcl",
                "s3:PutBucketAcl",
                "s3:GetBucketPolicy",
                "s3:PutBucketPolicy"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}





*/

/*


"s3:GetObject",
"s3:GetObjectVersion",
"s3:PutObject",
"s3:GetObjectAcl",
"s3:GetObjectVersionAcl",
"s3:PutObjectAcl",
"s3:PutObjectVersionAcl",
"s3:DeleteObject",
"s3:DeleteObjectVersion",
"s3:ListMultipartUploadParts",
"s3:AbortMultipartUpload",
"s3:GetObjectTorrent",
"s3:GetObjectVersionTorrent",
"s3:RestoreObject",
"s3:CreateBucket",
"s3:DeleteBucket",
"s3:ListBucket",
"s3:ListBucketVersions",
"s3:ListAllMyBuckets",
"s3:ListBucketMultipartUploads",
"s3:GetBucketAcl",
"s3:PutBucketAcl",
"s3:GetBucketCORS",
"s3:PutBucketCORS",
"s3:GetBucketVersioning",
"s3:PutBucketVersioning",
"s3:GetBucketRequestPayment",
"s3:PutBucketRequestPayment",
"s3:GetBucketLocation",
"s3:GetBucketPolicy",
"s3:DeleteBucketPolicy",
"s3:PutBucketPolicy",
"s3:GetBucketNotification",
"s3:PutBucketNotification",
"s3:GetBucketLogging",
"s3:PutBucketLogging",
"s3:GetBucketTagging",
"s3:PutBucketTagging",
"s3:GetBucketWebsite",
"s3:PutBucketWebsite",
"s3:DeleteBucketWebsite",
"s3:GetLifecycleConfiguration",
"s3:PutLifecycleConfiguration",
"s3:PutReplicationConfiguration",
"s3:GetReplicationConfiguration",
"s3:DeleteReplicationConfiguration",


*/