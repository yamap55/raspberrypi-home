var fs = require('fs');
var google = require('googleapis');
var googleAuthWrapper = require("./googleDrive.js")

googleAuthWrapper.execute(a);

function a(auth) {
  var fileMetadata = {
    'name': 'photo.jpg',
    parents:[process.env.GOOGLE_DRIVE_FOLDER_ID]
  };
  var media = {
    mimeType: 'image/jpeg',
    // body: fs.createReadStream('/Users/yamap_55/Desktop/omocha_robot.png')
    body: fs.createReadStream(process.argv[2])
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
