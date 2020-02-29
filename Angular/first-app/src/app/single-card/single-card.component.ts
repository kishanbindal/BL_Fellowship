import { Component, OnInit, Input, Inject } from '@angular/core';
import { componentFactoryName } from '@angular/compiler';
import { MatDialog, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';


@Component({
  selector: 'app-single-card',
  templateUrl: './single-card.component.html',
  styleUrls: ['./single-card.component.css']
})
export class SingleCardComponent implements OnInit {
  
  @Input() note;

  constructor(public dialog: MatDialog) { 
  }

  ngOnInit(): void {
  }

  showNoteDialog(){
    const dialogRef = this.dialog.open(SingleCardDialogComponent,{
      width: "45em",
      height: "16.5em",
      data : this.note,
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log("Note Dialog Box Closed");
    });
  }
}

// SingleCardDialogComponent

@Component({
  selector: "app-single-card-component",
  templateUrl: "single-card-dialog.component.html",
  styleUrls: ['./single-card-dialog.component.css']
})

export class SingleCardDialogComponent {

  constructor(
    public dialogRef: MatDialogRef<SingleCardDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data:any){}

    closeDialog(){
      this.dialogRef.close()
    }
}

