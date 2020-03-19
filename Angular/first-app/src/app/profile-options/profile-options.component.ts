import { Component, OnInit, Inject } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { LogoutService } from '../services/logout-service/logout.service';
import { disableDebugTools } from '@angular/platform-browser';
import { DataService } from '../services/DataService/data-service.service';

// User Icon Component
@Component({
  selector: 'app-profile-options',
  templateUrl: './profile-options.component.html',
  styleUrls: ['./profile-options.component.css']
})
export class ProfileOptionsComponent implements OnInit {

  // clicked:boolean;

  userDetailsArray

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
    // this.clicked = false
    this.userDetailsArray = localStorage.getItem('user').split(',');
    console.log('Profile Options Array : ', this.userDetailsArray);
  }

  openProfileDialog():void {
    console.log('Clicked on profile to open Dialog Box')
    const dialogRef = this.dialog.open(ProfileOptionsDialogComponent,{
      width: '15em',
      height: '7.5em',
      position: {right: '0', top: '65px'},
      data: this.userDetailsArray,
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('Dialog Box Closed');
    })
  }

}

//DialogBox Component

@Component({
  selector: "app-profile-options-dialog",
  templateUrl: "profile-options-dialog.components.html"
})

export class ProfileOptionsDialogComponent {

  displayPicture;

  constructor(private logout: LogoutService,
    public dialogRef: MatDialogRef<ProfileOptionsDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data,
    public dataService: DataService,
    ){
      console.log('Dialog Data: ', data)
      console.log(typeof(data))
    }

  uploadImage($event){
    // console.log($event)
    this.displayPicture = $event.target.files[0];
    console.log(this.displayPicture)
    this.dataService.uploadProfilePicture(this.displayPicture);
  }

  logOut(){
    this.logout.logUserOut(); 
    this.dialogRef.close();
  }
}
