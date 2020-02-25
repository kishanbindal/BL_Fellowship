import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-collaborators',
  templateUrl: './collaborators.component.html',
  styleUrls: ['./collaborators.component.css']
})
export class CollaboratorsComponent implements OnInit {

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openCollaboratorDialog(): void{
    const dialogRef = this.dialog.open(CollaboratorsDialogBoxComponent, {
      width: "25em",
      height: "25em",
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log("Collaborators DialogBox Closed!");
    })
  }
}

//CollaboratorsDialogBox

@Component({
  selector: "app-collaborators-dialog-box",
  templateUrl: "collaborators-dialog-box.component.html"
})

export class CollaboratorsDialogBoxComponent {}
