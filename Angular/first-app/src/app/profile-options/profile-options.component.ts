import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { LogoutService } from '../services/logout-service/logout.service';

// User Icon Component
@Component({
  selector: 'app-profile-options',
  templateUrl: './profile-options.component.html',
  styleUrls: ['./profile-options.component.css']
})
export class ProfileOptionsComponent implements OnInit {

  // clicked:boolean;

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
    // this.clicked = false
  }

  openProfileDialog():void {
    console.log('Clicked on profile to open Dialog Box')
    const dialogRef = this.dialog.open(ProfileOptionsDialogComponent,{
      width: '25em',
      height: '30em',
      position: {right: '0', top: '65px'},
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

  constructor(private logout: LogoutService){}

  logOut(){
    this.logout.logUserOut();
  }
}
