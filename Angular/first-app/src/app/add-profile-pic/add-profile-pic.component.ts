import { Component, OnInit, Directive, Output, EventEmitter, HostBinding, HostListener } from '@angular/core';
import { DataService } from '../services/DataService/data-service.service';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { DomSanitizer } from '@angular/platform-browser';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-add-profile-pic',
  templateUrl: './add-profile-pic.component.html',
  styleUrls: ['./add-profile-pic.component.css']
})
export class AddProfilePicComponent implements OnInit {

  displayPicture;

  constructor(private dataService: DataService,
    public dialogBox : MatDialog) { }

  ngOnInit(): void {
  }

  openDialog(){
    const dialogRef = this.dialogBox.open(AddProfilePicDialogComponent, {
      width: '65%',
      height: '70%',
    })
  }
}


@Component({
  selector: 'app-add-profile-pic-dialog',
  templateUrl: 'add-profile-pic-dialog.component.html',
  styleUrls: ['add-profile-pic-dialog.component.css']
})



export class AddProfilePicDialogComponent{

  displayPictureUpload = null;
  imgUrl

  constructor(public dialogRef: MatDialogRef<AddProfilePicDialogComponent>,
    private dataService: DataService, 
    private domSanitizer: DomSanitizer,
    private snackbar: MatSnackBar){}

  getFileButton($event){
    console.log($event)
    this.displayPictureUpload = $event.target.files[0];
    var reader = new FileReader()
    reader.readAsDataURL(this.displayPictureUpload)
    setTimeout(() =>{
      this.imgUrl = reader.result
      this.imgUrl = this.domSanitizer.bypassSecurityTrustUrl(this.imgUrl)  
    }, 100)
  }

  getFile($event){
    console.log($event)
    this.displayPictureUpload = $event['file'];
    console.log('Image File:',this.displayPictureUpload)
    this.imgUrl = $event['url'];
    console.log('Image Url:', this.imgUrl)
  }
  
  close(){
    this.dialogRef.close(null)
  }

  uploadImage(){
    this.dataService.uploadProfilePicture(this.displayPictureUpload)
    .subscribe(response => {
      if(response['success'] === true){
        this.snackbar.open('SuccessFully Updated Profile Picture','close',{
          duration: 3000,
        })
        this.dialogRef.close()
      }else{
        this.snackbar.open('Unable to update profile pciture, Please try again', 'close', {
          duration: 3000
        })
      }
    })
  }

}
