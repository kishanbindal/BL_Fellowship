import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-color-picker',
  templateUrl: './color-picker.component.html',
  styleUrls: ['./color-picker.component.css']
})
export class ColorPickerComponent implements OnInit {
  
  dialogRef;
  state;

  constructor(public dialog : MatDialog) { 
    this.dialogRef = dialog;
    this.state = null;
  }

  ngOnInit(): void {
  }

  openColorDialog(event){
      
      var positionX = event.pageX+ 'px';
      console.log(positionX);
      var positionY = event.pageY + 'px';
      console.log(positionY);


      this.state = this.dialogRef.open(ColorPickerDialogComponent,{
      width: "10em",
      height: "10em",
      position : {left :positionX, top: positionY},
    });

    this.state.afterClosed().subscribe(result => {
      console.log("Color Picker Dialog Closed")
    });
  }

// For Mouse Leave property.

  // closeColorDialog(){
  //   this.state.close()
  // }

}

//Color Picker Dialog Component

@Component({
  selector: "app-color-picker-dialog",
  templateUrl: "color-picker-dialog.components.html"
})

export class ColorPickerDialogComponent {}
