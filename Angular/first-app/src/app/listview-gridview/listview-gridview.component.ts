import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-listview-gridview',
  templateUrl: './listview-gridview.component.html',
  styleUrls: ['./listview-gridview.component.css']
})
export class ListviewGridviewComponent implements OnInit {

  toggleList:boolean;

  constructor() {
   }

  ngOnInit(): void {
    this.toggleList = false; 
  }

  switchView(){
    if (this.toggleList === true){
      return this.toggleList = false
    }else{
      return this.toggleList = true;
    }
  }

}
