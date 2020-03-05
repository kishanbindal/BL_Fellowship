import { Component, OnInit, Output, EventEmitter } from '@angular/core';
// import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-upload-note-image',
  templateUrl: './upload-note-image.component.html',
  styleUrls: ['./upload-note-image.component.css']
})
export class UploadNoteImageComponent implements OnInit {
  
  @Output() sendFile = new EventEmitter()

  uploadFile=null;

  constructor() { } //private domSanitizer: DomSanitizer

  ngOnInit(): void {
  }

  getFile($event){
    console.log($event);
    this.uploadFile = $event.target.files[0];
    console.log(this.uploadFile)
    var reader = new FileReader();
    reader.readAsDataURL(this.uploadFile);
    //reader.result
    setTimeout(()=>{
      // let imgUrl = JSON.stringify(reader.result);
      // var preview = this.domSanitizer.bypassSecurityTrustUrl(imgUrl)
      this.sendFile.emit([this.uploadFile, reader.result]);
    }, 500);
  }
}
