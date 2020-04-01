import { Component, OnInit, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-listview-gridview',
  templateUrl: './listview-gridview.component.html',
  styleUrls: ['./listview-gridview.component.css']
})
export class ListviewGridviewComponent implements OnInit {

  toggleList:boolean;

  @Output() listSignal= new EventEmitter(false)

  constructor() {
   }

  ngOnInit(): void {
    this.toggleList = false; 
  }

  switchView(){
    if (this.toggleList === true){
      this.listSignal.emit(false)
      return this.toggleList = false
    }else{
      this.listSignal.emit(true)
      return this.toggleList = true;
    }
  }

}
