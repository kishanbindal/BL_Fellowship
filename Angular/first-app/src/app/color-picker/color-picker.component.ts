import { Component, OnInit, Inject, Output, EventEmitter } from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { element } from 'protractor';


@Component({
  selector: 'app-color-picker',
  templateUrl: './color-picker.component.html',
  styleUrls: ['./color-picker.component.css']
})
export class ColorPickerComponent implements OnInit {
  
  @Output() sendColor = new EventEmitter()
  dialogRef;
  state;
  color:string;

  constructor(public dialog : MatDialog) { 
    this.dialogRef = dialog;
    this.state = null;
  }

  ngOnInit(): void {
  }

  openColorDialog(event){
      
      // let source_element = event.srcElement;
      // console.log(event.srcElement)
      // console.log(event)
      let rect = event.target.getBoundingClientRect()
      console.log(rect)
      let leftX = rect.x + 'px';
      let topY = (rect.y +40) + 'px';
      // var positionX = event.pageX + 'px'//event.position+ 'px';
      // console.log(positionX);
      // var positionY = event.pageY + 'px';
      // console.log(positionY);


      this.state = this.dialogRef.open(ColorPickerDialogComponent,{
      width: "14.5em",
      height: "12.25em",
      position : {left :leftX, top: topY},
    });

    this.state.afterClosed().subscribe(result => {
      this.color = result
      this.sendColor.emit(this.color)
      // console.log(`Result in color-picker :  ${this.color}`)
    });
  }
}

//Color Picker Dialog Component

@Component({
  selector: "app-color-picker-dialog",
  templateUrl: "color-picker-dialog.components.html",
  styleUrls:["color-picker-dialog.component.css"]
})

export class ColorPickerDialogComponent {

  @Output() sendColor = new EventEmitter(false);
  color: string;

  constructor(public dialogRef: MatDialogRef<ColorPickerDialogComponent>){}

  pickColor($event){
    const element = $event.srcElement;
    console.log(element.style.backgroundColor);
    this.color = element.style.backgroundColor;
    console.log(this.color);
    this.dialogRef.close(this.color)
  }

  // sendColorToParent(){
  //   console.log('Emitting Event')
  //   let x = this.sendColor.emit(this.color); 
  // }

}
