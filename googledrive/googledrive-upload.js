var fs = require('fs');
var google = require('googleapis');
var googleAuthWrapper = require("./googledrive.js")

const photoPath = process.argv[2]
const splitList = photoPath.split("/")
const fileName = splitList[splitList.length - 1]

googleAuthWrapper.execute(a);

function a(auth) {
  var fileMetadata = {
    'name': fileName,
    parents:[process.env.GOOGLE_DRIVE_FOLDER_ID]
  };
  var media = {
    mimeType: 'image/jpeg',
    // body: fs.createReadStream('/Users/yamap_55/Desktop/omocha_robot.png')
    body: fs.createReadStream(photoPath)
  };
  var service = google.drive('v3');
  service.files.create({
    auth: auth,
    resource: fileMetadata,
    media: media,
    fields: 'id'
  }, function (err, file) {
    if (err) {
      // Handle error
      console.error(err);
    } else {
      console.log('File Id: ', file.id);
    }
  });
}
