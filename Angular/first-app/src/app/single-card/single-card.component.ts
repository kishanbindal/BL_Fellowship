import { Component, OnInit } from '@angular/core';
import { componentFactoryName } from '@angular/compiler';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-single-card',
  templateUrl: './single-card.component.html',
  styleUrls: ['./single-card.component.css']
})
export class SingleCardComponent implements OnInit {

  constructor(public dialog: MatDialog) { 
  }

  ngOnInit(): void {
  }
  showNoteDialog(){
    const dialogRef = this.dialog.open(SingleCardDialogComponent,{
      width: "45em",
      height: "15em"
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log("Note Dialog Box Closed");
    });
  }
}

// SingleCardDialogComponent

@Component({
  selector: "app-single-card-component",
  templateUrl: "app-single-card-dialog.component.html"
})

export class SingleCardDialogComponent {}

